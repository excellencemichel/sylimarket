from django.urls import re_path
from django.contrib.auth.views import LogoutView


from .views import (

			checkout_address_create_view,
			checkout_address_use_view,
			checkout_address_livraison_create_view,
			checkout_address_livraison_use_view,

			)

app_name = "addresses"






urlpatterns = [

	     re_path(r'^checkout/address/create/$', checkout_address_create_view, name="checkout_address_create"),
	     re_path(r'^checkout/address/reuse/$', checkout_address_use_view, name="checkout_address_reuse"),

	     re_path(r'^checkout/address_livraison/create/$', checkout_address_livraison_create_view, name="checkout_address_livraison_create"),
	     re_path(r'^checkout/address_livraison/reuse/$', checkout_address_livraison_use_view, name="checkout_address_livraison_reuse"),

		


]