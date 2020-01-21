import csv
from django.http import HttpResponse

from django.contrib import admin
from django.contrib.admin import AdminSite

from django.utils.safestring import mark_safe

from django import forms
from django.urls import path
from django.shortcuts import render, redirect








#import from models
from .models import (  Product,

					#clothings
					MenClothing, WomenClothing, Pantalon,
					Culotte, Jupe, MenShoes,
					WomenShoes, AccessoireClothng,

					#computers
					Computer, AccessoireComputer,

					#phones
					Phone, Tablette, AccessoirePhone,

					Electromenager,

					Beauty,

					Health,

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
					PhoneForm, TabletteForm, AccessoirePhoneForm,

					ElectromenagerForm,

					BeautyForm,

					HealthForm

					)






# Register your models here.

# Fiche de recherche

class Promotion(admin.SimpleListFilter):
	title = "flash"
	parameter_name ="est_flash"

	def lookups(self, request, model_admin):
		return (
				("Oui", "Oui"),
				("Non", "Non"),
			)


	def queryset(self, request, queryset):
		value = self.value()
		if value =="Oui":
			return queryset.filter(pourcentage__gt=50)
		elif value =="Non":
			return queryset.exclude(pourcentage__gt=50)
		return queryset


# Exportation


class ExportCsvMixin:
	def exporter_en_csv(self, request, queryset):
		meta = self.model._meta
		field_names = [field.name for field in meta.fields]

		response = HttpResponse(content_type="text/csv")
		response["Content-Disposition"] = "attachement; filename={}.csv".format(meta)
		writer = csv.writer(response)

		writer.writerow(field_names)
		for obj in queryset:
			row = writer.writerow([getattr(obj, field) for field in field_names])

		return response
	exporter_en_csv.short_description ="Selection à exporter"




class CsvImportForm(forms.Form):
	csv_file = forms.FileField()




@admin.register(Product)
class ProductAdmin(admin.ModelAdmin, ExportCsvMixin):
	form = ProductForm
	readonly_fields = ["show_image", "taxe", "subtotal"]
	list_display = ("name", "price", "en_flash")
	list_filter = ("price", Promotion) #Pour les champs qui vont s'afficher dans l'admin
	date_hierarchy = "updated" #Classification par date

	change_list_template ="products/admin/product_changelist.html"


	actions = ["exporter_en_csv"]

	


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

	def show_image(self, obj):
		return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
			url = obj.image.url,
			width = 250,
			height = 250,

			))


	def en_flash(self, obj):
		return obj.pourcentage > 50

	en_flash.boolean =True


	def get_actions(self, request):
		actions = super().get_actions(request)
		if "delete_selected" in actions:
			del actions["delete_selected"]
		return actions



	def get_urls(self):
		urls = super().get_urls()
		mon_urls = [

			path("import-csv/", self.import_csv),

		]
		return mon_urls + urls


	def import_csv(self, request):
		if request.method =="POST":
			csv_file = request.FILES["csv_file"]
			reader = csv.reader(csv_file)
			#Création d'un objet issu du fichier csv
			self.message_user(request, "Votre csv a été importé")
			return redirect("..")

		form = CsvImportForm()
		payload = {"form": form}
		return render(
				request, "products/admin/csv_form.html", payload
			)










# @admin.register(MenClothing)
class MenClothingAdmin(admin.ModelAdmin, ExportCsvMixin):
	form = MenClothingForm

	readonly_fields = ["show_image", "taxe", "subtotal"]
	list_display = ("name", "price", "en_flash")
	list_filter = ("price", Promotion) #Pour les champs qui vont s'afficher dans l'admin
	date_hierarchy = "updated" #Classification par date

	change_list_template ="products/admin/product_changelist.html"


	actions = ["exporter_en_csv"]

	
	def show_image(self, obj):
		return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
			url = obj.image.url,
			width = 250,
			height = 250,

			))


	def en_flash(self, obj):
		return obj.pourcentage > 50

	en_flash.boolean =True


	def get_actions(self, request):
		actions = super().get_actions(request)
		if "delete_selected" in actions:
			del actions["delete_selected"]
		return actions



	def get_urls(self):
		urls = super().get_urls()
		mon_urls = [

			path("import-csv/", self.import_csv),

		]
		return mon_urls + urls


	def import_csv(self, request):
		if request.method =="POST":
			csv_file = request.FILES["csv_file"]
			reader = csv.reader(csv_file)
			#Création d'un objet issu du fichier csv
			self.message_user(request, "Votre csv a été importé")
			return redirect("..")

		form = CsvImportForm()
		payload = {"form": form}
		return render(
				request, "products/admin/csv_form.html", payload
			)











