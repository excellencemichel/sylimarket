
from django.conf import settings

from django.http import Http404, HttpResponse, HttpResponseRedirect

from django.views.generic import ListView, View, DetailView

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy


from django.utils.decorators import method_decorator
from django.utils.translation import gettext_lazy as _



from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.db.models import Q




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









class MenClothingListView(ListView):
	template_name = "products/men_clothing_list.html"

	def get_context_data(self, *args, **kwargs):
		context = super(MenClothingListView,self).get_context_data(*args, **kwargs)
		cart_obj, new_obj = Cart.objects.new_or_get(self.request)
		context["cart"] = cart_obj
		return context



	def get_queryset(self, *args, **kwargs):
		request = self.request
		return Product.objects.get_men_clothings()



		










class WomenClothingListView(ListView):
	template_name = "products/women_clothing_list.html"

	def get_context_data(self, *args, **kwargs):
		context = super(WomenClothingListView,self).get_context_data(*args, **kwargs)
		cart_obj, new_obj = Cart.objects.new_or_get(self.request)
		context["cart"] = cart_obj
		return context



	def get_queryset(self, *args, **kwargs):
		request = self.request
		return Product.objects.get_women_clothings()



		







class PantalonListView(ListView):
	template_name = "products/pantalon_list.html"

	def get_context_data(self, *args, **kwargs):
		context = super(PantalonListView,self).get_context_data(*args, **kwargs)
		cart_obj, new_obj = Cart.objects.new_or_get(self.request)
		context["cart"] = cart_obj
		return context



	def get_queryset(self, *args, **kwargs):
		request = self.request
		return Product.objects.get_pantalons()



		







class CulotteListView(ListView):
	template_name = "products/culotte_list.html"

	def get_context_data(self, *args, **kwargs):
		context = super(CulotteListView,self).get_context_data(*args, **kwargs)
		cart_obj, new_obj = Cart.objects.new_or_get(self.request)
		context["cart"] = cart_obj
		return context



	def get_queryset(self, *args, **kwargs):
		request = self.request
		return Product.objects.get_culottes()



		







class JupeListView(ListView):
	template_name = "products/jupe_list.html"

	def get_context_data(self, *args, **kwargs):
		context = super(JupeListView,self).get_context_data(*args, **kwargs)
		cart_obj, new_obj = Cart.objects.new_or_get(self.request)
		context["cart"] = cart_obj
		return context



	def get_queryset(self, *args, **kwargs):
		request = self.request
		return Product.objects.get_jupes()



		







class MenShoesListView(ListView):
	template_name = "products/men_shoes_list.html"

	def get_context_data(self, *args, **kwargs):
		context = super(MenShoesListView,self).get_context_data(*args, **kwargs)
		cart_obj, new_obj = Cart.objects.new_or_get(self.request)
		context["cart"] = cart_obj
		return context



	def get_queryset(self, *args, **kwargs):
		request = self.request
		return Product.objects.get_men_shoes()



		







class WomenShoesListView(ListView):
	template_name = "products/women_shoes_list.html"

	def get_context_data(self, *args, **kwargs):
		context = super(WomenShoesListView,self).get_context_data(*args, **kwargs)
		cart_obj, new_obj = Cart.objects.new_or_get(self.request)
		context["cart"] = cart_obj
		return context



	def get_queryset(self, *args, **kwargs):
		request = self.request
		return Product.objects.get_women_shoes()



		







class AccessoireClothngListView(ListView):
	template_name = "products/accessoireclothing_list.html"

	def get_context_data(self, *args, **kwargs):
		context = super(AccessoireClothngListView,self).get_context_data(*args, **kwargs)
		cart_obj, new_obj = Cart.objects.new_or_get(self.request)
		context["cart"] = cart_obj
		return context



	def get_queryset(self, *args, **kwargs):
		request = self.request
		return Product.objects.get_clothing_accessoires()







