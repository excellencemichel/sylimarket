from django.urls import re_path, path

from .views import (

			 update_tag,
			 electronique_products_tag,
			 shoes_products_tag,
			 accessoires_products_tag,
			 clothing_products_tag,
			 fournitures_products_tag,
			 nature_products_tag,

			)




app_name = "tags"





urlpatterns = [

		path("update-tag", update_tag, name="update_tag"),
		path("electronique-products-tag", electronique_products_tag, name="electronique_products_tag"),
		path("shoes-products-tag", shoes_products_tag, name="shoes_products_tag"),
		path("accessoires-products-tag", accessoires_products_tag, name="accessoires_products_tag"),
		path("clothing-products-tag", clothing_products_tag, name="clothing_products_tag"),
		path("fournitures-products-tag", fournitures_products_tag, name="fournitures_products_tag"),
		path("nature-products-tag", nature_products_tag, name="nature_products_tag"),






	










		]