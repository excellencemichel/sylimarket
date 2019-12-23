from django.contrib import admin
from django.utils.safestring import mark_safe


from .models import Slide, Baniere

# Register your models here.

MAX_BANIERE = 4


MAX_SLIDE = 12




@admin.register(Slide)
class SlideAdmin(admin.ModelAdmin):

	readonly_fields = ["show_image"]
	list_display = ("titre", "annonce")
	list_filter = ("titre", "updated") #Pour les champs qui vont s'afficher dans l'admin
	date_hierarchy = "updated" #Classification par date

	def show_image(self, obj):
		return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
			url = obj.image.url,
			width = 250,
			height = 250,
			))



	def has_add_permission(self, request):
		if self.model.objects.count() >= MAX_SLIDE:
			return False
		return super().has_add_permission(request)
		








	def get_actions(self, request):
		actions = super().get_actions(request)
		if "delete_selected" in actions:
			del actions["delete_selected"]
		return actions





@admin.register(Baniere)
class BaniereAdmin(admin.ModelAdmin):
	readonly_fields = ["show_image"]
	list_display = ( "annonce", "message")
	list_filter = ("updated",) #Pour les champs qui vont s'afficher dans l'admin
	date_hierarchy = "updated" #Classification par date

	def show_image(self, obj):
		return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
			url = obj.image.url,
			width = 250,
			height = 250,
			))


	def has_add_permission(self, request):
		if self.model.objects.count() >= MAX_BANIERE:
			return False
		return super().has_add_permission(request)






	def get_actions(self, request):
		actions = super().get_actions(request)
		if "delete_selected" in actions:
			del actions["delete_selected"]
		return actions







