from django.db import models
from utils.files_utils import upload_file_location_slide


# Create your models here.



class SlideManager(models.Manager):
	def active(self):
		print(self.filter(active=True).order_by("?"))
		return self.filter(active=True).order_by("?")



class Slide(models.Model):
	titre 		= models.CharField(max_length=1000, null=True, blank=True)
	annonce		= models.CharField(max_length=1000, null=True, blank=True)
	image 		= models.FileField(upload_to=upload_file_location_slide)
	active 				= models.BooleanField(default=True)
	timestamp 			= models.DateTimeField(auto_now_add=True,)
	updated 			= models.DateTimeField(auto_now=True)


	objects = SlideManager()





	def __str__(self):
		return f"Slide sur {self.titre} portant l'annonce {self.annonce}"


