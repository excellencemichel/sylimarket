from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType

from django.urls import reverse


from django.db import models
from django.db.models import Q
from django.db.models.signals import pre_save, post_save



#locales import
from utils.files_utils import upload_file_location
from utils.generator_utils import unique_slug_generator


class ProductQuerySet(models.query.QuerySet):
	def active(self):
		return self.filter(active=True)
	def featured(self):
		return self.filter(featured=True)


	def search(self, query):
		lookups =( 
				 Q(name__icontains=query)|
				 Q(slug__icontains=query)|
				 Q(description__icontains=query)|
				 Q(price__icontains=query)
				 # Q(tag__title__icontains=query)
				)
		return self.filter(lookups)






class ProductManager(models.Manager):

	def get_queryset(self):
		return ProductQuerySet(self.model, using=self._db)


	# def all(self):
	# 	return self.get_queryset().active()

	def featured(self):
		return self.get_queryset().featured()

	def get_by_id(self, id):

		qs = self.get_queryset().filter(id=id)
		if qs.count() ==1:
			return qs.first()

		return None


	def get_by_slug_id(self, slug, id):

		qs = self.get_queryset().filter(slug=slug, id=id)
		if qs.count() ==1:
			return qs.first()

		return None

		# return self.get_queryset().filter(id=id)


	def search(self, query):
		return self.get_queryset().active().search(query)



class Product(models.Model):
	name 				= models.CharField(max_length=250)
	slug 				= models.SlugField(max_length=1000, blank=True )
	description 		= models.TextField()
	price 				= models.DecimalField(max_digits=40, decimal_places=2)
	stock 				= models.PositiveIntegerField()
	featured			= models.BooleanField(default=False)
	active 				= models.BooleanField(default=True)
	image 				= models.FileField(upload_to=upload_file_location)
	timestamp 			= models.DateTimeField(auto_now_add=True,)
	updated 			= models.DateTimeField(auto_now=True)
	marque 				= models.CharField(max_length=250)
	product_model 		= models.CharField(max_length=250)

	
	cart_items = GenericRelation(
        'carts.CartItem',
        'product_object_id',
        'product_content_type_id',
        related_query_name='products',
    )

	objects = ProductManager()






	def __str__(self):
		return "Produit :{name}, coute : {price}".format(name=self.name, price=self.price)




	def get_absolute_url(self):
		return reverse("products:detail", kwargs={ "pk": self.pk, "slug": self.slug})





def product_pre_save_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)



post_save.connect(product_pre_save_receiver, sender=Product)