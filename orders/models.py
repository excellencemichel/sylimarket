from math import fsum
import datetime

from django.conf import settings

from django.db import models
from django.db.models.signals import pre_save, post_save
from django.db.models import Sum, Avg, Count 

from django.urls import reverse

from django.utils import timezone



#Locale import
from utils.generator_utils import unique_order_id_generator, unique_order_payement_livraison_id_generator

from billing.models import BillingProfile, PayementLivraison 
from carts.models import Cart, CartItem
from addresses.models import Address, AddressPayementLivraison
from products.models import Product 

# Create your models here.
User = settings.AUTH_USER_MODEL




class OrderManagerQuerySet(models.query.QuerySet):

	def recent(self):
		return self.order_by("-updated", "-timestamp")


	def get_sales_breakdown(self):
		recent = self.recent().not_refunded()
		recent_data = recent.totals_data()
		recent_cart_data = recent.cart_data()
		shipped = recent.not_refunded().by_status(status="shipped")
		shipped_data = shipped.totals_data()
		paid = recent.by_status(status="paid")
		paid_data = paid.totals_data()

		data = {
			"recent":recent,
			"recent_data" :recent_data,
			"recent_cart_data": recent_cart_data,
			"shipped" : shipped,
			"shipped_data" : shipped_data,
			"paid":paid,
			"paid_data": paid_data
		}
		return data
		
	def by_weeks_range(self, weeks_ago=7, number_of_weeks=2):
		if number_of_weeks > weeks_ago:
			number_of_weeks = weeks_ago
		days_ago_start = weeks_ago * 7
		days_ago_end = days_ago_start - (number_of_weeks * 7)
		# print(days_ago_start, days_ago_end)

		start_date = timezone.now() - datetime.timedelta(days=days_ago_start)
		end_date = timezone.now() - datetime.timedelta(days=days_ago_end)
		# print(start_date, end_date)
		return self.by_range(start_date=start_date, end_date=end_date)



	def by_range(self, start_date, end_date=None):
		if end_date is None:
			return self.filter(updated__gte=start_date)
		return self.filter(updated__gte=start_date).filter(updated__lt=end_date)

	def by_date(self):
		now = timezone.now() - datetime.timedelta(days=1)
		return self.filter(updated__day__gte=now.day)



	def totals_data(self):
		return self.aggregate(Sum("total"), Avg("total"))



	def cart_data(self):
		return self.aggregate(
					Sum("cart__products__price"),
					Avg("cart__products__price"),
					Count("cart__products")
			)


	def by_status(self, status="shipped"):
		return self.filter(status=status)


	def not_refunded(self):
		return self.exclude(status="refunded")

	def by_request(self, request):
		billing_profile, created = BillingProfile.objects.new_or_get(request)
		return self.filter(billing_profile=billing_profile)



	def not_created(self):
		return self.exclude(status="created")

class OrderManager(models.Manager):

	def get_queryset(self):
		return OrderManagerQuerySet(self.model, using=self._db)



	def by_request(self, request):
		return self.get_queryset().by_request(request)


	def new_or_get(self, billing_profile, cart_obj):
		created = False
		qs	= self.get_queryset().filter(
				billing_profile=billing_profile,
				cart=cart_obj,
				active=True, status="created")
		if qs.count() == 1:
			obj = qs.first()

		else:
			obj = self.model.objects.create(
						billing_profile=billing_profile,
						cart=cart_obj
						)
			created = True

		return obj, created


