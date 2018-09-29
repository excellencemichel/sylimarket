from django.contrib import admin
from .models import Statistique

# Register your models here.


class StatistiqueAdmin(admin.ModelAdmin):
	list_display = ["__str__", "nb_visites", "request_user", "request_user_ip", "timestamp"]
	list_filter = ('nb_visites', "request_user_ip",)



	class Meta:
		model = Statistique




admin.site.register(Statistique, StatistiqueAdmin)