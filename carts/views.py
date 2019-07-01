from io import BytesIO
from email.mime.base import MIMEBase
from email import encoders
from time import strftime
from decimal import Decimal 


from django.conf import settings
from django.core.mail import EmailMultiAlternatives, EmailMessage


from django.utils.translation import gettext_lazy as _
from django.utils.decorators import method_decorator

from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from django.contrib import messages

from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy




import stripe

STRIPE_SECRET_KEY = getattr(settings, "STRIPE_SECRET_KEY")
STRIPE_PUB_KEY = getattr(settings, "STRIPE_PUB_KEY" )
stripe.api_key = STRIPE_SECRET_KEY



#Local imports
from utils.generator_utils import render_to_pdf
from utils.decimal_utils import TWOPLACES

from analytics.signals import product_purshase_create_signal


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

		elif paymement_choices == "mobile":
			return redirect("carts:mobile")
		else:
			return redirect("carts:payement_method")


	context = { "form": form,
	"login_form" : login_form
	}


	return render(request, "carts/payement_method.html", context)

def cart_detail_api_view(request):
	cart_obj, new_obj = Cart.objects.new_or_get(request)
	products = [
			
			{
			"id": x.id,
			"url": x.get_absolute_url(),
			"name": x.name,
			 "price":x.price,
			 "taxe": x.taxe,
			 "subtotal": x.subtotal,
			 "image": x.image.url
			 } 
			 for x in cart_obj.products.all()] # [<object>, <object>, <object>]

	cart_data = {
		"products": products, "quantite": cart_obj.quantite, "subtotal":cart_obj.subtotal, "taxe": cart_obj.taxe, "total": cart_obj.total

	}
	return JsonResponse(cart_data)


def cart_home(request):
	cart_obj, new_obj = Cart.objects.new_or_get(request)
	context = {
		"cart": cart_obj,
	}
	return render(request, "carts/home.html", context)

def update_cart(request):
	product_id = request.POST.get("product_id")
	product_quantite = request.POST.get("product_quantite")

	if product_id is not None:
		try:
			product_obj = Product.objects.get(id=product_id)
		except Product.DoesNotExist:
			messages.info(request, _("Désolé Mme M {user} le produit vient de finir dans le dépôt nous revenons dans sous peu".format(user=request.user)))
			return redirect(reverse("carts:home"))

		cart_obj, new_obj = Cart.objects.new_or_get(request)
		if product_obj in cart_obj.products.all():
			cart_obj.products.remove(product_obj)
			cart_obj.quantite.pop(str(product_obj.id))


			added = False
			print("Enlevé")
			print("Quantité enlevée :", product_quantite)
		else:
			cart_obj.products.add(product_obj)
			added = True
			try:
				cart_obj.quantite.get(str(product_obj.id)).update(product_quantite) #Une mise à jour du tableau des quantits
				cart_obj.products.remove(product_obj)
				cart_obj.quantite.get(str(product_obj.id)).update(product_quantite)
				cart_obj.products.add(product_obj)
			except AttributeError:
				cart_obj.products.remove(product_obj)
				cart_obj.quantite[str(product_obj.id)] = product_quantite
				cart_obj.products.add(product_obj)
			print("ajouté")
			print("Quantité ajoutée :", product_quantite)



		request.session["cart_items"] = cart_obj.products.count()
		request.session["cart_total"] = str(Decimal(cart_obj.total).quantize(Decimal('1.00')))


		if request.is_ajax():
			json_data = {
				"added": added,
				"removed": not added,

				"cartItemCount": cart_obj.products.count(),
				"cartTotal": str(Decimal(cart_obj.total).quantize(Decimal('1.00'))),

			}
			return JsonResponse(json_data, status=200)
	return redirect("carts:home")



def update_cart_old(request):
	print("Qty changed")
	product_id = request.POST.get("product_id")
	for_add_product = request.POST.get("for_add_product")
	for_remove_product = request.POST.get("for_remove_product")
	for_grow_product = request.POST.get("for_grow_product")
	for_qty_product  = request.POST.get("for_qty_product")
	product_quantite = request.POST.get("product_quantite")



	added = False #Pour savoir si le produit a été ajouté au panier
	removed = False #Pour savoir si produit a été supprimier du panier
	quantited = False #Pour savoir si c'est dans la case de quantité qui utliser pour modifier la quantité dans le panier
	stock_finish = False #Pour savoir si le stock ne dépasse pas 
	minimum = False #Minimum de quantité à faire entrer
	no_number_quantite = False #Donnée de quantité 

	if product_id is not None:
		"""
		Si l'id stocké dans le input est valide
		"""
		try:
			product_obj = Product.objects.get(id=product_id) #On recupère le produit dont l'id a été passé
		except Product.DoesNotExist:
			messages.success(request, _("Désolé Mme M {user} le produit vient de finir dans le dépôt nous revenons dans sous peu".format(user=request.user)))
			stock_finish = True
			return redirect(reverse("carts:home"))


		cart_obj, new_obj = Cart.objects.new_or_get(request)
		if product_obj.stock >0:

			if for_add_product:
				cart_obj.quantite[str(product_obj.id)] = 1
				cart_obj.products.add(product_obj)
				added = True

			elif for_remove_product:
				print("remove")
				cart_obj.products.remove(product_obj)
				cart_obj.quantite.pop(str(product_obj.id))
				cart_obj.save()
				removed = True


			if for_qty_product:
				try:
					nb_quantite = int(product_quantite)
				except ValueError:
					no_number_quantite = True
					nb_quantite = None

				if nb_quantite or nb_quantite==0:
					if nb_quantite >=1:
						try:
							cart_obj.quantite.get(str(product_obj.id)).update(product_quantite) #Une mise à jour du tableau des quantits
							cart_obj.products.remove(product_obj)
							cart_obj.quantite.get(str(product_obj.id)).update(product_quantite)
							cart_obj.products.add(product_obj)
						except AttributeError:
							cart_obj.products.remove(product_obj)
							cart_obj.quantite[str(product_obj.id)] = product_quantite
							cart_obj.products.add(product_obj)

						quantited = True

					else:
						minimum = True


		else:
			stock_finish = True #Le cas où le stock restant du produit est fini on envoie un message à l'utilisateur

		request.session["cart_items"] = cart_obj.products.count()
		request.session["cart_total"] = str(Decimal(cart_obj.total).quantize(Decimal('1.00')))



		

		if request.is_ajax():
			json_data = {
				"added": added,
				"removed": removed,
				"quantited" : quantited,
				"minimum": minimum,
				"no_number_quantite": no_number_quantite,
				"stock_finish": stock_finish,
				"cartItemCount": cart_obj.products.count(),
				"cartTotal": str(Decimal(cart_obj.total).quantize(Decimal('1.00'))),

			}
			return JsonResponse(json_data, status=200)
	return redirect("carts:home")


def demo_ajax(request):
	qty_content = request.POST.get("product_quantite")

	print("Il a été exécuté avec", qty_content)
	json_data = {"test":"Le test de marche d'ajax sans formulaire"}
	if request.is_ajax():
		print("Ca marche")
		return JsonResponse(json_data, status=200)

	return redirect("carts:home")




  

def checkout_card(request):
	cart_obj, cart_created = Cart.objects.new_or_get(request)
	order_obj = None
	if cart_created or cart_obj.products.count() == 0:
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
	print("On arrive ici")
	cart_obj, cart_created = Cart.objects.new_or_get(request)
	order_obj = None
	if cart_created or cart_obj.products.count() == 0:
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
			request.session["cart_total"] = str(0.00)
			request.session["items"] = []

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


