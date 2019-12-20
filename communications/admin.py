from django.contrib import admin
from django.utils.safestring import mark_safe


from .models import Slide

# Register your models here.




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




	def get_actions(self, request):
		actions = super().get_actions(request)
		if "delete_selected" in actions:
			del actions["delete_selected"]
		return actions







