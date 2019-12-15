
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
from utils.taxes import calcule_taxe






class PrototypeAbstract(models.Model):
	class Meta:
		abstract = True
	name 				= models.CharField(max_length=250)
	description 		= models.TextField()
	price 				= models.DecimalField(max_digits=40, decimal_places=2)
	promotion 			= models.DecimalField(max_digits=40, decimal_places=2)
	taux_taxe			= models.PositiveIntegerField(default=0)
	taxe 				= models.DecimalField(default=0.00, max_digits=100, decimal_places =2 )
	subtotal 			= models.DecimalField(default=0.00, max_digits=100, decimal_places =2 )
	stock 				= models.PositiveIntegerField()
	featured			= models.BooleanField(default=False)
	special 			= models.BooleanField(default=False)
	solde 				= models.BooleanField(default=False)
	pourcentage			= models.PositiveIntegerField(default=0)
	active 				= models.BooleanField(default=True)
	image 				= models.FileField(upload_to=upload_file_location)
	timestamp 			= models.DateTimeField(auto_now_add=True,)
	updated 			= models.DateTimeField(auto_now=True)
	marque 				= models.CharField(max_length=250)
	product_model 		= models.CharField(max_length=250)


class ProductQuerySet(models.query.QuerySet):
	def active(self):
		return self.filter(active=True)
	def featured(self):
		return self.filter(featured=True)

	def special_products(self):
		return self.filter(
			Q(solde=True) &
			Q(special=True) &
			Q(pourcentage__gte=50)
			)

	def good_deal(self):
		return self.filter(
			Q(solde=True) &
			Q(pourcentage__lt=40) &
			Q(pourcentage__gt=0)
			)

	def today_deal(self):
		return self.filter(
			Q(solde=True) &
			Q(pourcentage__lt=50) &
			Q(pourcentage__gte=40)
			)


	def best_seller(self):
		return self.filter(seller_count__gte=3)


	def get_men_clothings(self):
		return self.filter(product_type=Product.MEN_CLOTHING)




	def get_women_clothings(self):
		return self.filter(product_type=Product.WOMEN_CLOTHING)




	def get_pantalons(self):
		return self.filter(product_type=Product.PANTALON)




	def get_culottes(self):
		return self.filter(product_type=Product.CULOTTE)




	def get_jupes(self):
		return self.filter(product_type=Product.JUPE)




	def get_clothing_accessoires(self):
		return self.filter(product_type=Product.CLOTHING_ACCESSOIRE)




	def get_men_shoes(self):
		return self.filter(product_type=Product.MEN_SHOE)




	def get_women_shoes(self):
		return self.filter(product_type=Product.WOMEN_SHOE)






	def get_phones(self):
		return self.filter(product_type=Product.PHONE)






	def get_tablettes(self):
		return self.filter(product_type=Product.TABLETE)






	def get_phone_accessoires(self):
		return self.filter(product_type=Product.PHONE_ACCESSOIRE)






	def get_computers(self):
		return self.filter(product_type=Product.COMPUTER)






	def get_computer_accessoires(self):
		return self.filter(product_type=Product.COMPUTER_ACCESSOIRE)






	def search(self, query):
		lookups =( 
				 Q(name__icontains=query)|
				 Q(slug__icontains=query)|
				 Q(description__icontains=query)|
				 Q(price__icontains=query)|
				 Q(tag__title__icontains=query)
				)
		return self.filter(lookups)


	def marquelist(self, marque):

		lookups =( 
				 Q(name__icontains=marque)|
				 Q(slug__icontains=marque)|
				 Q(description__icontains=marque)|
				 Q(price__icontains=marque)|
				 Q(tag__title__icontains=marque)
				)
		return self.filter(lookups)







class ProductManager(models.Manager):

	def get_queryset(self):
		return ProductQuerySet(self.model, using=self._db).active().order_by("?")


	def all(self):
		return self.get_queryset().active()

	def special_products(self):
		return self.get_queryset().special_products()

	def good_deal(self):
		return self.get_queryset().good_deal()

	def today_deal(self):
		return self.get_queryset().today_deal()

	def best_seller(self):
		return self.get_queryset().best_seller()
			

	def featured(self):
		return self.get_queryset().featured()




	def get_men_clothings(self):
		return self.get_queryset().get_men_clothings()

		

	def get_women_clothings(self):
		return self.get_queryset().get_women_clothings()

		

	def get_pantalons(self):
		return self.get_queryset().get_pantalons()

		

	def get_culottes(self):
		return self.get_queryset().get_culottes()

		

	def get_jupes(self):
		return self.get_queryset().get_jupes()

		

	def get_clothing_accessoires(self):
		return self.get_queryset().get_clothing_accessoires()

		

	def get_men_shoes(self):
		return self.get_queryset().get_men_shoes()

		

	def get_women_shoes(self):
		return self.get_queryset().get_women_shoes()

		

	def get_phones(self):
		return self.get_queryset().get_phones()

		

	def get_tablettes(self):
		return self.get_queryset().get_tablettes()

		

	def get_phone_accessoires(self):
		return self.get_queryset().get_phone_accessoires()

		

	def get_computers(self):
		return self.get_queryset().get_computers()

		

		

	def get_computer_accessoires(self):
		return self.get_queryset().get_computer_accessoires()

		
		


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



	def search(self, query):
		return self.get_queryset().active().search(query)


	def marquelist(self, marque):
		return self.get_queryset().active().marquelist(marque)



