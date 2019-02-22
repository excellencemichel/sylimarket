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
<<<<<<< HEAD
	products = Product.objects.all()
	phones  = products.filter(types_product="phone")
	electromenagers  = products.filter(types_product="electromenager")
	electroniques 	 = products.filter(types_product="electronique")
	cloths			 = products.filter(types_product="cloths")
	shoes 			 = products.filter(types_product="shoe")
	luxes 			 = products.filter(types_product="luxe")
	tablettes 		 = products.filter(types_product="tablette")
	computers 		 = products.filter(types_product="computer")
	foods 			 = products.filter(types_product="food")
	fournitures 	 = products.filter(types_product="fourniture")
	materiels 		 = products.filter(types_product="materiel")
	pants 			 = products.filter(types_product="pants")


=======
	products =  Product.objects.all()[:5]
	news_products = Product.objects.featured()[:4]

	men_clothings = MenClothing.objects.all() 
	women_clothings  = WomenClothing.objects.all()
	accessoire_clothings = AccessoireClothng.objects.all()

	men_shoes = MenShoes.objects.all()
	women_shoes = WomenShoes.objects.all()
>>>>>>> dev

	phones 	= Phone.objects.all()
	tablettes = Tablette.objects.all()
	accessoire_phones = AccessoirePhone.objects.all()

	computers = Computer.objects.all()
	accessoire_computers = AccessoireComputer.objects.all()


	jupes = Jupe.objects.all()

	pantalons = Pantalon.objects.all()
	culottes = Culotte.objects.all()


	




	context = {
<<<<<<< HEAD
		"cart": 			cart_obj,
		"products": 		products,
		"phones": 			phones,
		"electromenagers":  electromenagers,
		"electroniques": 	electroniques,
		"cloths": 			cloths,
		"shoes": 			shoes,
		"luxes": 			luxes,
		"tablettes": 		tablettes,
		"computers": 		computers,
		"foods": 			foods,
		"fournitures": 		fournitures,
		"materiels": 		materiels,
		"pants": 			pants,


=======
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

>>>>>>> dev


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






