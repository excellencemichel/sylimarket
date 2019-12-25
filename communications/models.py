from django.db import models
from utils.files_utils import upload_file_location_slide, upload_file_banniere


# Create your models here.



class SlideManager(models.Manager):
	def active(self):
		return self.filter(active=True).order_by("?")



class Slide(models.Model):
	titre 		= models.CharField(max_length=1000, null=True, blank=True)
	annonce		= models.CharField(max_length=1000, null=True, blank=True)
	image 		= models.FileField(upload_to=upload_file_location_slide)
	active 				= models.BooleanField(default=True)
	timestamp 			= models.DateTimeField(auto_now_add=True,)
	updated 			= models.DateTimeField(auto_now=True)


	objects = SlideManager()

	class Meta:
		verbose_name ="Slide"
		verbose_name_plural = "Slides"





	def __str__(self):
		return f"Slide sur {self.titre} portant l'annonce {self.annonce}"




class BaniereManager(models.Manager):
	def active(self):
		return self.filter(active=True).order_by("?")



class Baniere(models.Model):

	NIVEAU_UN = "niveau_un"
	NIVEAU_DEUX = "niveau_deux"
	NIVEAU_TROIS = "niveau_trois"
	NIVEAU_QUATRE = "niveau_quatre"

	NIVEAU_BANIERE = (
		(NIVEAU_UN, "Niveau un (1)"),
		(NIVEAU_DEUX, "Niveau deux (2)"),
		(NIVEAU_TROIS, "Niveau trois (3)"),
		(NIVEAU_QUATRE, "Niveau quatre (4)"),
		)

	annonce				= models.CharField(max_length=1000, null=True, blank=True)
	message				= models.CharField( max_length=1000, null=True, blank=True)
	lien				= models.URLField(max_length=1000, null=True, blank=True)
	niveau_baniere  	= models.CharField(max_length=250, choices=NIVEAU_BANIERE)
	image 				= models.FileField(upload_to=upload_file_banniere)
	active 				= models.BooleanField(default=True)
	timestamp 			= models.DateTimeField(auto_now_add=True,)
	updated 			= models.DateTimeField(auto_now=True)


	objects = BaniereManager()

	class Meta:
		verbose_name ="Bannière"
		verbose_name_plural = "Bannières"




	def __str__(self):
		return f"Banière de niveau {self.niveau_baniere} portant le message : {self.message}"


