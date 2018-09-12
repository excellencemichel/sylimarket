from django.http import HttpResponse, JsonResponse


from django.shortcuts import render, redirect
from django.urls import reverse



#Local import 

from products.models import Product
from carts.models import Cart




from .forms import (


			ContactForm,

	)




def home(request):
	cart_obj, new_obj = Cart.objects.new_or_get(request)
	products = Product.objects.all()
	phones  = products.filter(types_product="phone")
	electromenagers  = products.filter(types_product="electromenager")
	electroniques 	 = products.filter(types_product="electronique")
	cloths			 = products.filter(types_product="cloths")
	shoes 			 = products.filter(types_product="shoe")





	context = {
		"cart": cart_obj,
		"products": products,
		"phones": phones,
		"electromenagers": electromenagers,
		"electroniques": electroniques,
		"cloths": cloths,
		"shoes": shoes,


		}

	

	return render(request, "home.html", context)






def about_page(request):

	context = {
		"title" : "About page",
		"content" : "Welcome to the About page"

	}

	return render(request, "home.html", context)


def contact_page(request):

	contact_form = ContactForm(request.POST or None)

	context = {
		"title" :"Contact",
		"content" : "Welcome to the Contact page",
		"form" : contact_form,

		"brand": "New brand Name",

	}

	if contact_form.is_valid():
		if request.is_ajax():
			return JsonResponse({"message": "Thank you for your submission"})
		print(contact_form.cleaned_data)

	if contact_form.errors:
		errors = contact_form.errors.as_json()
		if request.is_ajax():
			return HttpResponse(errors, status=400, content_type="application/json")

	# if request.method == "POST":
	# 	print(request.POST)
	# 	print(request.POST.get("fullname"))
	# 	print(request.POST.get("email"))
	# 	print(request.POST.get("content"))

	return render(request, "contact/views.html", context)




def home_page_old(request):
	html_ = """
			<!doctype html>
			<html lang="en">
			  <head>
			    <!-- Required meta tags -->
			    <meta charset="utf-8">
			    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

			    <!-- Bootstrap CSS -->
			    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

			    <title>Hello, world!</title>
			  </head>
			  <body>
			  	<div class="text-center">
			    <h1>Hello, world!</h1>

			    </div>

			    <!-- Optional JavaScript -->
			    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
			    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
			    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
			    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
			  </body>
			</html>


	"""

	return HttpResponse(html_)