# @admin.register(WomenClothing)
class WomenClothingAdmin(admin.ModelAdmin, ExportCsvMixin):
	form = WomenClothingForm

	readonly_fields = ["show_image", "taxe", "subtotal"]
	list_display = ("name", "price", "en_flash")
	list_filter = ("price", Promotion) #Pour les champs qui vont s'afficher dans l'admin
	date_hierarchy = "updated" #Classification par date

	change_list_template ="products/admin/product_changelist.html"


	actions = ["exporter_en_csv"]

	
	def show_image(self, obj):
		return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
			url = obj.image.url,
			width = 250,
			height = 250,

			))


	def en_flash(self, obj):
		return obj.pourcentage > 50

	en_flash.boolean =True


	def get_actions(self, request):
		actions = super().get_actions(request)
		if "delete_selected" in actions:
			del actions["delete_selected"]
		return actions



	def get_urls(self):
		urls = super().get_urls()
		mon_urls = [

			path("import-csv/", self.import_csv),

		]
		return mon_urls + urls



	def import_csv(self, request):
		if request.method =="POST":
			csv_file = request.FILES["csv_file"]
			reader = csv.reader(csv_file)
			#Création d'un objet issu du fichier csv
			self.message_user(request, "Votre csv a été importé")
			return redirect("..")

		form = CsvImportForm()
		payload = {"form": form}
		return render(
				request, "products/admin/csv_form.html", payload
			)











# @admin.register(Pantalon)
class PantalonAdmin(admin.ModelAdmin, ExportCsvMixin):
	form = PantalonForm
	readonly_fields = ["show_image", "taxe", "subtotal"]
	list_display = ("name", "price", "en_flash")
	list_filter = ("price", Promotion) #Pour les champs qui vont s'afficher dans l'admin
	date_hierarchy = "updated" #Classification par date

	change_list_template ="products/admin/product_changelist.html"


	actions = ["exporter_en_csv"]

	
	
	def show_image(self, obj):
		return mark_safe('<im src={url}" width="{width}" height="{height}" />'.format(
			url = obj.image.url,
			width = obj.image.width,
			height = obj.image.height,

			))



	def en_flash(self, obj):
		return obj.pourcentage > 50

	en_flash.boolean =True


	def get_actions(self, request):
		actions = super().get_actions(request)
		if "delete_selected" in actions:
			del actions["delete_selected"]
		return actions



	def get_urls(self):
		urls = super().get_urls()
		mon_urls = [

			path("import-csv/", self.import_csv),

		]
		return mon_urls + urls



	def import_csv(self, request):
		if request.method =="POST":
			csv_file = request.FILES["csv_file"]
			reader = csv.reader(csv_file)
			#Création d'un objet issu du fichier csv
			self.message_user(request, "Votre csv a été importé")
			return redirect("..")

		form = CsvImportForm()
		payload = {"form": form}
		return render(
				request, "products/admin/csv_form.html", payload
			)











# @admin.register(Culotte)
class CulotteAdmin(admin.ModelAdmin, ExportCsvMixin):
	form = CulotteForm
	readonly_fields = ["show_image", "taxe", "subtotal"]
	list_display = ("name", "price", "en_flash")
	list_filter = ("price", Promotion) #Pour les champs qui vont s'afficher dans l'admin
	date_hierarchy = "updated" #Classification par date

	change_list_template ="products/admin/product_changelist.html"


	actions = ["exporter_en_csv"]

	
	def show_image(self, obj):
		return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
			url = obj.image.url,
			width = 250,
			height = 250,

			))



	def en_flash(self, obj):
		return obj.pourcentage > 50

	en_flash.boolean =True


	def get_actions(self, request):
		actions = super().get_actions(request)
		if "delete_selected" in actions:
			del actions["delete_selected"]
		return actions



	def get_urls(self):
		urls = super().get_urls()
		mon_urls = [

			path("import-csv/", self.import_csv),

		]
		return mon_urls + urls



	def import_csv(self, request):
		if request.method =="POST":
			csv_file = request.FILES["csv_file"]
			reader = csv.reader(csv_file)
			#Création d'un objet issu du fichier csv
			self.message_user(request, "Votre csv a été importé")
			return redirect("..")

		form = CsvImportForm()
		payload = {"form": form}
		return render(
				request, "products/admin/csv_form.html", payload
			)











