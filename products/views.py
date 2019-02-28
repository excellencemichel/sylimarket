
from django.conf import settings

from django.http import Http404, HttpResponse, HttpResponseRedirect

from django.views.generic import ListView, View, DetailView

from django.shortcuts import render, get_object_or_404, redirect

from django.utils.decorators import method_decorator
from django.utils.translation import gettext_lazy as _



from django.contrib.auth.decorators import login_required
from django.contrib import messages



#Local import
from analytics.mixins import ObjectViewedMixin
from analytics.signals import object_viewed_signal
from carts.models import Cart
from orders.models import ProductPurshase




#import from models
from .models import (  Product,

					#clothings
					MenClothing, WomenClothing, Pantalon,
					Culotte, Jupe, MenShoes,
					WomenShoes, AccessoireClothng,

					#computers
					Computer, AccessoireComputer,

					#phones
					Phone, Tablette, AccessoirePhone

					)




# Create your views here.




class ProductFeaturedListView(ListView):
	template_name = "products/list.html"


	def get_queryset(self, *args, **kwargs):
		request = self.request
		return Product.objects.featured()


class ProductFeaturedDetailView(ObjectViewedMixin, DetailView):
	queryset = Product.objects.featured()
	template_name = "products/featured_detail.html"

	def get_queryset(self, *args, **kwargs):
		request = self.request
		return Product.objects.all()






class ProductListView(ListView):
	template_name = "products/list.html"

	def get_context_data(self, *args, **kwargs):
		context = super(ProductListView,self).get_context_data(*args, **kwargs)
		cart_obj, new_obj = Cart.objects.new_or_get(self.request)
		context["cart"] = cart_obj
		return context



	def get_queryset(self, *args, **kwargs):
		request = self.request
		return Product.objects.all()




def product_detail(request, pk=None, slug=None):
	product = get_object_or_404(Product, slug=slug)
	cart_obj, new_obj = Cart.objects.new_or_get(request)
	product_in_cart = cart_obj.cart_item_exists(product)
	print("Dans product")


	context = {
		"product": product,
		"cart": cart_obj,
		"product_in_cart": product_in_cart,
	}


	return render(request, "products/detail.html", context)








@method_decorator(login_required, name='dispatch') # ça peut marcher si on veux rediriger l'utilisateur sur la page de connexion
class UserProductHistoryView(ListView):
	template_name = "products/user_history.html"


	def get_context_data(self, *args, **kwargs):
		context = super(UserProductHistoryView, self).get_context_data(*args, **kwargs)
		cart_obj, new_obj = Cart.objects.new_or_get(self.request)
		context["cart"] = cart_obj
		return context



	def get_queryset(self, *args, **kwargs):
		request = self.request
		views 	= request.user.objectviewed_set.by_model(Product, model_queryset=True) #all().filter(content_type__name="product")

		
		return views #Product.objects.filter(pk__in=viewed_ids)










def men_clothing_detail(request, pk=None, slug=None):
	men_clothing = get_object_or_404(MenClothing, pk=pk, slug=slug)
	cart_obj, new_obj = Cart.objects.new_or_get(request)
	product_in_cart = cart_obj.cart_item_exists(men_clothing)

	context = {
		"cart": cart_obj,
		"product_in_cart": product_in_cart,
		"product": men_clothing,
	}


	return render(request, "products/men_clothing_detail.html", context)





def women_clothing_detail(request, pk=None, slug=None):
	women_clothing = get_object_or_404(WomenClothing, pk=pk, slug=slug)
	cart_obj, new_obj = Cart.objects.new_or_get(request)
	product_in_cart = cart_obj.cart_item_exists(women_clothing)

	context = {
		"cart": cart_obj,
		"product_in_cart": product_in_cart,
		"product": women_clothing
	}


	return render(request, "products/women_clothing_detail.html", context)




def accessoire_clothing_detail(request, pk=None, slug=None):
	accessoire_clothing = get_object_or_404(AccessoireClothng, pk=pk, slug=slug)
	cart_obj, new_obj = Cart.objects.new_or_get(request)
	product_in_cart = cart_obj.cart_item_exists(accessoire_clothing)

	context = {
		"cart": cart_obj,
		"product_in_cart": product_in_cart,
		"product": accessoire_clothing
	}


	return render(request, "products/accessoire_clothing_detail.html", context)



