from django.db import models


from django.db.models.signals import pre_save, post_save

from django.urls import reverse

from utils.generator_utils import unique_slug_generator_with_tilte
from products.models import Product
# Create your models here.




class Tag(models.Model):
	title 				= models.CharField(max_length=250)
	slug 				= models.SlugField()
	tag_text			= models.CharField(max_length=250)
	tag_product_type 	= models.CharField(max_length=250)
	timestamp			= models.DateTimeField(auto_now_add=True)
	active 				= models.BooleanField(default=True)
	products			= models.ManyToManyField(Product, blank=True)



	def __str__(self):
		return str(self.title)























def tag_pre_save_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = unique_slug_generator_with_tilte(instance)



pre_save.connect(tag_pre_save_receiver, sender=Tag)