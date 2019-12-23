from django.db import models
from django.contrib.postgres.fields import JSONField
from django.urls import reverse


#Locales import 
from utils.files_utils import upload_file_location

from .products import Product, PrototypeAbstract


class ClothingAbstractModel(PrototypeAbstract):
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


	GENRE_MEN = "hommes"
	GENRE_WOMEN = "femmes"
	GENRE_MIX   = "mix"

	GENRE_CHOICE = (

		(GENRE_MEN, "Hommes"),
		(GENRE_WOMEN, "Femmes"),
		(GENRE_MIX, "Mix"),

		)


	MANCHE_COURTE = "courte"
	MANCHE_LONGUE = "longue"

	MANCHE_CHOICE = (
		(MANCHE_COURTE, "Courte"),
		(MANCHE_LONGUE, "Longue"),

		)

	TAILLE_S = "s"
	TAILLE_M = "m"
	TAILLE_L = "l"
	TAILLE_XL = "xl"
	TAILLE_XXL = "xxl"

	TAILLE_CHOICE = (

		(TAILLE_S, "S"),
		(TAILLE_M, "M"),
		(TAILLE_L, "L"),
		(TAILLE_XL, "XL"),
		(TAILLE_XXL, "XXL"),
		)

	AGE_12 = "moins12"
	AGE_20 = "moins20"
	AGE_40 = "moins40"
	AGE_P40 = "plus40"
	AGE_ALL = "allage"

	TRANCHE_AGE = (

		(AGE_ALL, "Pour tous les âges"),
		(AGE_40, "Moins de 40 ans"),
		(AGE_20, "Moins de 20 ans"),
		(AGE_P40, "Plus de 40 ans"),
		(AGE_12, "Moins de 12 ans"),

		)




	image_derriere 	= models.FileField(upload_to=upload_file_location)
	image_devant 	= models.FileField(upload_to=upload_file_location)
	couleur 		= models.CharField(max_length=250, choices=COLOR_CHOICES)
	taille 			= models.CharField(max_length=250, choices=TAILLE_CHOICE)
	genre 			= models.CharField(max_length=250, choices=GENRE_CHOICE)
	manche 			= models.CharField(max_length=250, choices=MANCHE_CHOICE)
	tranche 		= models.CharField(max_length=250, choices=TRANCHE_AGE)



class MenClothing(ClothingAbstractModel):

	CLOTHING_SHIRT = "shirt"
	CLOTHING_TSHIRT = "tshirt"
	CLOTHING_JACKET = "jacket"
	CLOTHING_BLUSON = "bluson"
	CLOTHING_PULL = "pull"
	CLOTHING_POLO = "polo"
	CLOTHING_MAILLOT = "maillot"
	CLOTHING_GILET = "gilet"





	TYPE_CLOTHINGS_CHOICES = (

		(CLOTHING_SHIRT, "Chemise"),
		(CLOTHING_TSHIRT, "T-Shirt"),
		(CLOTHING_JACKET, "Jacket"),
		(CLOTHING_BLUSON, "Blouson"),
		(CLOTHING_PULL, "Pulls"),
		(CLOTHING_POLO, "Polo"),
		(CLOTHING_MAILLOT, "Maillot"),
		(CLOTHING_GILET, "Gilet"),

		)

	clothing_type = models.CharField(max_length=250, choices=TYPE_CLOTHINGS_CHOICES)
	product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="men_clothings")

	def __str__(self):
		return self.name


	class Meta:
		verbose_name ="Vêtement hommes"
		verbose_name_plural = "Vêtement hommes "