class ComputerListView(ListView):
	template_name = "products/computer_list.html"

	def get_context_data(self, *args, **kwargs):
		context = super(ComputerListView,self).get_context_data(*args, **kwargs)
		cart_obj, new_obj = Cart.objects.new_or_get(self.request)
		context["cart"] = cart_obj
		return context



	def get_queryset(self, *args, **kwargs):
		request = self.request
		return Product.objects.get_computers()



		







class AccessoireComputerListView(ListView):
	template_name = "products/accessoire_computer_list.html"

	def get_context_data(self, *args, **kwargs):
		context = super(AccessoireComputerListView,self).get_context_data(*args, **kwargs)
		cart_obj, new_obj = Cart.objects.new_or_get(self.request)
		context["cart"] = cart_obj
		return context



	def get_queryset(self, *args, **kwargs):
		request = self.request
		return Product.objects.get_computer_accessoires()



		







class PhoneListView(ListView):
	template_name = "products/phone_list.html"

	def get_context_data(self, *args, **kwargs):
		context = super(PhoneListView,self).get_context_data(*args, **kwargs)
		cart_obj, new_obj = Cart.objects.new_or_get(self.request)
		context["cart"] = cart_obj
		return context



	def get_queryset(self, *args, **kwargs):
		request = self.request
		return Product.objects.get_phones()



		







class TabletteListView(ListView):
	template_name = "products/tablette_list.html"

	def get_context_data(self, *args, **kwargs):
		context = super(TabletteListView,self).get_context_data(*args, **kwargs)
		cart_obj, new_obj = Cart.objects.new_or_get(self.request)
		context["cart"] = cart_obj
		return context



	def get_queryset(self, *args, **kwargs):
		request = self.request
		return Product.objects.get_tablettes()



		







class AccessoirePhoneListView(ListView):
	template_name = "products/accessoire_phone_list.html"

	def get_context_data(self, *args, **kwargs):
		context = super(AccessoirePhoneListView,self).get_context_data(*args, **kwargs)
		cart_obj, new_obj = Cart.objects.new_or_get(self.request)
		context["cart"] = cart_obj
		return context



	def get_queryset(self, *args, **kwargs):
		request = self.request
		return Product.objects.get_phone_accessoires()



		


def men_clothing_detail(request, pk=None, slug=None, *args, **kwargs):
	print("Men clothing detail appélé")
	product = get_object_or_404(Product, pk=pk, slug=slug)
	cart_obj, new_obj = Cart.objects.new_or_get(request)
	try:
		men_clothing = MenClothing.objects.get(product_id = product.id)
	except MenClothing.MultipleObjectsReturned:
		men_clothing = MenClothing.objects.filter(product_id=product.id).first()

	except MenClothing.DoesNotExist:
		pass

	except:
		print("Autre erreur non lié à la laison")

	if product:
		object_viewed_signal.send(product.__class__, instance=product, request=request)


	if product in cart_obj.products.all():
		quantite = cart_obj.quantite[str(product.id)]

	else:
		quantite = "1"


	if request.user.is_authenticated:
		views 	= request.user.objectviewed_set.by_model(Product, model_queryset=True).exclude(id=product.id) #all().filter(content_type__name="product"), l'exclude permet d'enlever les produit encours puisque de toutes les façons il est déjà afficher
	else:
		views = None




	context = {
		"cart": cart_obj,
		"product": product,
		"men_clothing": men_clothing,
		"views": views,
		"quantite": quantite


	}


	return render(request, "products/men_clothing_detail.html", context)





def women_clothing_detail(request, pk=None, slug=None, *args, **kwargs):
	product = get_object_or_404(Product, pk=pk, slug=slug)
	cart_obj, new_obj = Cart.objects.new_or_get(request)
	try:
		women_clothing = WomenClothing.objects.get(product_id = product.id)

	except WomenClothing.MultipleObjectsReturned:
		women_clothing = WomenClothing.objects.filter(product_id=product.id).first()

	except WomenClothing.DoesNotExist:
		pass

	except:
		print("Autre erreur non liée à la laison")

	if product:
		object_viewed_signal.send(product.__class__, instance=product, request=request)


	if product in cart_obj.products.all():
		quantite = cart_obj.quantite[str(product.id)]

	else:
		quantite = "1"


	if request.user.is_authenticated:
		views 	= request.user.objectviewed_set.by_model(Product, model_queryset=True).exclude(id=product.id) #all().filter(content_type__name="product"), l'exclude permet d'enlever les produit encours puisque de toutes les façons il est déjà afficher
	else:
		views = None


	context = {
		"cart": cart_obj,
		"product": product,
		"women_clothing" : women_clothing,
		"quantite": quantite,
		"views": views,

	}


	return render(request, "products/women_clothing_detail.html", context)