class Order(models.Model):

	STATUS_CREATED = "created"
	STATUS_PAID = "paid"
	STATUS_SHIPPED = "shipped"
	STATUS_REFUNDED = "refunded"


	ORDER_STATUS_CHOICES = (

		(STATUS_CREATED, "Created"),
		(STATUS_PAID, "Paid"),
		(STATUS_SHIPPED, "Shipped"),
		(STATUS_REFUNDED, "Refunded"),

	)
	billing_profile 	= models.ForeignKey(BillingProfile,  null=True, blank=True, on_delete=models.CASCADE)
	order_id			= models.CharField(max_length=120, blank=True) # Maybe AB18DE#
	shipping_address 	= models.ForeignKey(Address, related_name="shipping_address", null =True, blank=True, on_delete=models.CASCADE)
	billing_address		= models.ForeignKey(Address, related_name="billing_address", null=True, blank=True, on_delete=models.CASCADE) 
	cart 				= models.ForeignKey(Cart, on_delete=models.CASCADE)
	status  			= models.CharField(max_length=250, default="created", choices=ORDER_STATUS_CHOICES)
	shipping_total		= models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
	total				= models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
	active				= models.BooleanField(default=True)
	updated 			= models.DateTimeField(auto_now=True)
	timestamp 			= models.DateTimeField(auto_now_add=True)
	order_pdf			= models.FileField(upload_to="pdfs", null=True, blank=True)




	objects	= OrderManager()

	class Meta:
		ordering = ["-timestamp", "-updated"]
		verbose_name = "Commande avec payement à la carte bancaire"
		verbose_name_plural = "Commandes avec payements à la carte bancaire"

	def get_absolute_url(self):
		return reverse("orders:detail", kwargs={"order_id": self.order_id})



	def get_status(self):
		if self.status == "shipped":
			return "Shipped"

		elif self.status == "refunded":
			return "Refunded order"

		return "Shipped soon"


	def __str__(self):
		return self.order_id



	def update_total(self):
		cart_total = self.cart.total
		shipping_total = self.shipping_total
		new_total = fsum([cart_total, shipping_total])
		formatted_total = format(new_total, ".2f")
		print(type(new_total))
		self.total = formatted_total
		self.save()
		return new_total


	def check_done(self):
		billing_profile 	= self.billing_profile
		billing_address		= self.billing_address

		total = self.total


		if billing_profile and billing_address and total > 0:
			return True

		return False


	def update_purshases(self):
		for item in self.cart.items.all():
			obj, created  = ProductPurshase.objects.get_or_create(
				order_id = self.order_id,
				cart_item=item,
				billing_profile=self.billing_profile
				)

		return ProductPurshase.objects.filter(order_id=self.order_id).count()


	def mark_paid(self):
		if self.status != "paid":
			if self.check_done():
				self.status = "paid"
				self.save()
				self.update_purshases()
		return self.status




def pre_save_create_order_id(sender, instance, *args, **kwargs):
	if not instance.order_id:
		instance.order_id = unique_order_id_generator(instance)

	qs	= Order.objects.filter(cart=instance.cart).exclude(billing_profile=instance.billing_profile)
	if qs.exists():
		qs.update(active=False)





pre_save.connect(pre_save_create_order_id,sender=Order)



def post_save_cart_total(sender, instance, created, *args, **kwargs):
	if not created:
		cart_obj = instance
		cart_total = cart_obj.total
		cart_id = cart_obj.id 
		qs = Order.objects.filter(cart__id=cart_id)
		if qs.count() == 1:
			order_obj = qs.first()
			order_obj.update_total()



post_save.connect(post_save_cart_total, sender=Cart)



def post_save_order(sender, instance, created, *args, **kwargs):
	if created:
		instance.update_total()



post_save.connect(post_save_order, sender=Order)




class ProductPurshaseQuerySet(models.query.QuerySet):

	def active(self):
		return self.filter(refunded=False)


	def by_request(self, request):
		billing_profile, created = BillingProfile.objects.new_or_get(request)
		return self.filter(billing_profile=billing_profile)



class ProductPurshaseManager(models.Manager):

	def get_queryset(self):
		return ProductPurshaseQuerySet(self.model, using=self._db)

	def all(self):
		return self.get_queryset().active()



	def by_request(self, request):
		return self.get_queryset().by_request(request)


	def products_by_id(self, request):
		qs = self.by_request(request)#.digital()
		ids_ = [x.product.id for x in qs]
		return ids_



	def products_by_request(self, request):
		ids_ = self.products_by_id(request)
		product_qs  = Product.objects.filter(id__in=ids_).distinct()
		return product_qs

class ProductPurshase(models.Model): #Purshase veut dire achat
	order_id			= models.CharField(max_length=120)
	billing_profile 	= models.ForeignKey(BillingProfile,on_delete=models.CASCADE)
	cart_item 			= models.ForeignKey(CartItem, on_delete=models.CASCADE)
	refunded 			= models.BooleanField(default=False)
	updated 			= models.DateTimeField(auto_now=True)
	timestamp 			= models.DateTimeField(auto_now_add=True)


	objects = ProductPurshaseManager()


	class Meta:
		ordering = ["-timestamp", "-updated"]
		verbose_name = "Produit payé avec payement par carte bancaire"
		verbose_name_plural = "Produits payés avec payements par carte bancaire"

	def __str__(self):
		return self.product.title




###################################### Order payement à la livraison #########################""




