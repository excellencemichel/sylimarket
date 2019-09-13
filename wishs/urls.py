from django.urls import re_path, path

from .views import (


			wish_home,
			update_wish,

			)




app_name = "wishs"





urlpatterns = [

		
		path("", wish_home, name="home"),
		path("update-wish", update_wish, name="update_wish"),


	










		]