def men_shoe_detail(request, pk=None, slug=None):
	men_shoe = get_object_or_404(MenShoes, pk=pk, slug=slug)
	cart_obj, new_obj = Cart.objects.new_or_get(request)
	product_in_cart = cart_obj.cart_item_exists(men_shoe)

	context = {
		"cart": cart_obj,
		"product_in_cart": product_in_cart,
		"product": men_shoe
	}


	return render(request, "products/men_shoe_detail.html", context)






def women_shoe_detail(request, pk=None, slug=None):
	women_sheo = get_object_or_404(WomenShoes, pk=pk, slug=slug)
	cart_obj, new_obj = Cart.objects.new_or_get(request)
	product_in_cart = cart_obj.cart_item_exists(women_sheo)

	context = {
		"cart": cart_obj,
		"product_in_cart": product_in_cart,
		"product": women_sheo
	}


	return render(request, "products/women_shoe_detail.html", context)









def patalon_detail(request, pk=None, slug=None):
	pantalon = get_object_or_404(Pantalon, pk=pk, slug=slug)
	cart_obj, new_obj = Cart.objects.new_or_get(request)
	product_in_cart = cart_obj.cart_item_exists(pantalon)

	context = {
		"cart": cart_obj,
		"product_in_cart": product_in_cart,
		"product": pantalon
	}


	return render(request, "products/pantalon_detail.html", context)









def culotte_detail(request, pk=None, slug=None):
	culotte = get_object_or_404(Culotte, slug=slug)
	cart_obj, new_obj = Cart.objects.new_or_get(request)
	product_in_cart = cart_obj.cart_item_exists(culotte)

	context = {
		"cart": cart_obj,
		"product_in_cart": product_in_cart,
		"product": culotte
	}


	return render(request, "products/culotte_detail.html", context)









def jupe_detail(request, pk=None, slug=None):
	jupe = get_object_or_404(Jupe, pk=pk, slug=slug)
	cart_obj, new_obj = Cart.objects.new_or_get(request)
	product_in_cart = cart_obj.cart_item_exists(jupe)
	print("Dans jupe")
	print("Si dedans", product_in_cart)

	context = {
		"cart": cart_obj,
		"product_in_cart": product_in_cart,
		"product": jupe
	}


	return render(request, "products/jupe_detail.html", context)




def phone_detail(request, pk=None, slug=None):
	phone = get_object_or_404(Phone, pk=pk, slug=slug)
	cart_obj, new_obj = Cart.objects.new_or_get(request)
	product_in_cart = cart_obj.cart_item_exists(phone)

	context = {
		"cart": cart_obj,
		"product_in_cart": product_in_cart,
		"product": phone
	}


	return render(request, "products/phone_detail.html", context)





def tablette_detail(request, pk=None, slug=None):
	tablette = get_object_or_404(Tablette, pk=pk, slug=slug)
	cart_obj, new_obj = Cart.objects.new_or_get(request)
	product_in_cart = cart_obj.cart_item_exists(tablette)

	context = {
		"cart": cart_obj,
		"product_in_cart": product_in_cart,
		"product": tablette
	}


	return render(request, "products/tablette_detail.html", context)









def accessoire_phone_detail(request, pk=None, slug=None):
	accessoire_phone = get_object_or_404(AccessoirePhone, pk=pk, slug=slug)
	cart_obj, new_obj = Cart.objects.new_or_get(request)
	product_in_cart = cart_obj.cart_item_exists(accessoire_phone)

	context = {
		"cart": cart_obj,
		"product_in_cart": product_in_cart,
		"product": accessoire_phone
	}


	return render(request, "products/accessoire_phone_detail.html", context)









def computer_detail(request, pk=None, slug=None):
	computer = get_object_or_404(Computer, pk=pk, slug=slug)
	cart_obj, new_obj = Cart.objects.new_or_get(request)
	product_in_cart = cart_obj.cart_item_exists(computer)

	context = {
		"cart": cart_obj,
		"product_in_cart": product_in_cart,
		"product": computer
	}


	return render(request, "products/computer_detail.html", context)









def accessoire_computer_detail(request, pk=None, slug=None):
	accessoire_computer = get_object_or_404(AccessoireComputer, pk=pk, slug=slug)
	cart_obj, new_obj = Cart.objects.new_or_get(request)
	product_in_cart = cart_obj.cart_item_exists(accessoire_computer)

	context = {
		"cart": cart_obj,
		"product_in_cart": product_in_cart,
		"product": accessoire_computer
	}


	return render(request, "products/accessoire_computer_detail.html", context)





