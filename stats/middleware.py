from django.db.models import F 


# Locale import
from analytics.utils import get_client_ip

from .models import Statistique






def stats_middleware(get_response):
	def middleware(request):
		"""
		Avant chaque exécution de la vue, on incremente
		le nombr de page vues à chque appel de vues
		"""

		try:
			#Le compteur lié à la page est récuperé et incrementé
			page_view = Statistique.objects.get(url=request.path)
			page_view.nb_visites = F("nb_visites") + 1
			page_view.save()

		except Statistique.DoesNotExist:

			if request.user.is_authenticated:
				request_user = request.user.email
			else:
				request_user = "AnonymeUser"
			request_user_ip = get_client_ip(request)

			page_view = Statistique.objects.create(url=request.path, request_user=request_user, request_user_ip=request_user_ip)


		#Appel de la vu Django
		response = get_response(request)
		# Une fois la vue exécutée, on ajoute à la fin le nombre de vues de la page
		# response.content += bytes("Cette page a été vue {0} fois.".format(page_view.nb_visites), "utf8")

		# Et on retourne le résultat
		return response
	return middleware