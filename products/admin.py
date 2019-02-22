from django.contrib import admin




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



#import from forms
from .forms.product_forms import ( ProductForm,

					#clothings
					MenClothingForm, WomenClothingForm, PantalonForm,
					CulotteForm, JupeForm, MenShoesForm,
					WomenShoesForm, AccessoireClothngForm,

					#computers
					ComputerForm, AccessoireComputerForm,

					#phones
					PhoneForm, TabletteForm, AccessoirePhoneForm

					)






# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	form = ProductForm






@admin.register(MenClothing)
class MenClothingAdmin(admin.ModelAdmin):
	form = MenClothingForm



@admin.register(WomenClothing)
class WomenClothingAdmin(admin.ModelAdmin):
	form = WomenClothingForm



@admin.register(Pantalon)
class PantalonAdmin(admin.ModelAdmin):
	form = PantalonForm



@admin.register(Culotte)
class CulotteAdmin(admin.ModelAdmin):
	form = CulotteForm



@admin.register(Jupe)
class JupeAdmin(admin.ModelAdmin):
	form = JupeForm



@admin.register(MenShoes)
class MenShoesAdmin(admin.ModelAdmin):
	form = MenShoesForm



@admin.register(WomenShoes)
class WomenShoesAdmin(admin.ModelAdmin):
	form = WomenShoesForm



@admin.register(AccessoireClothng)
class AccessoireClothngAdmin(admin.ModelAdmin):
	form = AccessoireClothngForm



@admin.register(Computer)
class ComputerAdmin(admin.ModelAdmin):
	form = ComputerForm



@admin.register(AccessoireComputer)
class AccessoireComputerAdmin(admin.ModelAdmin):
	form = AccessoireComputerForm



@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
	form = PhoneForm



@admin.register(Tablette)
class TabletteAdmin(admin.ModelAdmin):
	form = TabletteForm



@admin.register(AccessoirePhone)
class AccessoirePhoneAdmin(admin.ModelAdmin):
	form = AccessoirePhoneForm







