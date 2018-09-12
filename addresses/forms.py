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
	class Meta:
		model = AddressPayementLivraison

		fields = [
			"address",
			"description",
			"pays",
			"etat",
			"ville",
			"postal_code"
		]


