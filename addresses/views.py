from django.utils.http import is_safe_url

from django.shortcuts import render, redirect

from .forms import AddressForm, AddressPayementLivraisonForm
from .models import Address, AddressPayementLivraison

from billing.models import BillingProfile, PayementLivraison

# Create your views here.



def checkout_address_create_view(request):
	form = AddressForm(request.POST or None)
	context = {
		"form": form
	}

	next_ = request.GET.get("next")
	next_post	= request.POST.get("next")
	redirect_path	= next_ or next_post or None
	if form.is_valid():
		instance = form.save(commit=False)
		billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(request)
		if billing_profile is not None:
			address_type	= request.POST.get("address_type", "shipping")
			instance.billing_profile = billing_profile
			instance.address_type	= address_type
			instance.save()

			request.session[address_type + "_address_id"] = instance.id 
			

		else:
			return redirect("carts:checkout")
		if is_safe_url(redirect_path, request.get_host()):
			return redirect(redirect_path)

	return redirect("carts:checkout")





def checkout_address_use_view(request):
	if request.user.is_authenticated:
		
		context = {}

		next_ = request.GET.get("next")
		next_post	= request.POST.get("next")
		redirect_path	= next_ or next_post or None

		if request.method == "POST":
			shipping_address	=	request.POST.get("shipping_address", None)
			address_type	= request.POST.get("address_type", "shipping")
			billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(request)
			if shipping_address is not None:
				qs	=	Address.objects.filter(billing_profile=billing_profile, id=shipping_address)
				if qs.exists():
					request.session[address_type + "_address_id"] =  shipping_address
			
				if is_safe_url(redirect_path, request.get_host()):
					return redirect(redirect_path)

	return redirect("carts:checkout")



###################"" Payement à la livraison ""#####################################


def checkout_address_livraison_create_view(request):
	form = AddressPayementLivraisonForm(request.POST or None)
	context = {
		"form": form
	}

	next_ = request.GET.get("next")
	next_post	= request.POST.get("next")
	redirect_path	= next_ or next_post or None
	if form.is_valid():
		instance = form.save(commit=False)
		payement_livraison, payement_livraison_created = PayementLivraison.objects.new_or_get(request)
		if payement_livraison is not None:
			address_payement_livraison_type	= request.POST.get("address_payement_livraison_type", "livraison")
			instance.payement_livraison = payement_livraison
			instance.address_payement_livraison_type	= address_payement_livraison_type
			instance.save()

			request.session[address_payement_livraison_type + "_address_id"] = instance.id 
			

		else:
			return redirect("carts:checkout_livraison")
		if is_safe_url(redirect_path, request.get_host()):
			return redirect(redirect_path)

	return redirect("carts:checkout_livraison")




def checkout_address_livraison_use_view(request):
	if request.user.is_authenticated:
		
		context = {}

		next_ = request.GET.get("next")
		next_post	= request.POST.get("next")
		redirect_path	= next_ or next_post or None

		if request.method == "POST":
			adresse_livraison	=	request.POST.get("adresse_livraison", None)
			address_payement_livraison_type	= request.POST.get("address_payement_livraison_type", "livraison")
			payement_livraison, payement_livraison_created = PayementLivraison.objects.new_or_get(request)
			if adresse_livraison is not None:
				qs	=	AddressPayementLivraison.objects.filter(payement_livraison=payement_livraison, id=adresse_livraison)
				if qs.exists():
					request.session[address_payement_livraison_type + "_address_id"] =  adresse_livraison
			
				if is_safe_url(redirect_path, request.get_host()):
					return redirect(redirect_path)

	return redirect("carts:checkout_livraison")