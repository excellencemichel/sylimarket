from io import BytesIO
from email.mime.base import MIMEBase
from email import encoders
from time import strftime
from django.conf import settings
from django.core.mail import EmailMultiAlternatives, EmailMessage


from django.utils.translation import gettext_lazy as _
from django.utils.decorators import method_decorator

from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType

from django.http import JsonResponse
from django.shortcuts import render, redirect



import stripe

STRIPE_SECRET_KEY = getattr(settings, "STRIPE_SECRET_KEY")
STRIPE_PUB_KEY = getattr(settings, "STRIPE_PUB_KEY" )
stripe.api_key = STRIPE_SECRET_KEY



#Local imports
from utils.generator_utils import render_to_pdf

from .models import Cart
from .forms import PayementMethod

from accounts.forms import LoginForm, GuestForm

from orders.models import Order 
from products.models import Product 


from addresses.forms import AddressForm, AddressPayementLivraisonForm
from addresses.models import Address, AddressPayementLivraison

from orders.models import Order, OrderPayementLivraison

from billing.models import BillingProfile, PayementLivraison
# Create your views here.



def payement_method(request):
	form = PayementMethod(request.POST, None)
	login_form 		= LoginForm(request=request)		
	if form.is_valid():
		paymement_choices = form.cleaned_data.get("paymement_choices")
		print("Methode choisie est :", paymement_choices)
		if paymement_choices == "livraison":
			return redirect("carts:checkout_livraison")
		elif paymement_choices == "bancaire":
			return redirect("carts:checkout")

		elif paymement_choices =="mobile":
			return redirect("cats:mobile")
		else:
			return redirect("carts:payement_method")


	context = {
		"form": form,
		"login_form": login_form,
	}



	return render(request, "carts/payement_method.html", context)

def cart_detail_api_view(request):
	cart_obj, new_obj = Cart.objects.new_or_get(request)

	products = [

		{
		"id": x.product.id,
		"url": x.product.get_absolute_url(),
		"name": x.product.name,
		"price" : x.product.price
		}
		for x in cart_obj.items.all()
	]

	cart_data = {
	"products": products, "subtotal": cart_obj.subtotal, "total": cart_obj.total
	}

	return JsonResponse(cart_data)




def cart_home(request):
	cart_obj, new_obj = Cart.objects.new_or_get(request)
	context = {
		"cart": cart_obj,
	}
	return render(request, "carts/home.html", context)



def cart_update(request):
	product_id = request.POST.get("product_id")
	if product_id is not None:
		try:
			product_obj = Product.objects.get(id=product_id)
		except Product.DoesNotExist:
			print("Show message to user, product is gone ?")
			return redirect("carts:home")

		cart_obj, new_obj = Cart.objects.new_or_get(request)
		product_in_cart = cart_obj.cart_item_exists(product_obj)

		if product_in_cart:
			print("Dedans")
			cart_obj.delete_item(product_obj)
			added = False
		else:
			cart_obj.add_item(product_obj)
			print("Pas dedans")
			added = True
			
		request.session["cart_items"] = cart_obj.items.all().count()

		if request.is_ajax():
			print("We are in ajax request")
			json_data = {
			"added": added,
			"removed": not added,
			"cartItemsCount": cart_obj.items.all().count(),
			}
			return JsonResponse(json_data, status=200)
			# return JsonResponse({"message": "Error 404"}, status=404)


	return redirect("carts:home")


  

def checkout_card(request):
	cart_obj, cart_created = Cart.objects.new_or_get(request)
	order_obj = None
	if cart_created or cart_obj.items.all().count() == 0:
		return redirect("carts:home")

	login_form 		= LoginForm(request=request)
	guest_form 		= GuestForm(request.POST or None)
	address_form 	= AddressForm()
	billing_address_id = request.session.get("billing_address_id", None)
	shipping_address_id	= request.session.get("shipping_address_id", None)
	billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(request)
	address_qs = None
	has_card = None
	if billing_profile is not None:
		if request.user.is_authenticated:
			address_qs	= Address.objects.filter(billing_profile=billing_profile)
		order_obj, order_obj_created = Order.objects.new_or_get(billing_profile, cart_obj)
		if shipping_address_id:
			order_obj.shipping_address = Address.objects.get(id=shipping_address_id)
			del request.session["shipping_address_id"]

		if billing_address_id:
			order_obj.billing_address = Address.objects.get(id=billing_address_id)
			del request.session["billing_address_id"]


		if billing_address_id or shipping_address_id:
			order_obj.save()

		has_card = billing_profile.has_card


	if request.method == "POST":
		is_prepared = order_obj.check_done()
		if is_prepared:
			did_charge,charge_msg = billing_profile.charge(order_obj)
			order_obj.mark_paid()
			if did_charge:

				to_email = ["michel37124077@gmail.com",]
				if request.user.is_authenticated:

					to_email.append(request.user.email)

				if guest_form.is_valid():
					guest_address_email = guest_form.cleaned_data.get("email")

					to_email.append(guest_address_email)
					import pdb; pdb.set_trace()

				from_email = settings.EMAIL_HOST_USER

				context_dict = {"models_instance": order_obj}
				context_dict["billing_profile"] = billing_profile
				order_pdf = render_to_pdf("carts/order_pdf.html", context_dict)
				format_filename = """{jour}_{mois}_{annee}_{heure}_{minute}_{seconde}""".format(seconde=strftime("%S"), minute=strftime("%M"), heure=strftime("%H"), mois= strftime("%m"), annee=strftime("%Y"), jour=strftime("%d")) 
				order_obj.order_pdf.save(format_filename, BytesIO(order_pdf.content))

				subject = """SyliMarket, Monsieur Madame voici votre reçu de payement que vous venez d'effectuer chez SyliMarket Les détails sont dans la pièce jointe en PDF """

				with open(settings.BASE_DIR + "/carts/templates/carts/order_email_message.txt") as f:
					order_email_message = f.read()



				order_email_pdf = EmailMessage(

					subject = subject,
					body= order_email_message,
					from_email= from_email,
					to=to_email,
					)


				instance_attach = MIMEBase('application', "octet-stream")
				instance_attach.set_payload(order_obj.order_pdf.read())

				encoders.encode_base64(instance_attach)
				instance_attach.add_header("Content-Disposition", "attachment", filename="SM_{format_filename}.pdf".format(format_filename=format_filename))
				order_email_pdf.attach(instance_attach)

				order_email_pdf.send()


				request.session["cart_items"] = 0
				del request.session["cart_id"]
				if not billing_profile.user:
					billing_profile.set_cards_inactive()
				return redirect ("carts:success")

			else:
				print(charge_msg)
				return redirect("carts:checkout")

	context = {
		"object": order_obj,
		"billing_profile": billing_profile,
		"login_form": login_form,
		"guest_form": guest_form,
		"address_form" : address_form,
		"address_qs": address_qs,
		"has_card": has_card,
		"publish_key": STRIPE_PUB_KEY,


	}
	return render(request, "carts/checkout.html", context)



