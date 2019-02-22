from django.urls import re_path, path

from .views import (


			ProductListView,
			product_detail,
			ProductFeaturedListView,
			ProductFeaturedDetailView,
			UserProductHistoryView,


			men_clothing_detail, 	women_clothing_detail,

			accessoire_clothing_detail,	men_shoe_detail,

			women_shoe_detail, patalon_detail, culotte_detail, 

			jupe_detail,  phone_detail, tablette_detail,

			accessoire_phone_detail, computer_detail, 

			accessoire_computer_detail


			)









app_name = "products"




urlpatterns = [


			path("", ProductListView.as_view(), name="list"),
			re_path(r'^(?P<slug>[\w-]+)/detail/$', product_detail, name="detail"),	

			re_path(r'^(?P<slug>[\w-]+)/detail/$', men_clothing_detail, name="men_clothing_detail"),			
			re_path(r'^(?P<slug>[\w-]+)/detail/$', women_clothing_detail, name="women_clothing_detail"),			
			re_path(r'^(?P<slug>[\w-]+)/detail/$', accessoire_clothing_detail, name="accessoire_clothing_detail"),			
			re_path(r'^(?P<slug>[\w-]+)/detail/$', men_shoe_detail, name="men_shoe_detail"),			
			re_path(r'^(?P<slug>[\w-]+)/detail/$', women_shoe_detail, name="women_shoe_detail"),			
			re_path(r'^(?P<slug>[\w-]+)/detail/$', patalon_detail, name="patalon_detail"),			
			re_path(r'^(?P<slug>[\w-]+)/detail/$', culotte_detail, name="culotte_detail"),	
			re_path(r'^(?P<slug>[\w-]+)/detail/$', jupe_detail, name="jupe_detail"),					
			re_path(r'^(?P<slug>[\w-]+)/detail/$', phone_detail, name="phone_detail"),			
			re_path(r'^(?P<slug>[\w-]+)/detail/$', tablette_detail, name="tablette_detail"),			
			re_path(r'^(?P<slug>[\w-]+)/detail/$', accessoire_phone_detail, name="accessoire_phone_detail"),			
			re_path(r'^(?P<slug>[\w-]+)/detail/$', computer_detail, name="computer_detail"),			
			re_path(r'^(?P<slug>[\w-]+)/detail/$', accessoire_computer_detail, name="accessoire_computer_detail"),			
		


			path("featured", ProductFeaturedListView.as_view(), name="list_featured"),
			re_path(r'^featured/(?P<pk>\d+)/$', ProductFeaturedDetailView.as_view(), name="detail_featured"),


			path('history/products', UserProductHistoryView.as_view(), name="user_history"),









		]