def accessoire_clothing_detail(request, pk=None, slug=None, *args, **kwargs):
	product = get_object_or_404(Product, pk=pk, slug=slug)
	cart_obj, new_obj = Cart.objects.new_or_get(request)
	try:
		accessoire_clothing = AccessoireClothng.objects.get(product_id = product.id)
	except AccessoireClothng.MultipleObjectsReturned:
		accessoire_clothing = AccessoireClothng.objects.filter(product_id=product.id).first()

	except AccessoireClothng.DoesNotExist:
		pass

	except:
		print("Autre erreur non liée à la laison")

	if product:
		object_viewed_signal.send(product.__class__, instance=product, request=request)


	if product in cart_obj.products.all():
		quantite = cart_obj.quantite[str(product.id)]

	else:
		quantite = "1"


	if request.user.is_authenticated:
		views 	= request.user.objectviewed_set.by_model(Product, model_queryset=True).exclude(id=product.id) #all().filter(content_type__name="product"), l'exclude permet d'enlever les produit encours puisque de toutes les façons il est déjà afficher
	else:
		views = None



	context = {
		"cart": cart_obj,
		"product": product,
		"accessoire_clothing" : accessoire_clothing,
		"quantite": quantite,
		"views": views,

	}


	return render(request, "products/accessoire_clothing_detail.html", context)





def men_shoe_detail(request, pk=None, slug=None, *args, **kwargs):
	product = get_object_or_404(Product, pk=pk, slug=slug)
	cart_obj, new_obj = Cart.objects.new_or_get(request)
	try:
		men_shoe = MenShoes.objects.get(product_id = product.id)
	except MenShoes.MultipleObjectsReturned:
		men_shoe = MenShoes.objects.filter(product_id=product.id).first()

	except MenShoes.DoesNotExist:
		pass

	except:
		print("Autre erreur non liée à la laison")

	if product:
		object_viewed_signal.send(product.__class__, instance=product, request=request)


	if product in cart_obj.products.all():
		quantite = cart_obj.quantite[str(product.id)]

	else:
		quantite = "1"


	if request.user.is_authenticated:
		views 	= request.user.objectviewed_set.by_model(Product, model_queryset=True).exclude(id=product.id) #all().filter(content_type__name="product"), l'exclude permet d'enlever les produit encours puisque de toutes les façons il est déjà afficher
	else:
		views = None



	context = {
		"cart": cart_obj,
		"product": product,
		"men_shoe": men_shoe,
		"quantite": quantite,
		"views": views,

	}


	return render(request, "products/men_shoe_detail.html", context)




def women_shoe_detail(request, pk=None, slug=None, *args, **kwargs):
	product = get_object_or_404(Product, pk=pk, slug=slug)
	cart_obj, new_obj = Cart.objects.new_or_get(request)
	try:
		women_sheo = WomenShoes.objects.get(product_id = product.id)
	except WomenShoes.MultipleObjectsReturned:
		women_sheo = WomenShoes.objects.filter(product_id=product.id).first()

	except WomenShoes.DoesNotExist:
		pass

	except:
		print("Autre erreur non liée à la laison")

	if product:
		object_viewed_signal.send(product.__class__, instance=product, request=request)


	if product in cart_obj.products.all():
		quantite = cart_obj.quantite[str(product.id)]

	else:
		quantite = "1"


	if request.user.is_authenticated:
		views 	= request.user.objectviewed_set.by_model(Product, model_queryset=True).exclude(id=product.id) #all().filter(content_type__name="product"), l'exclude permet d'enlever les produit encours puisque de toutes les façons il est déjà afficher
	else:
		views = None



	context = {
		"cart": cart_obj,
		"product": product,
		"women_sheo" : women_sheo,
		"quantite": quantite,
		"views": views,

	}


	return render(request, "products/women_shoe_detail.html", context)