@login_required
def checkout_livraison(request):
	cart_obj, cart_created = Cart.objects.new_or_get(request)
	order_obj = None
	if cart_created or cart_obj.items.all().count() == 0:
		return redirect("carts:home")

	address_payement_livraison_form 				= AddressPayementLivraisonForm()
	facturation_address_id							= request.session.get("facturation_address_id", None)
	livraison_address_id							= request.session.get("livraison_address_id", None)
	payement_livraison, payement_livraison_created 	= PayementLivraison.objects.new_or_get(request)
	address_payement_livraison_qs = None
	if payement_livraison is not None:
		if request.user.is_authenticated:
			address_payement_livraison_qs	= AddressPayementLivraison.objects.filter(payement_livraison=payement_livraison).distinct("ville")
		order_obj, order_obj_created = OrderPayementLivraison.objects.new_or_get(payement_livraison, cart_obj)
		if livraison_address_id:
			order_obj.livraison_address = AddressPayementLivraison.objects.get(id=livraison_address_id)
			del request.session["livraison_address_id"]

		if facturation_address_id:
			order_obj.facturation_address = AddressPayementLivraison.objects.get(id=facturation_address_id)
			del request.session["facturation_address_id"]


		if facturation_address_id or livraison_address_id:
			order_obj.save()

	if request.method == "POST":
		is_prepared = order_obj.check_done()
		if is_prepared:
			order_obj.mark_paid()

			to_email = ["sylimarket@gmail.com",]
			if request.user.is_authenticated:

				to_email.append(request.user.email)

			from_email = settings.EMAIL_HOST_USER

			context_dict = {"models_instance": order_obj}
			context_dict["payement_livraison"] = payement_livraison
			order_payement_livraison_pdf = render_to_pdf("carts/order_payement_livraison_pdf.html", context_dict)
			format_filename = """{jour}_{mois}_{annee}_{heure}_{minute}_{seconde}""".format(seconde=strftime("%S"), minute=strftime("%M"), heure=strftime("%H"), mois= strftime("%m"), annee=strftime("%Y"), jour=strftime("%d")) 
			order_obj.order_payement_livraison_pdf.save(format_filename, BytesIO(order_payement_livraison_pdf.content))

			subject = """SyliMarket, Monsieur Madame voici votre reçu de payement que vous venez d'effectuer chez SyliMarket Les détails sont dans la pièce jointe en PDF"""

			with open(settings.BASE_DIR + "/carts/templates/carts/order_email_message.txt") as f:
				order_email_message = f.read()



			order_payement_livraison_email_pdf = EmailMessage(

				subject = subject,
				body= order_email_message,
				from_email= from_email,
				to=to_email,
				)


			instance_attach = MIMEBase('application', "octet-stream")
			instance_attach.set_payload(order_obj.order_payement_livraison_pdf.read())

			encoders.encode_base64(instance_attach)
			instance_attach.add_header("Content-Disposition", "attachment", filename="SM_{format_filename}.pdf".format(format_filename=format_filename))
			order_payement_livraison_email_pdf.attach(instance_attach)

			order_payement_livraison_email_pdf.send()


			request.session["cart_items"] = 0
			del request.session["cart_id"]
			return redirect ("carts:success")

		else:
			return redirect("carts:checkout_livraison")

	context = {
		"object": order_obj,
		"payement_livraison": payement_livraison,
		"address_payement_livraison_form" : address_payement_livraison_form,
		"address_payement_livraison_qs": address_payement_livraison_qs,


	}
	return render(request, "carts/checkout_livraison.html", context)



def checkout_mobile(request):
	context = {}

	return render(request, "carts/checkout_mobile.html", context)


def checkout_done_view(request):
	context = {}
	return render(request, "carts/checkout_done.html", context)
