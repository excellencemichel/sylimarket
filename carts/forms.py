from django.utils.translation import pgettext, ugettext, ugettext_lazy as _

from django import forms




class PayementMethod(forms.Form):
	METHOD_LIVRAISON = "livraison"
	METHOD_BANCAIRE = "bancaire"
	METHOD_MOBILE = "mobile"

	METHOD_CHOICE = (
		(METHOD_LIVRAISON, "Payement à la livraison"),
		(METHOD_MOBILE, "Payement par les réseaux mobile (Orange Money)"),
		(METHOD_BANCAIRE, "Payement par carte de crédit bancaire"),

		)

	paymement_choices = forms.ChoiceField(label=_("Votre choix de payement"),
			 help_text=_("Velliez à bien faire le choix parce que la suite y dépend"),
			 widget=forms.RadioSelect(attrs = {"class": "form-check-input",}),
			 choices=METHOD_CHOICE, required=True

			 )