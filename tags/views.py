from django.contrib import messages

from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy

from django.utils.translation import gettext_lazy as _

from django.db.models import Q


#Local import 
from products.models import Product 


from .models import Tag


# Create your views here.



def update_tag(request):
	product_id = request.POST.get("product_id")
	input_tag = request.POST.get("input_tag")
	print("Le type est: ", type(input_tag))

	if product_id:
		try:
			product_obj = Product.objects.get(id=product_id)
		except Product.DoesNotExist:
			messages.info(request, _("Désolé le produit que vous voulez tager est momentanement indisponible"))

		exist_tag = Tag.objects.filter(products__id=product_id)
		if exist_tag:
			print("Le tag existe déjà pour se produit")
		else:
			new_tag = product_obj.tag_set.create(title=product_obj.name, tag_text=input_tag, tag_product_type=product_obj.product_type)

		if request.is_ajax():
			json_data = {
				"added": True,
				"removed": False,
			}
			return JsonResponse(json_data, status=200)

	return redirect("home")




def electronique_products_tag(request):
	products = Product.objects.filter(
		Q(tag__tag_product_type= Product.PHONE)|
		Q(tag__tag_product_type= Product.TABLETE)|
		Q(tag__tag_product_type= Product.PHONE_ACCESSOIRE)|
		Q(tag__tag_product_type= Product.COMPUTER)|
		Q(tag__tag_product_type= Product.COMPUTER_ACCESSOIRE)

		)
	context = {
		"products": products,
	}

	return render(request, "tags/electronique_products_tag.html", context)


def accessoires_products_tag(request):
	products = Product.objects.filter(
		Q(tag__tag_product_type= Product.CLOTHING_ACCESSOIRE)|
		Q(tag__tag_product_type= Product.PHONE_ACCESSOIRE)|
		Q(tag__tag_product_type= Product.COMPUTER_ACCESSOIRE)

		)
	context = {
		"products": products,
	}

	return render(request, "tags/accessoires_products_tag.html", context)



def clothing_products_tag(request):
	products = Product.objects.filter(
		Q(tag__tag_product_type= Product.MEN_CLOTHING)|
		Q(tag__tag_product_type= Product.WOMEN_CLOTHING)|
		Q(tag__tag_product_type= Product.CLOTHING_ACCESSOIRE)|
		Q(tag__tag_product_type= Product.PANTALON)|
		Q(tag__tag_product_type= Product.CULOTTE)|
		Q(tag__tag_product_type= Product.JUPE)
		)
	context = {
		"products": products,
	}

	return render(request, "tags/clothing_products_tag.html", context)



def fournitures_products_tag(request):
	products = Product.objects.filter(
		Q(tag__tag_product_type= Product.VISUAL_AUDIO)

		)
	context = {
		"products": products,
	}

	return render(request, "tags/fournitures_products_tag.html", context)




def nature_products_tag(request):
	products = Product.objects.filter(
		Q(tag__tag_product_type= Product.WATCH)

		)
	context = {
		"products": products,
	}

	return render(request, "tags/nature_products_tag.html", context)




def shoes_products_tag(request):
	products = Product.objects.filter(
		Q(tag__tag_product_type= Product.MEN_SHOE)|
		Q(tag__tag_product_type= Product.WOMEN_SHOE)
		)
	context = {
		"products": products,
	}

	return render(request, "tags/shoes_products_tag.html", context)