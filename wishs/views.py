from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.contrib import messages

from django.http import JsonResponse
from django.urls import reverse, reverse_lazy

# Locals imports
from products.models import Product 

from .models import Wish

# Create your views here.
@login_required
def wish_home(request):
	wish_obj = Wish.objects.filter(user=request.user).first()
	print("Liste de souhaits", wish_obj)
	context = {
		"wishs": wish_obj,
	}
	return render(request, "wishs/home.html", context)
@login_required
def update_wish(request):

	product_id = request.POST.get("product_id")

	if product_id:
		try:
			product_obj = Product.objects.get(id=product_id)
		except Product.DoesNotExist:
			messages.info(request, _("Désolé Mme M {user} l'action que vous voulez faire n'a pu être effectué, nous y travaillons pour mettre l'ordre"))
		wish_obj, new_obj = Wish.objects.new_or_get(request)
		if product_obj in wish_obj.products.all():
			wish_obj.products.remove(product_obj)

			added = False
		else:
			wish_obj.products.add(product_obj)
			added = True



		request.session["wish_items"] = wish_obj.products.count()


		if request.is_ajax():
			json_data = {
				"added": added,
				"removed": not added,

				"wishItemCount": wish_obj.products.count(),

			}
			return JsonResponse(json_data, status=200)