class OrderPayementLivraisonManagerQuerySet(models.query.QuerySet):

	def recent(self):
		return self.order_by("-updated", "-timestamp")


	def get_sales_breakdown(self):
		recent = self.recent().not_refunded()
		recent_data = recent.totals_data()
		recent_cart_data = recent.cart_data()
		shipped = recent.not_refunded().by_status(status="shipped")
		shipped_data = shipped.totals_data()
		paid = recent.by_status(status="paid")
		paid_data = paid.totals_data()

		data = {
			"recent":recent,
			"recent_data" :recent_data,
			"recent_cart_data": recent_cart_data,
			"shipped" : shipped,
			"shipped_data" : shipped_data,
			"paid":paid,
			"paid_data": paid_data
		}
		return data
		
	def by_weeks_range(self, weeks_ago=7, number_of_weeks=2):
		if number_of_weeks > weeks_ago:
			number_of_weeks = weeks_ago
		days_ago_start = weeks_ago * 7
		days_ago_end = days_ago_start - (number_of_weeks * 7)
		# print(days_ago_start, days_ago_end)

		start_date = timezone.now() - datetime.timedelta(days=days_ago_start)
		end_date = timezone.now() - datetime.timedelta(days=days_ago_end)
		# print(start_date, end_date)
		return self.by_range(start_date=start_date, end_date=end_date)



	def by_range(self, start_date, end_date=None):
		if end_date is None:
			return self.filter(updated__gte=start_date)
		return self.filter(updated__gte=start_date).filter(updated__lt=end_date)

	def by_date(self):
		now = timezone.now() - datetime.timedelta(days=1)
		return self.filter(updated__day__gte=now.day)



	def totals_data(self):
		return self.aggregate(Sum("total"), Avg("total"))



	def cart_data(self):
		return self.aggregate(
					Sum("cart__products__price"),
					Avg("cart__products__price"),
					Count("cart__products")
			)


	def by_status(self, status="shipped"):
		return self.filter(status=status)


	def not_refunded(self):
		return self.exclude(status="refunded")

	def by_request(self, request):
		payement_livraison, created = PayementLivraison.objects.new_or_get(request)
		return self.filter(payement_livraison=payement_livraison)



	def not_created(self):
		return self.exclude(status="created")

class OrderPayementLivraisonManager(models.Manager):

	def get_queryset(self):
		return OrderPayementLivraisonManagerQuerySet(self.model, using=self._db)



	def by_request(self, request):
		return self.get_queryset().by_request(request)


	def new_or_get(self, payement_livraison, cart_obj):
		created = False
		qs	= self.get_queryset().filter(
				payement_livraison=payement_livraison,
				cart=cart_obj,
				active=True, status="created")
		if qs.count() == 1:
			obj = qs.first()

		else:
			obj = self.model.objects.create(
						payement_livraison=payement_livraison,
						cart=cart_obj
						)
			created = True

		return obj, created


class OrderPayementLivraison(models.Model):

	STATUS_CREATED = "created"
	STATUS_PAID = "paid"
	STATUS_SHIPPED = "shipped"
	STATUS_REFUNDED = "refunded"


	ORDER_PAYEMENT_LIVRAISON_STATUS_CHOICES = (

		(STATUS_CREATED, "Created"),
		(STATUS_PAID, "Paid"),
		(STATUS_SHIPPED, "Shipped"),
		(STATUS_REFUNDED, "Refunded"),

	)

	payement_livraison 				= models.ForeignKey(PayementLivraison,  null=True, blank=True, on_delete=models.CASCADE)
	order_payement_livraison_id		= models.CharField(max_length=120, blank=True) # Maybe AB18DE#
	livraison_address 				= models.ForeignKey(AddressPayementLivraison, related_name="livraison_address", null =True, blank=True, on_delete=models.CASCADE)
	facturation_address				= models.ForeignKey(AddressPayementLivraison, related_name="facturation_address", null=True, blank=True, on_delete=models.CASCADE) 
	cart 							= models.ForeignKey(Cart, on_delete=models.CASCADE)
	status  						= models.CharField(max_length=250, default="created", choices=ORDER_PAYEMENT_LIVRAISON_STATUS_CHOICES)
	shipping_total					= models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
	total							= models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
	active							= models.BooleanField(default=True)
	updated 						= models.DateTimeField(auto_now=True)
	timestamp 						= models.DateTimeField(auto_now_add=True)
	order_payement_livraison_pdf	= models.FileField(upload_to="order_p_l_pdfs", null=True, blank=True)




	objects	= OrderPayementLivraisonManager()

	class Meta:
		ordering = ["-timestamp", "-updated"]
		verbose_name = "Commande avec payement à la livraison"
		verbose_name_plural = "Commandes de payements à la livraison"


	def get_absolute_url(self):
		return reverse("orders:detail", kwargs={"order_payement_livraison_id": self.order_payement_livraison_id})



	def get_status(self):
		if self.status == "shipped":
			return "Shipped"

		elif self.status == "refunded":
			return "Refunded order"

		return "Shipped soon"


	def __str__(self):
		return self.order_payement_livraison_id



	def update_total(self):
		cart_total = self.cart.total
		shipping_total = self.shipping_total
		new_total = fsum([cart_total, shipping_total])
		formatted_total = format(new_total, ".2f")
		self.total = formatted_total
		self.save()
		return new_total


	def check_done(self):
		payement_livraison 	= self.payement_livraison
		facturation_address		= self.facturation_address

		total = self.total


		if payement_livraison and facturation_address and total > 0:
			return True

		return False


	def update_purshases(self):
		for item in self.cart.items.all():
			obj, created  = ProductPurshasePayementLivraison.objects.get_or_create(
				order_payement_livraison_id = self.order_payement_livraison_id,
				cart_item=item,
				payement_livraison=self.payement_livraison
				)

		return ProductPurshasePayementLivraison.objects.filter(order_payement_livraison_id=self.order_payement_livraison_id).count()


	def mark_paid(self):
		if self.status != "paid":
			if self.check_done():
				self.status = "paid"
				self.save()
				self.update_purshases()
		return self.status