# @admin.register(Jupe)
class JupeAdmin(admin.ModelAdmin, ExportCsvMixin):
	form = JupeForm
	readonly_fields = ["show_image", "taxe", "subtotal"]
	list_display = ("name", "price", "en_flash")
	list_filter = ("price", Promotion) #Pour les champs qui vont s'afficher dans l'admin
	date_hierarchy = "updated" #Classification par date

	change_list_template ="products/admin/product_changelist.html"


	actions = ["exporter_en_csv"]

	
	def show_image(self, obj):
		return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
			url = obj.image.url,
			width = 250,
			height = 250,

			))



	def en_flash(self, obj):
		return obj.pourcentage > 50

	en_flash.boolean =True


	def get_actions(self, request):
		actions = super().get_actions(request)
		if "delete_selected" in actions:
			del actions["delete_selected"]
		return actions



	def get_urls(self):
		urls = super().get_urls()
		mon_urls = [

			path("import-csv/", self.import_csv),

		]
		return mon_urls + urls



	def import_csv(self, request):
		if request.method =="POST":
			csv_file = request.FILES["csv_file"]
			reader = csv.reader(csv_file)
			#Création d'un objet issu du fichier csv
			self.message_user(request, "Votre csv a été importé")
			return redirect("..")

		form = CsvImportForm()
		payload = {"form": form}
		return render(
				request, "products/admin/csv_form.html", payload
			)












# @admin.register(MenShoes)
class MenShoesAdmin(admin.ModelAdmin, ExportCsvMixin):
	form = MenShoesForm
	readonly_fields = ["show_image", "taxe", "subtotal"]
	list_display = ("name", "price", "en_flash")
	list_filter = ("price", Promotion) #Pour les champs qui vont s'afficher dans l'admin
	date_hierarchy = "updated" #Classification par date

	change_list_template ="products/admin/product_changelist.html"


	actions = ["exporter_en_csv"]

	
	def show_image(self, obj):
		return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
			url = obj.image.url,
			width = 250,
			height = 250,

			))


	def en_flash(self, obj):
		return obj.pourcentage > 50

	en_flash.boolean =True


	def get_actions(self, request):
		actions = super().get_actions(request)
		if "delete_selected" in actions:
			del actions["delete_selected"]
		return actions



	def get_urls(self):
		urls = super().get_urls()
		mon_urls = [

			path("import-csv/", self.import_csv),

		]
		return mon_urls + urls



	def import_csv(self, request):
		if request.method =="POST":
			csv_file = request.FILES["csv_file"]
			reader = csv.reader(csv_file)
			#Création d'un objet issu du fichier csv
			self.message_user(request, "Votre csv a été importé")
			return redirect("..")

		form = CsvImportForm()
		payload = {"form": form}
		return render(
				request, "products/admin/csv_form.html", payload
			)









# @admin.register(WomenShoes)
class WomenShoesAdmin(admin.ModelAdmin, ExportCsvMixin):
	form = WomenShoesForm
	readonly_fields = ["show_image", "taxe", "subtotal"]
	list_display = ("name", "price", "en_flash")
	list_filter = ("price", Promotion) #Pour les champs qui vont s'afficher dans l'admin
	date_hierarchy = "updated" #Classification par date

	change_list_template ="products/admin/product_changelist.html"


	actions = ["exporter_en_csv"]

	
	def show_image(self, obj):
		return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
			url = obj.image.url,
			width = 250,
			height = 250,

			))


	def en_flash(self, obj):
		return obj.pourcentage > 50

	en_flash.boolean =True


	def get_actions(self, request):
		actions = super().get_actions(request)
		if "delete_selected" in actions:
			del actions["delete_selected"]
		return actions



	def get_urls(self):
		urls = super().get_urls()
		mon_urls = [

			path("import-csv/", self.import_csv),

		]
		return mon_urls + urls



	def import_csv(self, request):
		if request.method =="POST":
			csv_file = request.FILES["csv_file"]
			reader = csv.reader(csv_file)
			#Création d'un objet issu du fichier csv
			self.message_user(request, "Votre csv a été importé")
			return redirect("..")

		form = CsvImportForm()
		payload = {"form": form}
		return render(
				request, "products/admin/csv_form.html", payload
			)











