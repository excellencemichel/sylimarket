from django.contrib import admin

from django.utils.safestring import mark_safe



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
	readonly_fields = ["show_image", "taxe", "subtotal"]



	def show_image(self, obj):

		return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
			url = obj.image.url,
			width = 250,
			height = 250,

			))



	def get_actions(self, request):
		actions = super().get_actions(request)
		if 'delete_selected' in actions:
			del actions['delete_selected']
		return actions

	def has_add_permission(self, request):
		return False



	def has_delete_permission(self, request, obj=None):
		return False

	def has_update_permission(self, request, obj=None):
		return False










@admin.register(MenClothing)
class MenClothingAdmin(admin.ModelAdmin):
	form = MenClothingForm

	readonly_fields = ["show_image", "taxe", "subtotal"]

	def show_image(self, obj):
		return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
			url = obj.image.url,
			width = 250,
			height = 250,

			))



@admin.register(WomenClothing)
class WomenClothingAdmin(admin.ModelAdmin):
	form = WomenClothingForm

	readonly_fields = ["show_image", "taxe", "subtotal"]

	def show_image(self, obj):
		return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
			url = obj.image.url,
			width = 250,
			height = 250,

			))



@admin.register(Pantalon)
class PantalonAdmin(admin.ModelAdmin):
	form = PantalonForm
	readonly_fields = ["show_image", "taxe", "subtotal"]
	def show_image(self, obj):
		return mark_safe('<im src={url}" width="{width}" height="{height}" />'.format(
			url = obj.image.url,
			width = obj.image.width,
			height = obj.image.height,

			))



@admin.register(Culotte)
class CulotteAdmin(admin.ModelAdmin):
	form = CulotteForm
	readonly_fields = ["show_image", "taxe", "subtotal"]

	def show_image(self, obj):
		return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
			url = obj.image.url,
			width = 250,
			height = 250,

			))



@admin.register(Jupe)
class JupeAdmin(admin.ModelAdmin):
	form = JupeForm
	readonly_fields = ["show_image", "taxe", "subtotal"]

	def show_image(self, obj):
		return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
			url = obj.image.url,
			width = 250,
			height = 250,

			))




@admin.register(MenShoes)
class MenShoesAdmin(admin.ModelAdmin):
	form = MenShoesForm
	readonly_fields = ["show_image", "taxe", "subtotal"]

	def show_image(self, obj):
		return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
			url = obj.image.url,
			width = 250,
			height = 250,

			))



@admin.register(WomenShoes)
class WomenShoesAdmin(admin.ModelAdmin):
	form = WomenShoesForm
	readonly_fields = ["show_image", "taxe", "subtotal"]

	def show_image(self, obj):
		return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
			url = obj.image.url,
			width = 250,
			height = 250,

			))



@admin.register(AccessoireClothng)
class AccessoireClothngAdmin(admin.ModelAdmin):
	form = AccessoireClothngForm
	readonly_fields = ["show_image", "taxe", "subtotal"]

	def show_image(self, obj):
		return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
			url = obj.image.url,
			width = 250,
			height = 250,

			))



@admin.register(Computer)
class ComputerAdmin(admin.ModelAdmin):
	form = ComputerForm
	readonly_fields = ["show_image", "taxe", "subtotal"]

	def show_image(self, obj):
		return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
			url = obj.image.url,
			width = 250,
			height = 250,

			))



@admin.register(AccessoireComputer)
class AccessoireComputerAdmin(admin.ModelAdmin):
	form = AccessoireComputerForm
	readonly_fields = ["show_image", "taxe", "subtotal"]

	def show_image(self, obj):
		return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
			url = obj.image.url,
			width = 250,
			height = 250,

			))



@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
	form = PhoneForm
	readonly_fields = ["show_image", "taxe", "subtotal"]

	def show_image(self, obj):
		return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
			url = obj.image.url,
			width = 250,
			height = 250,

			))



@admin.register(Tablette)
class TabletteAdmin(admin.ModelAdmin):
	form = TabletteForm

	readonly_fields = ["show_image", "taxe", "subtotal"]

	def show_image(self, obj):
		return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
			url = obj.image.url,
			width = 250,
			height = 250,

			))



@admin.register(AccessoirePhone)
class AccessoirePhoneAdmin(admin.ModelAdmin):
	form = AccessoirePhoneForm

	readonly_fields = ["show_image", "taxe", "subtotal"]

	def show_image(self, obj):
		return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
			url = obj.image.url,
			width = 250,
			height = 250,

			))