def pre_save_create_order_payement_livraison_id(sender, instance, *args, **kwargs):
	if not instance.order_payement_livraison_id:
		instance.order_payement_livraison_id = unique_order_payement_livraison_id_generator(instance)

	qs	= OrderPayementLivraison.objects.filter(cart=instance.cart).exclude(payement_livraison=instance.payement_livraison)
	if qs.exists():
		qs.update(active=False)





pre_save.connect(pre_save_create_order_payement_livraison_id,sender=OrderPayementLivraison)



def post_save_cart_total_payement_livraison(sender, instance, created, *args, **kwargs):
	if not created:
		cart_obj = instance
		cart_total = cart_obj.total
		cart_id = cart_obj.id 
		qs = OrderPayementLivraison.objects.filter(cart__id=cart_id)
		if qs.count() == 1:
			order_obj = qs.first()
			order_obj.update_total()



post_save.connect(post_save_cart_total_payement_livraison, sender=Cart)



def post_save_order_payment_livraison(sender, instance, created, *args, **kwargs):
	if created:
		instance.update_total()



post_save.connect(post_save_order_payment_livraison, sender=OrderPayementLivraison)






class ProductPurshasePayementLivraisonQuerySet(models.query.QuerySet):

	def active(self):
		return self.filter(refunded=False)


	def by_request(self, request):
		payement_livraison, created = PayementLivraison.objects.new_or_get(request)
		return self.filter(payement_livraison=payement_livraison)



class ProductPurshasePayementLivraisonManager(models.Manager):

	def get_queryset(self):
		return ProductPurshasePayementLivraisonQuerySet(self.model, using=self._db)

	def all(self):
		return self.get_queryset().active()


	def by_request(self, request):
		return self.get_queryset().by_request(request)


	def products_by_id(self, request):
		qs = self.by_request(request)#.digital()
		ids_ = [x.product.id for x in qs]
		return ids_



	def products_by_request(self, request):
		ids_ = self.products_by_id(request)
		product_qs  = Product.objects.filter(id__in=ids_).distinct()
		return product_qs

class ProductPurshasePayementLivraison(models.Model): #Purshase veut dire achat
	order_payement_livraison_id		= models.CharField(max_length=120)
	payement_livraison 				= models.ForeignKey(PayementLivraison,on_delete=models.CASCADE)
	cart_item 						= models.ForeignKey(CartItem, on_delete=models.CASCADE)
	refunded 						= models.BooleanField(default=False)
	updated 						= models.DateTimeField(auto_now=True)
	timestamp 						= models.DateTimeField(auto_now_add=True)


	objects = ProductPurshasePayementLivraisonManager()


	class Meta:
		ordering = ["-timestamp", "-updated"]
		verbose_name = "Produit payé à la livraison"
		verbose_name_plural = "Produits payés à la livraison"

	def __str__(self):
		return ("On a {cart_item}".format(cart_item=self.cart_item))