class Product(PrototypeAbstract):
	MEN_CLOTHING 			= "men_clothing"
	WOMEN_CLOTHING 			= "women_clothing"
	CLOTHING_ACCESSOIRE 	= "clothing_accessoire"
	PANTALON 				= "pantalon"
	CULOTTE  				= "culotte"
	JUPE 					="jupe"

	MEN_SHOE 				= "men_shoe"
	WOMEN_SHOE 				= "women_shoe"

	PHONE 					= "phone"
	TABLETE 				= "tablette"
	PHONE_ACCESSOIRE 		= "phone_accessoire"

	COMPUTER 				= "computer"
	COMPUTER_ACCESSOIRE 	= "computer_accessoire"

	WATCH 					= "watch"
	VISUAL_AUDIO 			= "audio_viduel"





	TYPES_PRODUCTS = (

		(MEN_CLOTHING,"Vetements"),
		(WOMEN_CLOTHING,"Vetements"),
		(MEN_CLOTHING,"Vetements"),
		(CLOTHING_ACCESSOIRE,"Accessoires de Vetements"),
		(PANTALON,"Pantalon"),
		(CULOTTE,"Culotte"),
		(JUPE,"Jupe"),

		(MEN_SHOE,"Chaussure pour homme"),
		(WOMEN_SHOE,"Chaussure pour femme "),

		(PHONE,"Phone"),
		(TABLETE,"Tablette"),
		(PHONE_ACCESSOIRE,"Accessoire de phone"),


		(COMPUTER,"Ordinateur"),
		(COMPUTER_ACCESSOIRE,"Accessoire pour Ordinateur"),

		(WATCH,"Montre"),
		(VISUAL_AUDIO,"Audio Visuel"),

		)
	slug 				= models.SlugField(max_length=1000, blank=True )
	seller_count		= models.PositiveIntegerField(default=0)
	product_type = models.CharField(max_length=250, choices=TYPES_PRODUCTS)



	objects = ProductManager()






	def __str__(self):
		return "Produit :{name}, coute : {price}".format(name=self.name, price=self.price)


	class Meta:
		verbose_name = "Produit"
		verbose_name_plural ="Produits"




	def get_absolute_url(self):
		if self.product_type == self.MEN_CLOTHING:
			return reverse("products:men_clothing_detail", kwargs={ "pk": self.pk, "slug": self.slug})

		if self.product_type == self.WOMEN_CLOTHING:
			return reverse("products:women_clothing_detail", kwargs={ "pk": self.pk, "slug": self.slug})

		elif self.product_type == self.CLOTHING_ACCESSOIRE:
			return reverse("products:accessoire_clothing_detail", kwargs={ "pk": self.pk, "slug": self.slug})

		elif self.product_type == self.PANTALON:
			return reverse("products:patalon_detail", kwargs={ "pk": self.pk, "slug": self.slug})

		elif self.product_type == self.CULOTTE:
			return reverse("products:culotte_detail", kwargs={ "pk": self.pk, "slug": self.slug})

		elif self.product_type == self.JUPE:
			return reverse("products:jupe_detail", kwargs={ "pk": self.pk, "slug": self.slug})

		elif self.product_type == self.MEN_SHOE:
			return reverse("products:men_shoe_detail", kwargs={ "pk": self.pk, "slug": self.slug})

		elif self.product_type == self.WOMEN_SHOE:
			return reverse("products:women_shoe_detail", kwargs={ "pk": self.pk, "slug": self.slug})

		elif self.product_type == self.PHONE:
			return reverse("products:phone_detail", kwargs={ "pk": self.pk, "slug": self.slug})

		elif self.product_type == self.PHONE_ACCESSOIRE:
			return reverse("products:accessoire_phone_detail", kwargs={ "pk": self.pk, "slug": self.slug})

		elif self.product_type == self.TABLETE:
			return reverse("products:tablette_detail", kwargs={ "pk": self.pk, "slug": self.slug})


		elif self.product_type == self.COMPUTER:
			return reverse("products:computer_detail", kwargs={ "pk": self.pk, "slug": self.slug})

		elif self.product_type == self.COMPUTER_ACCESSOIRE:
			return reverse("products:accessoire_computer_detail", kwargs={ "pk": self.pk, "slug": self.slug})







def product_pre_save_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)





pre_save.connect(product_pre_save_receiver, sender=Product)


