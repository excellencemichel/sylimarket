from django.urls import re_path, path

from .views import (


			cart_home,
			 update_cart,
			 checkout_card,
			 cart_detail_api_view,
			 checkout_livraison,
			 checkout_done_view,
			 payement_method,
			 checkout_mobile,

			 demo_ajax,

			)




app_name = "carts"





urlpatterns = [

		
		path("", cart_home, name="home"),
		path("api/cart/", cart_detail_api_view, name="api_cart"),
		path("update-cart", update_cart, name="update_cart"),

		path("checkout-livraison", checkout_livraison, name="checkout_livraison"),
		path("payement-method/choices", payement_method, name="payement_method"),
		path("checkout-mobile", checkout_mobile, name="checkout_mobile"),
		path("checkout", checkout_card, name="checkout"),

		#demo ajax
		path("demo", demo_ajax, name="demo_ajax"),



		re_path(r'^checkout/success$', checkout_done_view, name="success"),



	










		]