# @admin.register(AccessoireClothng)
class AccessoireClothngAdmin(admin.ModelAdmin, ExportCsvMixin):
	form = AccessoireClothngForm
	readonly_fields = ["show_image", "taxe", "subtotal"]
	list_display = ("name", "price", "en_flash")
	list_filter = ("price", Promotion) #Pour les champs qui vont s'afficher dans l'admin
	date_hierarchy = "updated" #Classification par date

	change_list_template ="products/admin/product_changelist.html"


	actions = ["exporter_en_csv"]

	
	def show_image(self, obj):
		return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
			url = obj.image.url,
			width = 250,
			height = 250,

			))


	def en_flash(self, obj):
		return obj.pourcentage > 50

	en_flash.boolean =True


	def get_actions(self, request):
		actions = super().get_actions(request)
		if "delete_selected" in actions:
			del actions["delete_selected"]
		return actions



	def get_urls(self):
		urls = super().get_urls()
		mon_urls = [

			path("import-csv/", self.import_csv),

		]
		return mon_urls + urls



	def import_csv(self, request):
		if request.method =="POST":
			csv_file = request.FILES["csv_file"]
			reader = csv.reader(csv_file)
			#Création d'un objet issu du fichier csv
			self.message_user(request, "Votre csv a été importé")
			return redirect("..")

		form = CsvImportForm()
		payload = {"form": form}
		return render(
				request, "products/admin/csv_form.html", payload
			)











# @admin.register(Computer)
class ComputerAdmin(admin.ModelAdmin, ExportCsvMixin):
	form = ComputerForm
	readonly_fields = ["show_image", "taxe", "subtotal"]
	list_display = ("name", "price", "en_flash")
	list_filter = ("price", Promotion) #Pour les champs qui vont s'afficher dans l'admin
	date_hierarchy = "updated" #Classification par date

	change_list_template ="products/admin/product_changelist.html"


	actions = ["exporter_en_csv"]

	
	def show_image(self, obj):
		return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
			url = obj.image.url,
			width = 250,
			height = 250,

			))



	def en_flash(self, obj):
		return obj.pourcentage > 50

	en_flash.boolean =True


	def get_actions(self, request):
		actions = super().get_actions(request)
		if "delete_selected" in actions:
			del actions["delete_selected"]
		return actions



	def get_urls(self):
		urls = super().get_urls()
		mon_urls = [

			path("import-csv/", self.import_csv),

		]
		return mon_urls + urls



	def import_csv(self, request):
		if request.method =="POST":
			csv_file = request.FILES["csv_file"]
			reader = csv.reader(csv_file)
			#Création d'un objet issu du fichier csv
			self.message_user(request, "Votre csv a été importé")
			return redirect("..")

		form = CsvImportForm()
		payload = {"form": form}
		return render(
				request, "products/admin/csv_form.html", payload
			)











# @admin.register(AccessoireComputer)
class AccessoireComputerAdmin(admin.ModelAdmin, ExportCsvMixin):
	form = AccessoireComputerForm
	readonly_fields = ["show_image", "taxe", "subtotal"]
	list_display = ("name", "price", "en_flash")
	list_filter = ("price", Promotion) #Pour les champs qui vont s'afficher dans l'admin
	date_hierarchy = "updated" #Classification par date

	change_list_template ="products/admin/product_changelist.html"


	actions = ["exporter_en_csv"]


	def show_image(self, obj):
		return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
			url = obj.image.url,
			width = 250,
			height = 250,

			))


	def en_flash(self, obj):
		return obj.pourcentage > 50

	en_flash.boolean =True


	def get_actions(self, request):
		actions = super().get_actions(request)
		if "delete_selected" in actions:
			del actions["delete_selected"]
		return actions



	def get_urls(self):
		urls = super().get_urls()
		mon_urls = [

			path("import-csv/", self.import_csv),

		]
		return mon_urls + urls



	def import_csv(self, request):
		if request.method =="POST":
			csv_file = request.FILES["csv_file"]
			reader = csv.reader(csv_file)
			#Création d'un objet issu du fichier csv
			self.message_user(request, "Votre csv a été importé")
			return redirect("..")

		form = CsvImportForm()
		payload = {"form": form}
		return render(
				request, "products/admin/csv_form.html", payload
			)


