def patalon_detail(request, pk=None, slug=None, *args, **kwargs):
	product = get_object_or_404(Product, pk=pk, slug=slug)
	cart_obj, new_obj = Cart.objects.new_or_get(request)
	try:
		pantalon = Pantalon.objects.get(product_id = product.id)
	except Pantalon.MultipleObjectsReturned:
		pantalon = Pantalon.objects.filter(product_id=product.id).first()

	except Pantalon.DoesNotExist:
		pass

	except:
		print("Autre erreur non liée à la laison")

	if product:
		object_viewed_signal.send(product.__class__, instance=product, request=request)


	if product in cart_obj.products.all():
		quantite = cart_obj.quantite[str(product.id)]

	else:
		quantite = "1"


	if request.user.is_authenticated:
		views 	= request.user.objectviewed_set.by_model(Product, model_queryset=True).exclude(id=product.id) #all().filter(content_type__name="product"), l'exclude permet d'enlever les produit encours puisque de toutes les façons il est déjà afficher
	else:
		views = None



	context = {
		"cart": cart_obj,
		"product": product,
		"pantalon" : pantalon,
		"quantite": quantite,
		"views": views,

	}


	return render(request, "products/pantalon_detail.html", context)



def culotte_detail(request, pk=None, slug=None, *args, **kwargs):
	product = get_object_or_404(Product, slug=slug)
	cart_obj, new_obj = Cart.objects.new_or_get(request)
	quantite = None
	try:
		culotte = Culotte.objects.get(product_id = product.id)

	except Culotte.MultipleObjectsReturned:
		culotte = Culotte.objects.filter(product_id=product.id).first()
	except Culotte.DoesNotExist:
		pass
	except:
		print("Autre erreur non liée à la laison")

	if product:
		object_viewed_signal.send(product.__class__, instance=product, request=request)

	if product in cart_obj.products.all():
		quantite = cart_obj.quantite[str(product.id)]

	else:
		quantite = "1"


	if request.user.is_authenticated:
		views 	= request.user.objectviewed_set.by_model(Product, model_queryset=True).exclude(id=product.id) #all().filter(content_type__name="product"), l'exclude permet d'enlever les produit encours puisque de toutes les façons il est déjà afficher
	else:
		views = None



	context = {
		"cart": cart_obj,
		"product": product,
		"culotte" : culotte,
		"quantite": quantite,
		"views": views,
	}


	return render(request, "products/culotte_detail.html", context)



def jupe_detail(request, pk=None, slug=None, *args, **kwargs):
	product = Product.objects.get(pk=pk, slug=slug)
	cart_obj, new_obj = Cart.objects.new_or_get(request)
	try:
		jupe = Jupe.objects.get(product_id=product.id)
	except Jupe.MultipleObjectsReturned:
		jupe = Jupe.objects.filter(product_id=product.id).first()
	except Jupe.DoesNotExist:
		pass
	except:
		print("Autre erreur non liée à laison")

	if product:
		object_viewed_signal.send(product.__class__, instance=product, request=request)

	if product in cart_obj.products.all():
		quantite = cart_obj.quantite[str(product.id)]
		stock_list = range(product.stock)

	else:
		quantite = "1"
		stock_list = range(1)




	if request.user.is_authenticated:
		views 	= request.user.objectviewed_set.by_model(Product, model_queryset=True).exclude(id=product.id) #all().filter(content_type__name="product"), l'exclude permet d'enlever les produit encours puisque de toutes les façons il est déjà afficher
	else:
		views = None



	print("Le panier", cart_obj.quantite)
	context = {
		"cart": cart_obj,
		"product": product,
		"jupe" :jupe,
		"quantite" :quantite,
		"views": views,
		"stock_list": stock_list,

	}


	return render(request, "products/jupe_detail.html", context)



