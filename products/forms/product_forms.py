from django import forms

from utils.generator_utils import unique_slug_generator
from django.utils.translation import gettext_lazy as _


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


def save_instance_model(instance, instance_type):
	try:
		product = Product.objects.get(id=instance.product_id)
		print("Le produit existe déjà")
		if product is not None:
			# import pdb; pdb.set_trace()

			Product.objects.filter(id=instance.product_id).update(
				name=instance.name,
				description = instance.description,
				price = instance.price,
				promotion = instance.promotion,
				taux_taxe = instance.taux_taxe,
				taxe 	  = instance.taxe,
				subtotal = instance.subtotal,
				stock = instance.stock,
				featured = instance.featured,
				special = instance.special,
				solde = instance.solde,
				pourcentage = instance.pourcentage,
				active = instance.active,
				marque = instance.marque,
				image = instance.image,
				product_model = instance.product_model,
				product_type = instance_type
				)
			print("Le produit a été modifié")

			instance.product = product



	except Product.DoesNotExist:
		print("Le produit n'existe pas")

		product = Product.objects.create(
		name=instance.name,
		description = instance.description,
		price = instance.price,
		promotion = instance.promotion,
		taux_taxe = instance.taux_taxe,
		taxe      = instance.taxe,
		subtotal = instance.subtotal,
		stock = instance.stock,
		featured = instance.featured,
		special = instance.special,
		solde = instance.solde,
		pourcentage = instance.pourcentage,
		active = instance.active,
		marque = instance.marque,
		image = instance.image,
		product_model = instance.product_model,
		product_type = instance_type
		)
		product.save()

		instance.product = product


	except:
		print("Autre erreur")






class ProductForm(forms.ModelForm):
  
    class Meta:
        model = Product
        exclude = ["slug"]


    def save(self, commit=True):
    	instance = super(ProductForm, self).save(commit=False)
    	print("Voici instance", instance)

    	if not instance.slug:
    		instance.slug = unique_slug_generator(instance)
    	if commit:
    		instance.save()
    	
    	return instance




###################----------clothings -----------------###################


class MenClothingForm(forms.ModelForm):
	class Meta:
		model = MenClothing
		fields = "__all__"
		exclude = ["slug", "product", "product_type"]



	def save(self, commit=True):

		instance = super(MenClothingForm, self).save(commit=False)
		save_instance_model(instance=instance, instance_type=Product.MEN_CLOTHING)

		if commit:
			instance.save()
		return instance







class WomenClothingForm(forms.ModelForm):
	class Meta:
		model = WomenClothing
		fields = "__all__"
		exclude = ["slug", "product", "product_type"]



	def save(self, commit=True):

		instance = super(WomenClothingForm, self).save(commit=False)
		save_instance_model(instance=instance, instance_type=Product.WOMEN_CLOTHING)

		if commit:
			instance.save()
		return instance




class PantalonForm(forms.ModelForm):
	class Meta:
		model = Pantalon
		fields = "__all__"
		exclude = ["slug", "product", "product_type"]



	def save(self, commit=True):

		instance = super(PantalonForm, self).save(commit=False)
		save_instance_model(instance=instance, instance_type=Product.PANTALON)

		if commit:
			instance.save()
		return instance







class CulotteForm(forms.ModelForm):
	class Meta:
		model = Culotte
		fields = "__all__"
		exclude = ["slug", "product", "product_type"]



	def save(self, commit=True):

		instance = super(CulotteForm, self).save(commit=False)
		save_instance_model(instance=instance, instance_type=Product.CULOTTE)

		if commit:
			instance.save()
		return instance







class JupeForm(forms.ModelForm):
	class Meta:
		model = Jupe
		fields = "__all__"
		exclude = ["slug", "product", "product_type"]



	def save(self, commit=True):

		instance = super(JupeForm, self).save(commit=False)
		save_instance_model(instance=instance, instance_type=Product.JUPE)

		if commit:
			instance.save()
		return instance





class MenShoesForm(forms.ModelForm):
	class Meta:
		model = MenShoes
		fields = "__all__"
		exclude = ["slug", "product", "product_type"]



	def save(self, commit=True):

		instance = super(MenShoesForm, self).save(commit=False)
		save_instance_model(instance=instance, instance_type=Product.MEN_SHOE)

		if commit:
			instance.save()
		return instance






class WomenShoesForm(forms.ModelForm):
	class Meta:
		model = WomenShoes
		fields = "__all__"
		exclude = ["slug", "product", "product_type"]



	def save(self, commit=True):

		instance = super(WomenShoesForm, self).save(commit=False)
		save_instance_model(instance=instance, instance_type=Product.WOMEN_SHOE)

		if commit:
			instance.save()
		return instance






class AccessoireClothngForm(forms.ModelForm):
	class Meta:
		model = AccessoireClothng
		fields = "__all__"
		exclude = ["slug", "product", "product_type"]



	def save(self, commit=True):

		instance = super(AccessoireClothngForm, self).save(commit=False)
		save_instance_model(instance=instance, instance_type=Product.CLOTHING_ACCESSOIRE)

		if commit:
			instance.save()
		return instance







###################----------End clothings -----------------###################



###################----------Start Computer -----------------###################







class ComputerForm(forms.ModelForm):
	class Meta:
		model = Computer
		fields = "__all__"
		exclude = ["slug", "product", "product_type"]



	def save(self, commit=True):

		instance = super(ComputerForm, self).save(commit=False)
		save_instance_model(instance=instance, instance_type=Product.COMPUTER)

		if commit:
			instance.save()
		return instance












class AccessoireComputerForm(forms.ModelForm):
	promotion 	= forms.CharField(label=_("Prix"))
	price 		= forms.CharField(label=_("Prix en promotion"))

	class Meta:
		model = AccessoireComputer
		fields = "__all__"
		exclude = ["slug", "product", "product_type"]



	def save(self, commit=True):

		instance = super(AccessoireComputerForm, self).save(commit=False)
		save_instance_model(instance=instance, instance_type=Product.COMPUTER_ACCESSOIRE)

		if commit:
			instance.save()
		return instance



###################----------End Computer -----------------###################





###################----------Start Phone -----------------###################










class PhoneForm(forms.ModelForm):
	class Meta:
		model = Phone
		fields = "__all__"
		exclude = ["slug", "product", "product_type"]



	def save(self, commit=True):

		instance = super(PhoneForm, self).save(commit=False)
		save_instance_model(instance=instance, instance_type=Product.PHONE)

		if commit:
			instance.save()
		return instance









class TabletteForm(forms.ModelForm):
	class Meta:
		model = Tablette
		fields = "__all__"
		exclude = ["slug", "product", "product_type"]



	def save(self, commit=True):

		instance = super(TabletteForm, self).save(commit=False)
		save_instance_model(instance=instance, instance_type=Product.TABLETE)

		if commit:
			instance.save()
		return instance











class AccessoirePhoneForm(forms.ModelForm):
	class Meta:
		model = AccessoirePhone
		fields = "__all__"
		exclude = ["slug", "product", "product_type"]



	def save(self, commit=True):

		instance = super(AccessoirePhoneForm, self).save(commit=False)
		save_instance_model(instance=instance, instance_type=Product.PHONE_ACCESSOIRE)

		if commit:
			instance.save()
		return instance








###################----------End Phone -----------------###################









