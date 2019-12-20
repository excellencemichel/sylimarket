from django.urls import re_path, path

from .views import (
			home,
			create,
			detail,
			)




app_name = "blogs"





urlpatterns = [

		path("home", home, name="home"),

    	re_path(r'^create/$', create, name="create"),

    	re_path(r'^detail/(?P<id>\d+)-(?P<slug>[\w-]+)/$', detail, name="detail"),







	





		]