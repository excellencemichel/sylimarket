from itertools import chain


from django.shortcuts import render
from django.db.models import Q
from django.views.generic import ListView



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


# from products.models import Product
from carts.models import Cart 
# Create your views here.



class SearchProductView(ListView):
	# queryset = Product.objects.all()
	template_name = "search/view.html"


	def get_context_data(self, *args, **kwargs):
		context = super(SearchProductView, self).get_context_data(*args, **kwargs)
		context["query"] = self.request.GET.get("q")
		cart_obj, new_obj = Cart.objects.new_or_get(self.request)
		context["cart"] = cart_obj

		return context



	def get_queryset(self, *args, **kwargs):
		"""
		__icontains = field contains this: Si le champ contient le mot
		__iexact = field is exactly this: Si le champ contient exactement le mot

		"""
		request = self.request
		method_dict = request.GET
		query = method_dict.get("q", None)
		if query is not None:
			q_menclothing = MenClothing.objects.search(query)
			q_womenclothing = WomenClothing.objects.search(query)
			q_pantalon = Pantalon.objects.search(query)
			q_culotte = Culotte.objects.search(query)
			q_jupe = Jupe.objects.search(query)
			q_menshoes = MenShoes.objects.search(query)
			q_womenshoes = WomenShoes.objects.search(query)
			q_accessoire_clothing = AccessoireClothng.objects.search(query)
			q_cumputer = Computer.objects.search(query)
			q_accessoire_computer = AccessoireComputer.objects.search(query)
			q_phone = Phone.objects.search(query)
			q_tablette = Tablette.objects.search(query)
			q_accessoire_phone = AccessoirePhone.objects.search(query)

			product_list = sorted(
        		chain(q_menclothing,
				q_womenclothing, q_pantalon, q_culotte, q_jupe,
				q_menshoes, q_womenshoes, q_accessoire_clothing,
				q_cumputer, q_accessoire_computer,
				q_phone, q_tablette, q_accessoire_phone
				),
        		key=lambda product: product.updated, reverse=True
        		)

			return product_list

		return 