class WomenClothing(ClothingAbstractModel):

	CLOTHING_SHIRT = "shirt"
	CLOTHING_TSHIRT = "tshirt"
	CLOTHING_JACKET = "jacket"
	CLOTHING_BLUSON = "bluson"
	CLOTHING_PULL = "pull"
	CLOTHING_POLO = "polo"
	CLOTHING_MAILLOT = "maillot"
	CLOTHING_GILET = "gilet"
	CLOTHING_ROBE = "robe"
	CLOTHING_PYJAMA = "pyjama"
	CLOTHING_TUNIQUE = "tunique"
	CLOTHING_CHEMISIER = "chemisier"
	CLOTHING_SALOPETTE = "salopette"






	TYPE_CLOTHINGS_CHOICES = (

		(CLOTHING_SHIRT, "Chemise"),
		(CLOTHING_TSHIRT, "T-Shirt"),
		(CLOTHING_JACKET, "Jacket"),
		(CLOTHING_BLUSON, "Bluson"),
		(CLOTHING_PULL, "Pulls"),
		(CLOTHING_POLO, "Polo"),
		(CLOTHING_MAILLOT, "Maillot"),
		(CLOTHING_GILET, "Gilet"),
		(CLOTHING_ROBE, "Robe"),
		(CLOTHING_PYJAMA, "Pyjama"),
		(CLOTHING_TUNIQUE, "Tunique"),
		(CLOTHING_CHEMISIER, "Chemisier"),
		(CLOTHING_SALOPETTE, "Salopette"),



		)

	clothing_type = models.CharField(max_length=250, choices=TYPE_CLOTHINGS_CHOICES)
	product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="women_clothings")

	def __str__(self):
		return self.name



	class Meta:
		verbose_name = "Vêtement femmes"
		verbose_name_plural = "Vêtements femmes"




#Pants


class PantsAbstractModel(ClothingAbstractModel):
	class Meta:
		abstract = True


	taille 			= None
	numero          = models.CharField(max_length=250)
	manche 			= None


class Pantalon(PantsAbstractModel):
	PANTALON_JEANS ="jeans"
	PANTALON_CHINO ="chino"
	PANTALON_TISSU ="tissu"
	PANTALON_JOGGING ="jggin"
	PANTALON_NILON ="nilon"
	PANTALON_MINI ="mini"


	PANTALON_TYPE_CHOICES = (

		(PANTALON_JEANS, "Pantalon Jeans"),
		(PANTALON_JOGGING, "Pantalon Jogging"),
		(PANTALON_CHINO, "Pantalon Chino"),
		(PANTALON_TISSU, "Pantalon Tissu "),
		(PANTALON_NILON, "Pantalon en nilon"),
		(PANTALON_MINI, "Pantalon en mini"),



		)

	pantalon_type = models.CharField(max_length=250, choices=PANTALON_TYPE_CHOICES)
	product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="pantalons")

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Pantalon"
		verbose_name_plural = "Pantalons"




class Culotte(PantsAbstractModel):
	CULOTTE_JEANS ="jeans"
	CULOTTE_CHINO ="chino"
	CULOTTE_TISSU ="tissu"
	CULOTTE_JOGGING ="jggin"
	CULOTTE_NILON ="nilon"

	CULOTTE_TYPE_CHOICES = (

		(CULOTTE_JEANS, "Culotte Jeans"),
		(CULOTTE_JOGGING, "Culotte Jogging"),
		(CULOTTE_CHINO, "Culotte Chino"),
		(CULOTTE_TISSU, "Culotte Tissu "),
		(CULOTTE_NILON, "Culotte en nilon"),


		)

	culotte_type = models.CharField(max_length=250, choices=CULOTTE_TYPE_CHOICES)
	product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="culottes")

	def __str__(self):
		return self.name



	class Meta:
		verbose_name = "Culotte"
		verbose_name_plural = "Culottes"







class Jupe(ClothingAbstractModel):

	TAILLE_MOYENNE ="moyenne"
	TAILLE_COURTE ="courte"
	TAILLE_LONGUE ="longue"

	TAILLE_CHOICE = (
		(TAILLE_MOYENNE, "Taille moyenne"),
		(TAILLE_COURTE, "Taille courte"),
		(TAILLE_LONGUE, "Taille longue"),


		)
	taille 			= models.CharField(max_length=250, choices=TAILLE_CHOICE)
	genre 			= None
	manche 			= None

	product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="jupes")


	def __str__(self):
		return self.name


	class Meta:
		verbose_name = "Jupe"
		verbose_name_plural = "Jupes"




#Shoes


class ShoesAbstractModel(ClothingAbstractModel):
	class Meta:
		abstract = True

	
	image_haut 		= models.FileField(upload_to=upload_file_location, null=True, blank=True)
	image_dos 		= models.FileField(upload_to=upload_file_location, null=True, blank=True)
	image_gauche 	= models.FileField(upload_to=upload_file_location, null=True, blank=True)
	image_droite 	= models.FileField(upload_to=upload_file_location, null=True, blank=True)
	image_derriere 	= models.FileField(upload_to=upload_file_location, null=True, blank=True)
	image_devant 	= models.FileField(upload_to=upload_file_location, null=True, blank=True)

	taille 			= None
	numero 			= models.CharField(max_length=250)
	manche 			= None


