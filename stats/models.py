from django.db import models

# Create your models here.


class Statistique(models.Model):
	url 			= models.URLField()
	nb_visites  	= models.IntegerField(default=1)
	request_user 	= models.CharField(max_length=250, blank=True, null=True)
	request_user_ip = models.CharField(max_length=250, blank=True, null=True)

	def __str__(self):
		return self.url
