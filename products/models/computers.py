
from django.db import models
from django.contrib.postgres.fields import JSONField


#Locales import 
from utils.files_utils import upload_file_location

from .products import Product, PrototypeAbstract


class Computer(PrototypeAbstract):

	WHITE_COLOR  = "white"
	RED_COLOR    = "red"
	BLUE_COLOR   = "blue" 
	GOLD_COLOR   = "gold"
	BLACK_COLOR  = "black" 
	GREEN_COLOR  = "green" 
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

	COMPUTER_PC 			= "pc"
	COMPUTER_BUREAUTIQUE 	= "bureatique"

	TYPE_COMPUTER = (
			(COMPUTER_PC, "Ordinateur portable"),
			(COMPUTER_BUREAUTIQUE, "Ordinateur bureatique"),


		)

	couleur = models.CharField(max_length=250, choices=COLOR_CHOICES)
	computer_type 	= models.CharField(max_length=250, choices=TYPE_COMPUTER, default=COMPUTER_PC)

	computer_model 	 = models.CharField(max_length=250)

	image_ouvert = models.FileField(max_length=250, upload_to=upload_file_location)
	image_dos = models.FileField(max_length=250, upload_to=upload_file_location)
	image_haut = models.FileField(max_length=250, upload_to=upload_file_location)
	image_bas = models.FileField(max_length=250, upload_to=upload_file_location)
	image_gauche = models.FileField(max_length=250, upload_to=upload_file_location)
	image_droite = models.FileField(max_length=250, upload_to=upload_file_location)

	disque_dur  = models.CharField(max_length=250)
	processeur			 = models.CharField(max_length=250)
	memoire_ram 		   	 = models.CharField(max_length=100)
	affichage 		  	 = models.CharField(max_length=250)
	systeme_exploitation = models.CharField(max_length=250)
	connectivite	     = models.CharField(max_length=250)
	ports 			     = models.CharField(max_length=250)


	product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="computers")

	def __str__(self):
		return self.name


	class Meta:
		verbose_name = "Ordinateur"
		verbose_name_plural ="Ordinateurs"






class AccessoireComputer(PrototypeAbstract):
	ACCESSOIRE_DISQUE_DURE = "disquedur"
	ACCESSOIRE_CHARGEUR = "chargeur"
	ACCESSOIRE_MICRO = "micro"
	ACCESSOIRE_LOGCIEL = "logiciel"
	ACCESSOIRE_CLAVIER  ="clavier"
	ACCESSOIRE_ECRAN = "ecran"



	TYPE_ACCESSOIRE = (
		(ACCESSOIRE_DISQUE_DURE, "Disque dur"),
		(ACCESSOIRE_CHARGEUR, "Chargeur"),
		(ACCESSOIRE_MICRO, "Micro"),
		(ACCESSOIRE_LOGCIEL, "Logiciel"),
		(ACCESSOIRE_CLAVIER, "Clavier"),
		(ACCESSOIRE_ECRAN, "Ecran"),
		)

	accesoire_computer = models.CharField(max_length=250, choices=TYPE_ACCESSOIRE)
	caracteristque 	   = models.TextField()

	product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="accesoire_computers")

	def __str__(self):
		return self.name


	class Meta:
		verbose_name = "Accessoire ordinateur"
		verbose_name_plural ="Accessoires ordinateur"
