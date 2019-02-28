

from django.db import models


#Locales import 
from utils.files_utils import upload_file_location


from .products import Product 




class PhoneAbstractModel(models.Model):
	class Meta:
		abstract = True
	WHITE_COLOR = "white"
	RED_COLOR = "red"
	BLUE_COLOR = "blue" 
	GOLD_COLOR = "gold"
	BLACK_COLOR = "black" 
	GREEN_COLOR = "green" 
	YELLOW_COLOR = "yellow"

	COLOR_CHOICES = (
		(WHITE_COLOR, "White"),
		(RED_COLOR, "Red"),
		(BLUE_COLOR, "Blue"),
		(GOLD_COLOR, "Gold"),
		(BLACK_COLOR, "Black"),
		(GREEN_COLOR, "Green"),
		(YELLOW_COLOR, "Yellow"),


		)


	taile_ecran 		 = models.CharField(max_length=1000)
	memoire    			 = models.CharField(max_length=1000)
	appareil_photo 		 = models.CharField(max_length=1000)
	systeme_exploitation = models.CharField(max_length=1000)
	processeur 			 = models.CharField(max_length=1000)
	batterie 	 		 = models.CharField(max_length=1000)

	couleur 			 = models.CharField(max_length=250, choices=COLOR_CHOICES)

	image_face 			 = models.FileField(upload_to=upload_file_location)
	image_dos 		 	 = models.FileField(upload_to=upload_file_location)
	image_haut 			 = models.FileField(upload_to=upload_file_location)
	image_bas 			 = models.FileField(upload_to=upload_file_location)
	image_gauche 		 = models.FileField(upload_to=upload_file_location)
	image_droite 		 = models.FileField(upload_to=upload_file_location)





class Phone(Product, PhoneAbstractModel):

	TYPE_SAMSUNG = "iphone"
	TYPE_IPHONE = "iphone"
	TYPE_HUAWEI = "iphone"
	TYPE_OPPO = "iphone"
	TYPE_XIOMI = "iphone"
	TYPE_TECNO = "iphone"
	TYPE_ITEL = "iphone"
	TYPE_HTC = "iphone"



	TYPE_PHONE = (

		(TYPE_SAMSUNG, "Téléphone samsung"),
		(TYPE_IPHONE, "Iphone"),
		(TYPE_HUAWEI, "Téléphone Huawei"),
		(TYPE_OPPO, "Téléphone oppo"),
		(TYPE_XIOMI, "Téléphone xiomi"),
		(TYPE_TECNO, "Téléphone tecno"),
		(TYPE_ITEL, "Téléphone itel"),
		(TYPE_HTC, "Téléphone HTC"),

		)

	phone_type = models.CharField(max_length=250, choices=TYPE_PHONE)

	def get_absolute_url(self):
		return reverse("products:phone_detail", kwargs={ "pk": self.pk, "slug": self.slug})



class Tablette(Product, PhoneAbstractModel):
	TYPE_IPAD = "ipad"
	TYPE_TABLETTE = "tablette"
	TABLETE_TYPE = (
		(TYPE_IPAD, "IPad"),
		(TYPE_TABLETTE, "Tablette"),
		)

	tablette_type = models.CharField(max_length=250, choices=TABLETE_TYPE)



	def get_absolute_url(self):
		return reverse("products:tablette_detail", kwargs={ "pk": self.pk, "slug": self.slug})





class AccessoirePhone(Product):
	ACCESSOIRE_CHARGEUR = "chargeur"
	ACCESSOIRE_ECOUTEURS = "ecouteurs"
	ACCESSOIRE_ECRAN = "ecran"
	ACCESSOIRE_BATTERIE = "batterie"
	ACCESSOIRE_POCHETTE = "pochette"
	ACCESSOIRE_ANTI_CASSE = "anticasse"


	TYPE_ACCESSOIRE = (
		(ACCESSOIRE_ECOUTEURS, "Ecouteurs"),
		(ACCESSOIRE_CHARGEUR, "Chargeur"),
		(ACCESSOIRE_POCHETTE, "Pochette"),
		(ACCESSOIRE_ANTI_CASSE, "Anti casse"),
		(ACCESSOIRE_ECRAN, "Ecran"),
		(ACCESSOIRE_BATTERIE, "Batterie"),

		)

	accessoire_type = models.CharField(max_length=250, choices=TYPE_ACCESSOIRE)

	caracteristique = models.TextField()

	def get_absolute_url(self):
		return reverse("products:accessoire_phone_detail", kwargs={ "pk": self.pk, "slug": self.slug})





