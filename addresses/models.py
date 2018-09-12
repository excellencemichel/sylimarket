from django.db import models

from django.utils.translation import ugettext_lazy as _

#Locale import
from billing.models import BillingProfile, PayementLivraison

# Create your models here.

ADDRESS_TYPES = (
	("billing", "Billing"),
	("shipping", "Shipping"),
	)


class Address(models.Model):
	billing_profile		= models.ForeignKey(BillingProfile, on_delete=models.CASCADE)
	address_type 		= models.CharField(max_length=120, choices=ADDRESS_TYPES)
	address_line_1		= models.CharField(max_length=250)
	address_line_2		= models.CharField(max_length=250, null=True, blank=True)
	city				= models.CharField(max_length=250)
	country				= models.CharField(max_length=250, default="United States of America")
	state				= models.CharField(max_length=250)
	postal_code			= models.CharField(max_length=250)



	def __str__(self):
		return str(self.billing_profile)




	def get_address(self):
		return "{line1}\n{line2}\n{city}\n{state}\n{postal_code}\n{country}".format(
						line1=self.address_line_1,
						line2=self.address_line_2 or "",
						city=self.city, 
						state=self.state,
						postal_code=self.postal_code,
						country=self.country

						)





ADDRESS_TYPES_LIVRAISON = (
	("facturation", "Facturation"),
	("livraison", "Livraison"),
	)


class AddressPayementLivraison(models.Model):
	payement_livraison						= models.ForeignKey(PayementLivraison, on_delete=models.CASCADE)
	address_payement_livraison_type 		= models.CharField(max_length=120, choices=ADDRESS_TYPES_LIVRAISON)
	address									= models.CharField(max_length=250)
	description								= models.CharField(max_length=250, null=True, blank=True)
	pays									= models.CharField(max_length=250)
	etat									= models.CharField(max_length=250)
	ville									= models.CharField(max_length=250)
	postal_code								= models.CharField(max_length=250)



	def __str__(self):
		return str(self.payement_livraison)




	def get_address(self):
		print("Avant exécution de get_address")
		return "{address_}\n{description_}\n{pays_}\n{etat_}\n{ville_}\n{postal_code_}".format(
						address_=self.address,
						description_=self.description or "",
						pays_=self.pays,
						etat_=self.etat,
						ville_=self.ville, 
						postal_code_=self.postal_code,

						)