from django.db import models

#Locales import 
from utils.files_utils import upload_file_location


from .products import Product, PrototypeAbstract


class Health(PrototypeAbstract):

	TYPE_ALIMENT = "aliment"
	TYPE_VITAMINE = "vitamine"
	TYPE_SOIN = "soins"
	TYPE_PHARMACEUTIQUE = "pharmaeutique"
	TYPE_PARAPHARMACEUTIQUE = "parapharmaeutique"






	TYPE_HEALTH = (

		(TYPE_ALIMENT, "Aliment"),
		(TYPE_VITAMINE, "Vitamine"),
		(TYPE_SOIN, "Pour les soins"),
		(TYPE_PHARMACEUTIQUE, "Phamaceutique"),
		(TYPE_PARAPHARMACEUTIQUE, "Paraphamaceutique"),


		)

	health_type = models.CharField(max_length=250, choices=TYPE_HEALTH)
	product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="health")

	def __str__(self):
		return self.name


	class Meta:
		verbose_name = "Produit de santé"
		verbose_name_plural ="Produits de santé"