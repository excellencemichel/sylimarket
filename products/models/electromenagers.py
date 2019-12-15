

from django.db import models


#Locales import 
from utils.files_utils import upload_file_location


from .products import Product, PrototypeAbstract







class Electromenager(PrototypeAbstract):
	MIXEUR = "mixeur"
	BATTEUR = "batteur"
	MACHINEALAVER = "machinealaver"
	RECHAUD = "rechaud"



	TYPE_MACHINE = (
		(MIXEUR, "Mixeur"),
		(BATTEUR, "Batteur"),
		(MACHINEALAVER, "Machine à laver"),
		(RECHAUD, "Rechaud"),

		)

	type_machine = models.CharField(max_length=250, choices=TYPE_MACHINE)

	caracteristique = models.TextField()
	product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="electromenager")


	def __str__(self):
		return self.name


	class Meta:
		verbose_name = "Electromenager"
		verbose_name_plural ="Electromenagers"





