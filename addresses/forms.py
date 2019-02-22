from django.utils.translation import pgettext, ugettext, ugettext_lazy as _

from django import forms


from .models import Address, AddressPayementLivraison



class AddressForm(forms.ModelForm):

	class Meta:
		model = Address

		fields = [

			# "billing_profile",
			# "address_type",
			"address_line_1",
			"address_line_2",
			"city",
			"country",
			"state",
			"postal_code",




			]


class AddressPayementLivraisonForm(forms.ModelForm):
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
	pays = forms.CharField(label=_("Pays par défaut ce sera la Guiné"), widget=forms.TextInput(attrs = {"class": "form-control",}) )
	ville = forms.ChoiceField(label=_("Votre ville"), help_text=_("Veillez à bien choisir la ville"), widget=forms.Select(attrs = {"class": "form-control",}), choices=VILLE_CHOICES)
	quartier = forms.CharField(label=_("Votre quartier de résidence"), widget=forms.TextInput(attrs = {"class": "form-control",}) )
	description = forms.CharField(label=_("Une description pour bien indiquer votre domicile"), widget=forms.Textarea(attrs={"class": "form-control",
                                                           "rows": "3",
                                                           }
                                                    ) )
	postal_code = forms.CharField(label=_("Votre code postal"), help_text=_("Cela est facultatif ou optionnels"), widget=forms.TextInput(attrs = {"class": "form-control",}) )

	class Meta:
		model = AddressPayementLivraison

		fields = [
			"pays",
			"ville",
			"quartier",
			"description",
			"postal_code"
		]