def phone_detail(request, pk=None, slug=None, *args, **kwargs):
	product = get_object_or_404(Product, pk=pk, slug=slug)
	cart_obj, new_obj = Cart.objects.new_or_get(request)
	try:
		phone = Phone.objects.get(product_id = product.id)

	except Phone.MultipleObjectsReturned:
		phone = Phone.objects.filter(product_id=product.id).first()

	except Phone.DoesNotExist:
		pass

	except:
		print("Autre erreur non liée à la laison")

	if product:
		object_viewed_signal.send(product.__class__, instance=product, request=request)


	if product in cart_obj.products.all():
		quantite = cart_obj.quantite[str(product.id)]

	else:
		quantite = "1"


	if request.user.is_authenticated:
		views 	= request.user.objectviewed_set.by_model(Product, model_queryset=True).exclude(id=product.id) #all().filter(content_type__name="product"), l'exclude permet d'enlever les produit encours puisque de toutes les façons il est déjà afficher
	else:
		views = None



	context = {
		"cart": cart_obj,
		"product": product,
		"phone": phone,
		"quantite": quantite,
		"views": views,

	}


	return render(request, "products/phone_detail.html", context)





def tablette_detail(request, pk=None, slug=None, *args, **kwargs):
	product = get_object_or_404(Product, pk=pk, slug=slug)
	cart_obj, new_obj = Cart.objects.new_or_get(request)
	try:
		tablette = Tablette.objects.get(product_id = product.id)
	except Tablette.MultipleObjectsReturned:
		tablette = Tablette.objects.filter(product_id=product.id).first()

	except Tablette.DoesNotExist:
		pass

	except:
		print("Autre erreur non lié à la laison")

	if product:
		object_viewed_signal.send(product.__class__, instance=product, request=request)


	if product in cart_obj.products.all():
		quantite = cart_obj.quantite[str(product.id)]

	else:
		quantite = "1"


	if request.user.is_authenticated:
		views 	= request.user.objectviewed_set.by_model(Product, model_queryset=True).exclude(id=product.id) #all().filter(content_type__name="product"), l'exclude permet d'enlever les produit encours puisque de toutes les façons il est déjà afficher
	else:
		views = None



	context = {
		"cart": cart_obj,
		"product": product,
		"tablette" :tablette,
		"quantite": quantite,
		"views": views,

	}


	return render(request, "products/tablette_detail.html", context)







def accessoire_phone_detail(request, pk=None, slug=None, *args, **kwargs):
	print("Phone accessoire detail appélé")
	product = get_object_or_404(Product, pk=pk, slug=slug)
	cart_obj, new_obj = Cart.objects.new_or_get(request)
	try:
		accessoire_phone = AccessoirePhone.objects.get(product_id = product.id)

	except AccessoirePhone.MultipleObjectsReturned:
		accessoire_phone = AccessoirePhone.objects.filter(product_id=product.id).first()

	except AccessoirePhone.DoesNotExist:
		pass

	except:
		print("Autre erreur non liée à la laison")

	if product:
		object_viewed_signal.send(product.__class__, instance=product, request=request)


	if product in cart_obj.products.all():
		quantite = cart_obj.quantite[str(product.id)]

	else:
		quantite = "1"


	if request.user.is_authenticated:
		views 	= request.user.objectviewed_set.by_model(Product, model_queryset=True).exclude(id=product.id) #all().filter(content_type__name="product"), l'exclude permet d'enlever les produit encours puisque de toutes les façons il est déjà afficher
	else:
		views = None



	context = {
		"cart": cart_obj,
		"product": product,
		"accessoire_phone" : accessoire_phone,
		"quantite": quantite,
		"views": views,

	}


	return render(request, "products/accessoire_phone_detail.html", context)









