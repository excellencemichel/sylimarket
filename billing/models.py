from django.conf import settings
from django.db.models.signals import pre_save, post_save

from django.urls import reverse

from django.db import models

from django.utils.translation import ugettext_lazy as _


import stripe

from accounts.models import GuestEmail


# Create your models here.


User = settings.AUTH_USER_MODEL

STRIPE_SECRET_KEY = getattr(settings, "STRIPE_SECRET_KEY", "sk_test_wIVcr24eoGW8iVGILTRPqK8y")

stripe.api_key = STRIPE_SECRET_KEY


class BillingProfileManager(models.Manager):

	def new_or_get(self, request):
		user = request.user
		guest_email_id 	= request.session.get("guest_email_id")
		created  = False
		obj = None
		if user.is_authenticated:
			"logged in user checkout; remember payment stuff"
			obj, created = self.model.objects.get_or_create(
								user = user, email=user.email)

		return obj, created


class BillingProfile(models.Model):
	user 			= models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	email 			= models.EmailField()
	active 			= models.BooleanField(default=True)
	update 			= models.DateTimeField(auto_now=True)
	timestamp 		= models.DateTimeField(auto_now_add=True)
	customer_id		= models.CharField(max_length=120, null=True, blank=True)
	# customer_id in Stripe or Braintree

	objects = BillingProfileManager()

	def __str__(self):
		return self.email


	def charge(self, order_obj, card=None):
		return Charge.objects.do(self, order_obj, card)


	def get_cards(self):
		return self.card_set.all()

	def get_payment_method_url(self):
		return reverse("billing:billing_payment_method")

	@property 
	def has_card(self): #instance.has_card
		card_qs = self.get_cards()
		return card_qs.exists() #return True or False

	@property
	def default_card(self):
		default_cards = self.get_cards().filter(active=True, default=True)
		if default_cards.exists():
			return default_cards.first()
		return None



	def set_cards_inactive(self):
		cards_qs 	= self.get_cards()
		cards_qs.update(active=False)
		return cards_qs.filter(active=True).count()



def billing_profile_created_receiver(sender, instance, *args, **kwargs):
	if not instance.customer_id and instance.email:
		customer 	= stripe.Customer.create(

				email = instance.email
			)
		instance.customer_id = customer.id


pre_save.connect(billing_profile_created_receiver, sender=BillingProfile)










class CardManager(models.Manager):
	def all(self, *args, **kwargs):
		return self.get_queryset().filter(active=True)
	def add_new(self, billing_profile, token):
		# if str(stripe_card_reponse.object) == "card":
		if token:
			customer = stripe.Customer.retrieve(billing_profile.customer_id)
			card_response = customer.sources.create(source=token)
			new_card = self.model(
				billing_profile 	= billing_profile,
				stripe_id 			= card_response.id,
				brand				= card_response.brand,
				country				= card_response.country,
				exp_month			= card_response.exp_month,
				exp_year			= card_response.exp_year,
				last4				= card_response.last4,


				)
			new_card.save()
			return new_card

		return None




class Card(models.Model):
	billing_profile 		= models.ForeignKey(BillingProfile, on_delete=models.CASCADE)
	stripe_id				= models.CharField(max_length=120)
	brand					= models.CharField(max_length=250, null=True, blank=True)
	country					= models.CharField(max_length=50, null=True, blank=True)
	exp_month				= models.IntegerField(null=True, blank=True)
	exp_year				= models.IntegerField(null=True, blank=True)
	last4					= models.CharField(max_length=4, null=True, blank=True)
	default 				= models.BooleanField(default=True)
	active 					= models.BooleanField(default=True)
	timestamp 				= models.DateTimeField(auto_now_add=True)


	objects		= CardManager()




	def __str__(self):
		return "{brand} {last4}".format(brand=self.brand, last4=self.last4)


def new_card_post_receiver(sender, instance,  *args, **kwargs):
	if instance.default:
		billing_profile = instance.billing_profile
		qs = Card.objects.filter(billing_profile=billing_profile).exclude(pk=instance.pk)
		qs.update(default=False)


post_save.connect(new_card_post_receiver, sender=Card)



	

class ChargeManager(models.Manager):
	def do(self, billing_profile, order_obj, card=None):
		card_obj = card
		if card_obj is None:
			cards = billing_profile.card_set.filter(default=True)
			if cards.exists():
				card_obj = cards.first()
		if card_obj is None:
			return False, "No cards Available"

		c 	= stripe.Charge.create(
			amount = int(order_obj.total * 100), # 39.99 * 100 --> 3999
			currency = "usd",
			customer = billing_profile.customer_id,
			source =  card_obj.stripe_id, #obtained with Stripe.js
			metadata = {"order_id": order_obj.order_id},
			)
		new_charge_obj 	= self.model(
				billing_profile = billing_profile,
				stripe_id = c.id,
				paid = c.paid,
				refunded = c.refunded,
				outcome = c.outcome,
				outcome_type = c.outcome["type"],
				seller_message  = c.outcome.get("seller_message"),
				risk_level 		= c.outcome.get("risk_level"),
			  )
		new_charge_obj.save()

		return new_charge_obj.paid, new_charge_obj.seller_message



class Charge(models.Model):
	billing_profile 		= models.ForeignKey(BillingProfile, on_delete=models.CASCADE)
	stripe_id 				= models.CharField(max_length=120)
	paid 					= models.BooleanField(default=False)
	refunded 				= models.BooleanField(default=False)
	outcome 				= models.TextField(null=True, blank=True)
	outcome_type 			= models.CharField(max_length=120, null=True, blank=True)
	seller_message 			= models.CharField(max_length=120, null=True, blank=True)
	risk_level	 			= models.CharField(max_length=120, null=True, blank=True)


	objects 	 = ChargeManager()


	def __str__(self):
		return str(self.billing_profile)





#################"" Payement à la livraison ""#########################################""


class PayementLivraisonManager(models.Manager):

	def new_or_get(self, request):
		user = request.user
		created  = False
		obj = None
		if user.is_authenticated:
			"logged in user checkout; remember payment stuff"
			obj, created = self.model.objects.get_or_create(
								user = user, email=user.email, mobile=user.mobile)
		else:
			pass

		return obj, created




class PayementLivraison(models.Model):
	user 				= models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	email 				= models.EmailField()
	mobile				= models.CharField(max_length=250)
	updated 			= models.DateTimeField(auto_now=True)
	timestamp 			= models.DateTimeField(auto_now_add=True)

	objects = PayementLivraisonManager()

	def __str__(self):
		return self.email














####################### Signaux ###############################




def user_created_receiver(sender, instance, created, *args, **kwargs):
	if created and instance.email:
		BillingProfile.objects.get_or_create(user=instance, email=instance.email)
	if created and instance.email and instance.mobile:
		PayementLivraison.objects.get_or_create(user=instance, email=instance.email, mobile=instance.mobile)



post_save.connect(user_created_receiver, sender=User)
