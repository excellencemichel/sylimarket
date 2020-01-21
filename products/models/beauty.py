from django.db import models

#Locales import 
from utils.files_utils import upload_file_location


from .products import Product, PrototypeAbstract


class Beauty(PrototypeAbstract):

	TYPE_PARFUM = "parfum"
	TYPE_SAVON = "savon"
	TYPE_GEL = "gel"
	TYPE_SHAMPOING = "shampoing"
	TYPE_HUILE = "huile"
	TYPE_VITAMINE = "vitamine"
	TYPE_SOIN = "soins"




	TYPE_BEAUTY = (

		(TYPE_PARFUM, "Le parfum"),
		(TYPE_SAVON, "Le savon"),
		(TYPE_GEL, "Le gel"),
		(TYPE_SHAMPOING, "Savon shampoing"),
		(TYPE_HUILE, "Huile crème"),
		(TYPE_VITAMINE, "Vitamine"),
		(TYPE_SOIN, "Produits de soins"),

		)

	beauty_type = models.CharField(max_length=250, choices=TYPE_BEAUTY)
	product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="beauty")

	def __str__(self):
		return self.name


	class Meta:
		verbose_name = "Produit de beauté"
		verbose_name_plural ="Produits de beauté"