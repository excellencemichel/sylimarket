from django.urls import re_path

from .views import (


			cart_home,
			cart_update,
			checkout_home,
			checkout_livraison,
			checkout_done_view,
			cart_detail_api_view,

			)








app_name = "carts"





urlpatterns = [

		
		re_path(r'^$', cart_home, name="home"),
		re_path(r'^update/$', cart_update, name="update"),
		re_path(r'^checkout/$', checkout_home, name="checkout"),
		re_path(r'^checkout-a-livraison/$', checkout_livraison, name="checkout_livraison"),
		re_path(r'^checkout/success$', checkout_done_view, name="success"),
   		re_path(r'^api/cart/$', cart_detail_api_view, name="api_cart"),










		]