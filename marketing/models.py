from django.conf import settings

from django.db import models
from django.db.models.signals import pre_save, post_save

from .utils import Mailchimp 

# Create your models here.


class MarketingPreference(models.Model):
	user 		 			 = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	subscribed	 			 = models.BooleanField(default=True)
	mailchimp_subscribed	 = models.NullBooleanField(blank=True)
	mailchimp_msg 			 = models.TextField(null=True, blank=True)
	timestamp 	  			 = models.DateTimeField(auto_now_add=True)
	updated 	  			 = models.DateTimeField(auto_now = True)



	def __str__(self):
		return self.user.email




def make_marketing_pref_receiver(sender, instance, created, *args, **kwargs):
	"""
	User model
	"""
	print("Post AUTH_USER_MODEL save we're going to Mailchimp")
	if created:
		MarketingPreference.objects.get_or_create(user=instance)

post_save.connect(make_marketing_pref_receiver, sender=settings.AUTH_USER_MODEL)





def marketing_pref_update_receiver(sender, instance, *args, **kwargs):
	if instance.subscribed != instance.mailchimp_subscribed:

		if instance.subscribed:
			# suscrebing user
			status_code, response_data = Mailchimp().subscribe(instance.user.email)


		else:
			# unsubscribing user
			status_code, response_data = Mailchimp().unsubscribe(instance.user.email)

		if response_data["status"] == "subscribed":
			instance.subscribed = True
			instance.mailchimp_subscribed = True
			instance.mailchimp_msg = response_data

		else:
			instance.subscribed = False
			instance.mailchimp_subscribed = False
			instance.mailchimp_msg = response_data


pre_save.connect(marketing_pref_update_receiver, sender=MarketingPreference)





def marketing_pref_create_receiver(sender, instance, created, *args, **kwargs):
	if created:
		print("Add user to mailchimp")
		status_code, response_data = Mailchimp().subscribe(instance.user.email)
		# import pdb; pdb.set_trace()

post_save.connect(marketing_pref_create_receiver, sender=MarketingPreference)



def upload_product_file_loc(instance, filename):
	id_ = instance.id
	if id_ is None:
		Klass = instance.__class__
		qs = Klass.objects.all().order_by("-pk")
		if qs.exists():
			id_ = qs.first().id + 1
		else:
			id_ = 0
	location = "sliders_media/{id}/".format(id=id_)


	return location + filename #path/to/file/filename.mp4


class MarketingSliders(models.Model):
	name 			= models.CharField(max_length=250)
	slider 			= models.ImageField(max_length=250,
						upload_to=upload_product_file_loc
						)
	timestamp 	  	= models.DateTimeField(auto_now_add=True)
	updated 	  	= models.DateTimeField(auto_now = True)
