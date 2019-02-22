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








class AddressPayementLivraison(models.Model):

	FACTURATION = "facturation"
	LIVRAISON = "livraison"

	ADDRESS_TYPES_LIVRAISON = (
	(FACTURATION, "Facturation"),
	("LIVRAISON", "Livraison"),
	)

	VILLE_CONAKRY = "conakry"

	VILLE_BOKE = "boke"
	VILLE_BOFFA = "boffa"
	VILLE_FRIA = "fria"
	VILLE_DUBREKA = "dubreka"
	VILLE_KAMSAR = "kamsar"
	VILLE_GAOUAL = "gaoual"
	VILLE_KOUNDARA = "koundara"



	VILLE_KINDIA = "kindia"
	VILLE_COYAH = "coyah"
	VILLE_FORECARIAH = "forecariah"
	VILLE_TELIMELE = "telimele"

	VILLE_MAMOU = "mamou"
	VILLE_PITA = "pita"
	VILLE_DALABA = "dalaba"


	VILLE_LABE = "labe"
	VILLE_LELOUMA = "Lelouma"
	VILLE_KOUBIA = "koubia"
	VILLE_TOUGUE = "tougue"
	VILLE_MALI = "mali"


	VILLE_FARANAH = "faranah"
	VILLE_DABOLA = "dabola"
	VILLE_KISSIDOUGOU = "kissidougou"
	VILLE_DINGUIRAYE = "dinguiraye"


	VILLE_KANKAN = "kankan"
	VILLE_MADIANAH = "madianah"
	VILLE_KOUROUSSA = "kouroussa"
	VILLE_SIGUIRI = "siguiri"

	VILLE_NZEREKORE = "nzerekore"
	VILLE_MACENTA = "macenta"
	VILLE_LOLA = "lola"
	VILLE_YOMOU = "yomou"
	VILLE_BEYLA = "beyla"
	VILLE_GUEKEDOU = "guekedou"

	VILLE_CHOICES = (

		(VILLE_CONAKRY, "Conakry"),
		(VILLE_BOKE, "Boké"),
		(VILLE_BOFFA, "Boffa"),
		(VILLE_FRIA, "Fria"),
		(VILLE_GAOUAL, "Gaoual"),
		(VILLE_KOUNDARA, "Koundara"),
		(VILLE_DUBREKA, "Dubreka"),
		(VILLE_KAMSAR, "Kamsar"),




		(VILLE_KINDIA, "Kindia"),
		(VILLE_FORECARIAH, "Forécariah"),
		(VILLE_COYAH, "Coyah"),
		(VILLE_TELIMELE, "Télimélé"),




		(VILLE_MAMOU, "Mamou"),
		(VILLE_PITA, "Pita"),
		(VILLE_DALABA, "Dalaba"),




		(VILLE_LABE, "Labé"),
		(VILLE_LELOUMA, "Lélouma"),
		(VILLE_MALI, "Mali yimbèrè"),
		(VILLE_KOUBIA, "Koubia"),
		(VILLE_TOUGUE, "Tougué"),





		(VILLE_FARANAH, "Faranah"),
		(VILLE_DINGUIRAYE, "Dinguiraye"),
		(VILLE_KISSIDOUGOU, "Kissidougou"),
		(VILLE_DABOLA, "Dabola"),




		(VILLE_KANKAN, "Kankan"),
		(VILLE_SIGUIRI, "Siguiri"),
		(VILLE_MADIANAH, "Madianah"),
		(VILLE_KOUROUSSA, "Kouroussa"),


		(VILLE_NZEREKORE, "N'Zérékoré"),
		(VILLE_MACENTA, "Macenta"),
		(VILLE_LOLA, "Lola"),
		(VILLE_BEYLA, "Beyla"),
		(VILLE_YOMOU, "Yomou"),





		)

	payement_livraison						= models.ForeignKey(PayementLivraison, on_delete=models.CASCADE)
	address_payement_livraison_type 		= models.CharField(max_length=120, choices=ADDRESS_TYPES_LIVRAISON)
	pays									= models.CharField(max_length=250, default="Guinée")
	ville									= models.CharField(max_length=250, choices=VILLE_CHOICES, default=VILLE_CONAKRY)
	quartier								= models.CharField(max_length=250)
	description								= models.TextField(null=True, blank=True)
	mobile									= models.CharField(max_length=250)
	postal_code								= models.CharField(max_length=250, null=True, blank=True)



	def __str__(self):
		return str(self.payement_livraison)




	def get_address(self):
		return "Pays: {pays_}\n ; Ville : {ville_}; \n Quartier:{quartier_};\n Description :{description_};\n Numéro de téléphone :{mobile_}; \nCode postal :{postal_code_}".format(
						pays_=self.pays,
						ville_=self.ville,
						quartier_= self.quartier,
						description_=self.description or "",
						mobile_=self.mobile,
						postal_code_=self.postal_code or "",
						)