class MenShoes(ShoesAbstractModel):
	SHOES_BASKET = "basket"
	SHOES_REPOSE_PIED = "reposepied"
	SHOES_SOULIER = "soulier"
	SHOES_SANDALE = "sandale"
	SHOES_TENIS = "tenis"
	SHOES_MOCASSIN = "mocassin"
	SHOES_ESPADRILLE = "espadrille"
	SHOES_RUNNING = "running"
	SHOES_MAX = "max"


	SHOES_TYPE = (
		(SHOES_BASKET, "Basket"),
		(SHOES_REPOSE_PIED, "Repose pied"),
		(SHOES_SOULIER, "Soulier"),
		(SHOES_SANDALE, "Sandale"),
		(SHOES_TENIS, "Tenis"),
		(SHOES_MOCASSIN, "Mocassin"),
		(SHOES_ESPADRILLE, "Espadrille"),
		(SHOES_RUNNING, "Running"),
		(SHOES_MAX, "Chaussure max grande taille"),
		)
	shoes_type      = models.CharField(max_length=250, choices=SHOES_TYPE)
	product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="men_shoes")


	def __str__(self):
		return self.name



	class Meta:
		verbose_name = "Chaussure hommes"
		verbose_name_plural = "Chaussures hommes"









class WomenShoes(ShoesAbstractModel):
	SHOES_TALON  = "talon"
	SHOES_BASKET = "basket"
	SHOES_REPOSE_PIED = "reposepied"
	SHOES_SOULIER = "soulier"
	SHOES_SANDALE = "sandale"
	SHOES_TENIS = "tenis"
	SHOES_ESPADRILLE = "espadrille"
	SHOES_RUNNING = "running"
	SHOES_MAX = "max"


	SHOES_TYPE = (
		(SHOES_TALON, "Talon"),
		(SHOES_BASKET, "Basket"),
		(SHOES_REPOSE_PIED, "Repose pied"),
		(SHOES_SOULIER, "Soulier"),
		(SHOES_SANDALE, "Sandale"),
		(SHOES_TENIS, "Tenis"),
		(SHOES_ESPADRILLE, "Espadrille"),
		(SHOES_RUNNING, "Running"),
		(SHOES_MAX, "Chaussure max grande taille"),
		)
	
	shoes_type      = models.CharField(max_length=250, choices=SHOES_TYPE)

	product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="women_shoes")

	def __str__(self):
		return self.name


	class Meta:
		verbose_name ="Chaussure femmes"
		verbose_name_plural = "Chaussures femmes"




class AccessoireClothng(PrototypeAbstract):
	ACCESSOIRE_CEINTEUR = "ceinture"
	ACCESSOIRE_LUNETTE = "lunette"
	ACCESSOIRE_KEPI = "kepi"
	ACCESSOIRE_FOULAR = "foular"
	ACCESSOIRE_CHAUSSETTE = "chausette"
	ACCESSOIRE_CRAVATE = "cravate"
	ACCESSOIRE_ECHARPE = "echarpe"

	TYPE_ACCESSOIRES = (
		(ACCESSOIRE_CEINTEUR, "Ceinteure"),
		(ACCESSOIRE_LUNETTE, "Lunette"),
		(ACCESSOIRE_KEPI, "Képi"),
		(ACCESSOIRE_FOULAR, "Foular"),
		(ACCESSOIRE_CHAUSSETTE, "Chaussette"),
		(ACCESSOIRE_CRAVATE, "Cravate"),
		(ACCESSOIRE_ECHARPE, "Echarpe"),
		)

	GENRE_MEN = "hommes"
	GENRE_WOMEN = "femmes"
	GENRE_MIX   = "mix"

	GENRE_CHOICE = (

		(GENRE_MEN, "Pour homme"),
		(GENRE_WOMEN, "Pour homme"),
		(GENRE_MIX, "Pour tous le monde"),

		)



	accessoire_type  	= models.CharField(max_length=250, choices=TYPE_ACCESSOIRES)
	genre 				= models.CharField(max_length=250, choices=GENRE_CHOICE, default=GENRE_MIX)
	caracteristque 		= models.TextField()
	product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="accessoire_clothings")


	def __str__(self):
		return self.name


	class Meta:
		verbose_name ="Accessoire vêtements"
		verbose_name_plural = "Accessoires vêtements"





