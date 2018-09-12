from django.urls import re_path, path

from .views import (

			OrderListView,
			OrderDetailView,
			VerifyOwnership,
			LibraryView,
			)









app_name = "orders"




urlpatterns = [

			path("", OrderListView.as_view(), name="list"),
			path("library", LibraryView.as_view(), name="library"),
			path("endpoint/verify/ownership", VerifyOwnership.as_view(), name="verify_ownership"),

			re_path(r'^(?P<order_id>[0-9A-Za-z]+)$', OrderDetailView.as_view(), name="detail"),

















		]