def computer_detail(request, pk=None, slug=None, *args, **kwargs):
	product = get_object_or_404(Product, pk=pk, slug=slug)
	cart_obj, new_obj = Cart.objects.new_or_get(request)
	try:
		computer = Computer.objects.get(product_id = product.id)

	except Computer.MultipleObjectsReturned:
		computer = Computer.objects.filter(product_id=product.id).first()

	except Computer.DoesNotExist:
		pass

	except:
		prin("Autre erreur non lié à la laison")

	if product:
		object_viewed_signal.send(product.__class__, instance=product, request=request)


	if product in cart_obj.products.all():
		quantite = cart_obj.quantite[str(product.id)]

	else:
		quantite = "1"


	if request.user.is_authenticated:
		views 	= request.user.objectviewed_set.by_model(Product, model_queryset=True).exclude(id=product.id) #all().filter(content_type__name="product"), l'exclude permet d'enlever les produit encours puisque de toutes les façons il est déjà afficher
	else:
		views = None



	context = {
		"cart": cart_obj,
		"product": product,
		"computer": computer,
		"quantite": quantite,
		"views": views,

	}


	return render(request, "products/computer_detail.html", context)









def accessoire_computer_detail(request, pk=None, slug=None, *args, **kwargs):
	product = get_object_or_404(Product, pk=pk, slug=slug)
	cart_obj, new_obj = Cart.objects.new_or_get(request)
	try:
		accessoire_computer = AccessoireComputer.objects.get(product_id = product.id)

	except AccessoireComputer.MultipleObjectsReturned:
		accessoire_computer = AccessoireComputer.objects.filter(product_id=product.id).first()

	except AccessoireComputer.DoesNotExist:
		pass

	except:
		print("Autre erreur non liée à la laison")

	if product:
		object_viewed_signal.send(product.__class__, instance=product, request=request)


	if product in cart_obj.products.all():
		quantite = cart_obj.quantite[str(product.id)]

	else:
		quantite = "1"


	if request.user.is_authenticated:
		views 	= request.user.objectviewed_set.by_model(Product, model_queryset=True).exclude(id=product.id) #all().filter(content_type__name="product"), l'exclude permet d'enlever les produit encours puisque de toutes les façons il est déjà afficher
	else:
		views = None



	context = {
		"cart": cart_obj,
		"product": product,
		"accessoire_computer" :accessoire_computer,
		"quantite": quantite,
		"views": views,

	}


	return render(request, "products/accessoire_cumputer_detail.html", context)








class SamsungMarqueListView(ListView):
	template_name = "products/samsung_list.html"

	def get_context_data(self, *args, **kwargs):
		context = super(SamsungMarqueListView,self).get_context_data(*args, **kwargs)
		cart_obj, new_obj = Cart.objects.new_or_get(self.request)
		context["cart"] = cart_obj
		return context



	def get_queryset(self, *args, **kwargs):
		request = self.request
		return Product.objects.marquelist("Samsung")


class AdidasMarqueListView(ListView):
	template_name = "products/adidas_list.html"

	def get_context_data(self, *args, **kwargs):
		context = super(SamsungMarqueListView,self).get_context_data(*args, **kwargs)
		cart_obj, new_obj = Cart.objects.new_or_get(self.request)
		context["cart"] = cart_obj
		return context



	def get_queryset(self, *args, **kwargs):
		request = self.request
		return Product.objects.marquelist("Adidas")



class LGMarqueListView(ListView):
	template_name = "products/lg_list.html"

	def get_context_data(self, *args, **kwargs):
		context = super(SamsungMarqueListView,self).get_context_data(*args, **kwargs)
		cart_obj, new_obj = Cart.objects.new_or_get(self.request)
		context["cart"] = cart_obj
		return context



	def get_queryset(self, *args, **kwargs):
		request = self.request
		return Product.objects.marquelist("LG")




class AppleMarqueListView(ListView):
	template_name = "products/apple_list.html"

	def get_context_data(self, *args, **kwargs):
		context = super(SamsungMarqueListView,self).get_context_data(*args, **kwargs)
		cart_obj, new_obj = Cart.objects.new_or_get(self.request)
		context["cart"] = cart_obj
		return context



	def get_queryset(self, *args, **kwargs):
		request = self.request
		return Product.objects.marquelist("Apple")