# @admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin, ExportCsvMixin):
	form = PhoneForm
	readonly_fields = ["show_image", "taxe", "subtotal"]

	def show_image(self, obj):
		return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
			url = obj.image.url,
			width = 250,
			height = 250,

			))


	def en_flash(self, obj):
		return obj.pourcentage > 50

	en_flash.boolean =True


	def get_actions(self, request):
		actions = super().get_actions(request)
		if "delete_selected" in actions:
			del actions["delete_selected"]
		return actions



	def get_urls(self):
		urls = super().get_urls()
		mon_urls = [

			path("import-csv/", self.import_csv),

		]
		return mon_urls + urls



	def import_csv(self, request):
		if request.method =="POST":
			csv_file = request.FILES["csv_file"]
			reader = csv.reader(csv_file)
			#Création d'un objet issu du fichier csv
			self.message_user(request, "Votre csv a été importé")
			return redirect("..")

		form = CsvImportForm()
		payload = {"form": form}
		return render(
				request, "products/admin/csv_form.html", payload
			)










# @admin.register(Tablette)
class TabletteAdmin(admin.ModelAdmin, ExportCsvMixin):
	form = TabletteForm

	readonly_fields = ["show_image", "taxe", "subtotal"]

	def show_image(self, obj):
		return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
			url = obj.image.url,
			width = 250,
			height = 250,

			))



	def en_flash(self, obj):
		return obj.pourcentage > 50

	en_flash.boolean =True


	def get_actions(self, request):
		actions = super().get_actions(request)
		if "delete_selected" in actions:
			del actions["delete_selected"]
		return actions



	def get_urls(self):
		urls = super().get_urls()
		mon_urls = [

			path("import-csv/", self.import_csv),

		]
		return mon_urls + urls



	def import_csv(self, request):
		if request.method =="POST":
			csv_file = request.FILES["csv_file"]
			reader = csv.reader(csv_file)
			#Création d'un objet issu du fichier csv
			self.message_user(request, "Votre csv a été importé")
			return redirect("..")

		form = CsvImportForm()
		payload = {"form": form}
		return render(
				request, "products/admin/csv_form.html", payload
			)










# @admin.register(AccessoirePhone)
class AccessoirePhoneAdmin(admin.ModelAdmin,ExportCsvMixin):
	form = AccessoirePhoneForm

	readonly_fields = ["show_image", "taxe", "subtotal"]

	def show_image(self, obj):
		return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
			url = obj.image.url,
			width = 250,
			height = 250,

			))



	def en_flash(self, obj):
		return obj.pourcentage > 50

	en_flash.boolean =True


	def get_actions(self, request):
		actions = super().get_actions(request)
		if "delete_selected" in actions:
			del actions["delete_selected"]
		return actions



	def get_urls(self):
		urls = super().get_urls()
		mon_urls = [

			path("import-csv/", self.import_csv),

		]
		return mon_urls + urls



	def import_csv(self, request):
		if request.method =="POST":
			csv_file = request.FILES["csv_file"]
			reader = csv.reader(csv_file)
			#Création d'un objet issu du fichier csv
			self.message_user(request, "Votre csv a été importé")
			return redirect("..")

		form = CsvImportForm()
		payload = {"form": form}
		return render(
				request, "products/admin/csv_form.html", payload
			)







