from django.urls import re_path, path

from .views import (


			cart_home,
			 cart_update_to_add,
			 cart_update_to_delete,
			 checkout_card,
			 cart_detail_api_view,
			 checkout_livraison,
			 checkout_done_view,
			 payement_method,
			 checkout_mobile,

			)




app_name = "carts"





urlpatterns = [

		
		path("", cart_home, name="home"),
		path("api/cart/", cart_detail_api_view, name="api_cart"),
		path("update", cart_update_to_add, name="update"),
		path("update-delete", cart_update_to_delete, name="update_to_delete"),
		path("checkout-livraison", checkout_livraison, name="checkout_livraison"),
		path("payement-method/choices", payement_method, name="payement_method"),
		path("checkout-mobile", checkout_mobile, name="checkout_mobile"),
		path("checkout", checkout_card, name="checkout"),


		re_path(r'^checkout/success$', checkout_done_view, name="success"),



	










		]