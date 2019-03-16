from django.http import HttpResponse, JsonResponse


from django.shortcuts import render, redirect
from django.urls import reverse



#Local import 
#import from models
from products.models import (  Product,

					#clothings
					MenClothing, WomenClothing, Pantalon,
					Culotte, Jupe, MenShoes,
					WomenShoes, AccessoireClothng,

					#computers
					Computer, AccessoireComputer,

					#phones
					Phone, Tablette, AccessoirePhone

					)

from carts.models import Cart




from .forms import (


			ContactForm,

	)




def home(request):
	cart_obj, new_obj = Cart.objects.new_or_get(request)
	products =  Product.objects.all()[:5]
	news_products = Product.objects.featured()[:4]

	men_clothings = MenClothing.objects.all() 
	women_clothings  = WomenClothing.objects.all()
	accessoire_clothings = AccessoireClothng.objects.all()

	men_shoes = MenShoes.objects.all()
	women_shoes = WomenShoes.objects.all()

	phones 	= Phone.objects.all()
	tablettes = Tablette.objects.all()
	accessoire_phones = AccessoirePhone.objects.all()

	computers = Computer.objects.all()
	accessoire_computers = AccessoireComputer.objects.all()


	jupes = Jupe.objects.all()

	pantalons = Pantalon.objects.all()
	culottes = Culotte.objects.all()


	# New
	men_clothings_new = MenClothing.objects.featured()[:3]
	women_clothings_new  = WomenClothing.objects.featured()[:3]
	accessoire_clothings_new = AccessoireClothng.objects.featured()[:3]

	men_shoes_new = MenShoes.objects.featured()[:3]
	women_shoes_new = WomenShoes.objects.featured()[:3]

	phones_new 	= Phone.objects.featured()[:3]
	tablettes_new = Tablette.objects.featured()[:3]
	accessoire_phones_new = AccessoirePhone.objects.featured()[:3]

	computers_new = Computer.objects.featured()[:3]
	accessoire_computers_new = AccessoireComputer.objects.featured()[:3]


	jupes_new = Jupe.objects.featured()[:3]

	pantalons_new = Pantalon.objects.featured()[:3]
	culottes_new = Culotte.objects.featured()[:3]
	




	context = {
		"cart": cart_obj,
		"products": products,
		"news_products": news_products,


		"men_clothings": men_clothings,
		"women_clothings": women_clothings,
		"accessoire_clothings": accessoire_clothings,

		"pantalons": pantalons,
		"jupes": jupes,
		"culottes": culottes,


		"phones": phones,
		"tablettes": tablettes,
		"accessoire_phones": accessoire_phones,

		"computers": computers,
		"accessoire_computers": accessoire_computers,

		"men_shoes": men_shoes,
		"women_shoes": women_shoes,

		# New
		"men_clothings_new": men_clothings_new,
		"women_clothings_new": women_clothings_new,
		"accessoire_clothings_new": accessoire_clothings_new,

		"pantalons_new": pantalons_new,
		"jupes_new": jupes_new,
		"culottes_new": culottes_new,


		"phones_new": phones_new,
		"tablettes_new": tablettes_new,
		"accessoire_phones_new": accessoire_phones_new,

		"computers_new": computers_new,
		"accessoire_computers_new": accessoire_computers_new,

		"men_shoes_new": men_shoes_new,
		"women_shoes_new": women_shoes_new,



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





