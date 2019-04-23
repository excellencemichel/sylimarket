
from django.http import HttpResponse, JsonResponse


from django.shortcuts import render, redirect
from django.urls import reverse

from django.db.models import Q


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
	products =  Product.objects.all()
	news_products = Product.objects.featured()

	news_clothings = news_products.filter(
		Q(product_type=Product.MEN_CLOTHING)|
		Q(product_type=Product.WOMEN_CLOTHING)|
		Q(product_type=Product.PANTALON)|
		Q(product_type=Product.CULOTTE)|
		Q(product_type=Product.JUPE)|
		Q(product_type=Product.CLOTHING_ACCESSOIRE)
		)


	news_electroniques = news_products.filter(
		Q(product_type=Product.PHONE)|
		Q(product_type=Product.TABLETE)|
		Q(product_type=Product.PHONE_ACCESSOIRE)|
		Q(product_type=Product.COMPUTER)|
		Q(product_type=Product.COMPUTER_ACCESSOIRE)
		)

	news_chaussures = news_products.filter(
		Q(product_type=Product.MEN_SHOE)|
		Q(product_type=Product.WOMEN_SHOE)|
		Q(product_type=Product.CLOTHING_ACCESSOIRE)
		)

	clothings = products.filter(
		Q(product_type=Product.MEN_CLOTHING)|
		Q(product_type=Product.WOMEN_CLOTHING)|
		Q(product_type=Product.PANTALON)|
		Q(product_type=Product.CULOTTE)|
		Q(product_type=Product.JUPE)|
		Q(product_type=Product.CLOTHING_ACCESSOIRE)
		)


	men_clothings = products.filter(product_type=Product.MEN_CLOTHING) 
	women_clothings  = products.filter(product_type=Product.WOMEN_CLOTHING) 
	accessoire_clothings = products.filter(product_type=Product.CLOTHING_ACCESSOIRE)

	chaussures = products.filter(
		Q(product_type=Product.MEN_SHOE)|
		Q(product_type=Product.WOMEN_SHOE)|
		Q(product_type=Product.CLOTHING_ACCESSOIRE)
		)


	electroniques = products.filter(
		Q(product_type=Product.PHONE)|
		Q(product_type=Product.TABLETE)|
		Q(product_type=Product.PHONE_ACCESSOIRE)|
		Q(product_type=Product.COMPUTER)|
		Q(product_type=Product.COMPUTER_ACCESSOIRE)
		)

	day_products = products.day_products()
	special_products = products.special_products()
	best_sellers  = products.best_seller()


	men_shoes = Product.objects.get_men_shoes()
	women_shoes = Product.objects.get_women_shoes()

	phones 	= Product.objects.get_phones()
	tablettes = Product.objects.get_tablettes()
	accessoire_phones = Product.objects.get_phone_accessoires()

	computers = Product.objects.get_computers()
	accessoire_computers = Product.objects.get_computer_accessoires()


	jupes = Product.objects.get_jupes()

	pantalons = Product.objects.get_pantalons()
	culottes = Product.objects.get_culottes()





	context = {
		"cart": cart_obj,
		"products": products,
		"best_sellers" : best_sellers,
		"news_products": news_products,
		"news_clothings": news_clothings,
		"news_electroniques" : news_electroniques,
		"news_chaussures": news_chaussures,



		"day_products" : day_products,
		"special_products": special_products,


		"clothings": clothings,
		"men_clothings": men_clothings,
		"women_clothings": women_clothings,
		"accessoire_clothings": accessoire_clothings,

		"chaussures" : chaussures,

		"electroniques" : electroniques,

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
		# "men_clothings_new": men_clothings_new,
		# "women_clothings_new": women_clothings_new,
		# "accessoire_clothings_new": accessoire_clothings_new,

		# "pantalons_new": pantalons_new,
		# "jupes_new": jupes_new,
		# "culottes_new": culottes_new,


		# "phones_new": phones_new,
		# "tablettes_new": tablettes_new,
		# "accessoire_phones_new": accessoire_phones_new,

		# "computers_new": computers_new,
		# "accessoire_computers_new": accessoire_computers_new,

		# "men_shoes_new": men_shoes_new,
		# "women_shoes_new": women_shoes_new,



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








