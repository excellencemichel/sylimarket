from django import forms

from utils.generator_utils import unique_slug_generator

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
class MenClothingForm(ProductForm):
	class Meta:
		model = MenClothing
		fields = "__all__"
		exclude = ["slug"]








class WomenClothingForm(ProductForm):
	class Meta:
		model = WomenClothing
		fields = "__all__"
		exclude = ["slug"]





class PantalonForm(ProductForm):
	class Meta:
		model = Pantalon
		fields = "__all__"
		exclude = ["slug"]





class CulotteForm(ProductForm):
	class Meta:
		model = Culotte
		fields = "__all__"
		exclude = ["slug"]





class JupeForm(ProductForm):
	class Meta:
		model = Jupe
		fields = "__all__"
		exclude = ["slug"]





class MenShoesForm(ProductForm):
	class Meta:
		model = MenShoes
		fields = "__all__"
		exclude = ["slug"]





class WomenShoesForm(ProductForm):
	class Meta:
		model = WomenShoes
		fields = "__all__"
		exclude = ["slug"]





class AccessoireClothngForm(ProductForm):
	class Meta:
		model = AccessoireClothng
		fields = "__all__"
		exclude = ["slug"]



###################----------End clothings -----------------###################



###################----------Start Computer -----------------###################

class ComputerForm(ProductForm):
	class Meta:
		model = Computer
		fields = "__all__"
		exclude = ["slug"]





class AccessoireComputerForm(ProductForm):
	class Meta:
		model = AccessoireComputer
		fields = "__all__"
		exclude = ["slug"]


###################----------End Computer -----------------###################





###################----------Start Phone -----------------###################
class PhoneForm(ProductForm):
	class Meta:
		model = Phone
		fields = "__all__"
		exclude = ["slug"]





class TabletteForm(ProductForm):
	class Meta:
		model = Tablette
		fields = "__all__"
		exclude = ["slug"]





class AccessoirePhoneForm(ProductForm):
	class Meta:
		model = AccessoirePhone
		fields = "__all__"
		exclude = ["slug"]



###################----------End Phone -----------------###################