class NikeMarqueListView(ListView):
	template_name = "products/nike_list.html"

	def get_context_data(self, *args, **kwargs):
		context = super(SamsungMarqueListView,self).get_context_data(*args, **kwargs)
		cart_obj, new_obj = Cart.objects.new_or_get(self.request)
		context["cart"] = cart_obj
		return context



	def get_queryset(self, *args, **kwargs):
		request = self.request
		return Product.objects.marquelist("Nike")



class SonyMarqueListView(ListView):
	template_name = "products/sony_list.html"

	def get_context_data(self, *args, **kwargs):
		context = super(SamsungMarqueListView,self).get_context_data(*args, **kwargs)
		cart_obj, new_obj = Cart.objects.new_or_get(self.request)
		context["cart"] = cart_obj
		return context



	def get_queryset(self, *args, **kwargs):
		request = self.request
		return Product.objects.marquelist("Sony")




class ItelMarqueListView(ListView):
	template_name = "products/itel_list.html"

	def get_context_data(self, *args, **kwargs):
		context = super(SamsungMarqueListView,self).get_context_data(*args, **kwargs)
		cart_obj, new_obj = Cart.objects.new_or_get(self.request)
		context["cart"] = cart_obj
		return context



	def get_queryset(self, *args, **kwargs):
		request = self.request
		return Product.objects.marquelist("Itel")



class TommyMarqueListView(ListView):
	template_name = "products/tommy_list.html"

	def get_context_data(self, *args, **kwargs):
		context = super(SamsungMarqueListView,self).get_context_data(*args, **kwargs)
		cart_obj, new_obj = Cart.objects.new_or_get(self.request)
		context["cart"] = cart_obj
		return context



	def get_queryset(self, *args, **kwargs):
		request = self.request
		return Product.objects.marquelist("Tommy")



class WhirlPoolMarqueListView(ListView):
	template_name = "products/whirlpool_list.html"

	def get_context_data(self, *args, **kwargs):
		context = super(SamsungMarqueListView,self).get_context_data(*args, **kwargs)
		cart_obj, new_obj = Cart.objects.new_or_get(self.request)
		context["cart"] = cart_obj
		return context



	def get_queryset(self, *args, **kwargs):
		request = self.request
		return Product.objects.marquelist("Whirlpool")



class AccentListView(ListView):
	template_name = "products/accent_list.html"

	def get_context_data(self, *args, **kwargs):
		context = super(SamsungMarqueListView,self).get_context_data(*args, **kwargs)
		cart_obj, new_obj = Cart.objects.new_or_get(self.request)
		context["cart"] = cart_obj
		return context



	def get_queryset(self, *args, **kwargs):
		request = self.request
		return Product.objects.marquelist("Accent")



class LorealMarqueListView(ListView):
	template_name = "products/loreal_list.html"

	def get_context_data(self, *args, **kwargs):
		context = super(SamsungMarqueListView,self).get_context_data(*args, **kwargs)
		cart_obj, new_obj = Cart.objects.new_or_get(self.request)
		context["cart"] = cart_obj
		return context



	def get_queryset(self, *args, **kwargs):
		request = self.request
		return Product.objects.marquelist("Loreal")




class OppoMarqueListView(ListView):
	template_name = "products/oppo_list.html"

	def get_context_data(self, *args, **kwargs):
		context = super(SamsungMarqueListView,self).get_context_data(*args, **kwargs)
		cart_obj, new_obj = Cart.objects.new_or_get(self.request)
		context["cart"] = cart_obj
		return context



	def get_queryset(self, *args, **kwargs):
		request = self.request
		return Product.objects.marquelist("oppo")



class HuaweiMarqueListView(ListView):
	template_name = "products/huawei_list.html"

	def get_context_data(self, *args, **kwargs):
		context = super(SamsungMarqueListView,self).get_context_data(*args, **kwargs)
		cart_obj, new_obj = Cart.objects.new_or_get(self.request)
		context["cart"] = cart_obj
		return context



	def get_queryset(self, *args, **kwargs):
		request = self.request
		return Product.objects.marquelist("Huawei")