# @admin.register(AccessoirePhone)
class ElectromenagerAdmin(admin.ModelAdmin,ExportCsvMixin):
	form = ElectromenagerForm

	readonly_fields = ["show_image", "taxe", "subtotal"]

	def show_image(self, obj):
		return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
			url = obj.image.url,
			width = 250,
			height = 250,

			))



	def en_flash(self, obj):
		return obj.pourcentage > 50

	en_flash.boolean =True


	def get_actions(self, request):
		actions = super().get_actions(request)
		if "delete_selected" in actions:
			del actions["delete_selected"]
		return actions



	def get_urls(self):
		urls = super().get_urls()
		mon_urls = [

			path("import-csv/", self.import_csv),

		]
		return mon_urls + urls



	def import_csv(self, request):
		if request.method =="POST":
			csv_file = request.FILES["csv_file"]
			reader = csv.reader(csv_file)
			#Création d'un objet issu du fichier csv
			self.message_user(request, "Votre csv a été importé")
			return redirect("..")

		form = CsvImportForm()
		payload = {"form": form}
		return render(
				request, "products/admin/csv_form.html", payload
			)







# @admin.register(AccessoirePhone)
class BeautyAdmin(admin.ModelAdmin,ExportCsvMixin):
	form = BeautyForm

	readonly_fields = ["show_image", "taxe", "subtotal"]

	def show_image(self, obj):
		return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
			url = obj.image.url,
			width = 250,
			height = 250,

			))



	def en_flash(self, obj):
		return obj.pourcentage > 50

	en_flash.boolean =True


	def get_actions(self, request):
		actions = super().get_actions(request)
		if "delete_selected" in actions:
			del actions["delete_selected"]
		return actions



	def get_urls(self):
		urls = super().get_urls()
		mon_urls = [

			path("import-csv/", self.import_csv),

		]
		return mon_urls + urls



	def import_csv(self, request):
		if request.method =="POST":
			csv_file = request.FILES["csv_file"]
			reader = csv.reader(csv_file)
			#Création d'un objet issu du fichier csv
			self.message_user(request, "Votre csv a été importé")
			return redirect("..")

		form = CsvImportForm()
		payload = {"form": form}
		return render(
				request, "products/admin/csv_form.html", payload
			)


# @admin.register(AccessoirePhone)
class HealthAdmin(admin.ModelAdmin,ExportCsvMixin):
	form = HealthForm

	readonly_fields = ["show_image", "taxe", "subtotal"]

	def show_image(self, obj):
		return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
			url = obj.image.url,
			width = 250,
			height = 250,

			))



	def en_flash(self, obj):
		return obj.pourcentage > 50

	en_flash.boolean =True


	def get_actions(self, request):
		actions = super().get_actions(request)
		if "delete_selected" in actions:
			del actions["delete_selected"]
		return actions



	def get_urls(self):
		urls = super().get_urls()
		mon_urls = [

			path("import-csv/", self.import_csv),

		]
		return mon_urls + urls



	def import_csv(self, request):
		if request.method =="POST":
			csv_file = request.FILES["csv_file"]
			reader = csv.reader(csv_file)
			#Création d'un objet issu du fichier csv
			self.message_user(request, "Votre csv a été importé")
			return redirect("..")

		form = CsvImportForm()
		payload = {"form": form}
		return render(
				request, "products/admin/csv_form.html", payload
			)









# Création d'un autre site d'administration

class ProductAdminSite(AdminSite):
	site_header = "Adminstration de produits"
	site_title 	= "SyliMarket administration"
	index_tilte = "SyliMarket"



product_admin_site = ProductAdminSite(name="product_admin")



# product_admin_site.register(Product, ProductAdmin)


product_admin_site.register(MenClothing, MenClothingAdmin)

product_admin_site.register( WomenClothing, WomenClothingAdmin)

product_admin_site.register(Pantalon, PantalonAdmin)

product_admin_site.register(Culotte, CulotteAdmin)

product_admin_site.register(Jupe, JupeAdmin)

product_admin_site.register(MenShoes, MenShoesAdmin)

product_admin_site.register(WomenShoes, WomenShoesAdmin)

product_admin_site.register(AccessoireClothng, AccessoireClothngAdmin)

product_admin_site.register(Computer, ComputerAdmin)

product_admin_site.register(AccessoireComputer, AccessoireComputerAdmin)




product_admin_site.register(Phone, PhoneAdmin)


product_admin_site.register(Tablette, TabletteAdmin)

product_admin_site.register(AccessoirePhone, AccessoirePhoneAdmin)


product_admin_site.register(Electromenager, ElectromenagerAdmin)


product_admin_site.register(Beauty, BeautyAdmin)
product_admin_site.register(Health, HealthAdmin)

