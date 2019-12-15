from django.urls import re_path, path

from .views import (


			ProductListView,
			ProductFeaturedListView,
			ProductFeaturedDetailView,
			UserProductHistoryView,


			men_clothing_detail, 	women_clothing_detail,

			accessoire_clothing_detail,	men_shoe_detail,

			women_shoe_detail, patalon_detail, culotte_detail, 

			jupe_detail,  phone_detail, tablette_detail,

			accessoire_phone_detail, computer_detail, 

			accessoire_computer_detail,

			electromenager_detail,
			



			MenClothingListView,
			WomenClothingListView, PantalonListView, CulotteListView,
 			JupeListView, MenShoesListView,
			WomenShoesListView, AccessoireClothngListView,
			ComputerListView, AccessoireComputerListView, PhoneListView, 
			TabletteListView, AccessoirePhoneListView,

			ElectromenagerListView,


			)









app_name = "products"




urlpatterns = [


			path("", ProductListView.as_view(), name="list"),

			#list products
			path("men-clothing-list", MenClothingListView.as_view(), name="men_clothing_list"),
			path("women-clothing-list", WomenClothingListView.as_view(), name="women_clothing_list"),
			path("pantalon-list", PantalonListView.as_view(), name="pantalon_list"),
			path("culotte-list", CulotteListView.as_view(), name="culotte_list"),
			path("jupe-list", JupeListView.as_view(), name="jupe_list"),
			path("men-shoe-list", MenShoesListView.as_view(), name="men_shoe_list"),
			path("women-shoe-list", WomenShoesListView.as_view(), name="women_shoe_list"),
			path("accessoire-clothing-list", AccessoireClothngListView.as_view(), name="accessoire_clothing_list"),
			path("computer-list", ComputerListView.as_view(), name="computer_list"),
			path("accessoire-computer-list", AccessoireComputerListView.as_view(), name="accessoire_computer_list"),
			path("phone-list", PhoneListView.as_view(), name="phone_list"),
			path("tablette-list", TabletteListView.as_view(), name="tablette_list"),
			path("accessoire-phone-list", AccessoirePhoneListView.as_view(), name="accessoire_phone_list"),

			path("electromenager-list", ElectromenagerListView.as_view(), name="electromenager_list"),


			# re_path(r'^(?P<pk>\d+)-(?P<slug>[\w-]+)/detail/$', product_detail, name="detail"),	




			re_path(r'^(?P<pk>\d+)-(?P<slug>[\w-]+)/men-clothing-detail/$', men_clothing_detail, name="men_clothing_detail"),			
			re_path(r'^(?P<pk>\d+)-(?P<slug>[\w-]+)/women-clothing-detail/$', women_clothing_detail, name="women_clothing_detail"),			
			re_path(r'^(?P<pk>\d+)-(?P<slug>[\w-]+)/accessoire-clothing-detail/$', accessoire_clothing_detail, name="accessoire_clothing_detail"),			
			re_path(r'^(?P<pk>\d+)-(?P<slug>[\w-]+)/men-shoe-detail/$', men_shoe_detail, name="men_shoe_detail"),			
			re_path(r'^(?P<pk>\d+)-(?P<slug>[\w-]+)/women-shoe-detail/$', women_shoe_detail, name="women_shoe_detail"),			
			re_path(r'^(?P<pk>\d+)-(?P<slug>[\w-]+)/patalon-detail/$', patalon_detail, name="patalon_detail"),			
			re_path(r'^(?P<pk>\d+)-(?P<slug>[\w-]+)/culotte-detail/$', culotte_detail, name="culotte_detail"),	
			re_path(r'^(?P<pk>\d+)-(?P<slug>[\w-]+)/jupe-detail/$', jupe_detail, name="jupe_detail"),					
			re_path(r'^(?P<pk>\d+)-(?P<slug>[\w-]+)/phone-detail/$', phone_detail, name="phone_detail"),			
			re_path(r'^(?P<pk>\d+)-(?P<slug>[\w-]+)/tablette-detail/$', tablette_detail, name="tablette_detail"),			
			re_path(r'^(?P<pk>\d+)-(?P<slug>[\w-]+)/accessoire-phone-detail/$', accessoire_phone_detail, name="accessoire_phone_detail"),			
			re_path(r'^(?P<pk>\d+)-(?P<slug>[\w-]+)/computer-detail/$', computer_detail, name="computer_detail"),			
			re_path(r'^(?P<pk>\d+)-(?P<slug>[\w-]+)/accessoire-computer-detail/$', accessoire_computer_detail, name="accessoire_computer_detail"),			
			re_path(r'^(?P<pk>\d+)-(?P<slug>[\w-]+)/electromenager-detail/$', electromenager_detail, name="electromenager_detail"),			

		


			path("featured", ProductFeaturedListView.as_view(), name="list_featured"),
			re_path(r'^featured/(?P<pk>\d+)/$', ProductFeaturedDetailView.as_view(), name="detail_featured"),


			path('history/products', UserProductHistoryView.as_view(), name="user_history"),







		]