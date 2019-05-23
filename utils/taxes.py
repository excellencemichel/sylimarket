from decimal import Decimal 

from utils.decimal_utils import multiplier, diviser, TWOPLACES




def calcule_taxe(sender, instance, *args, **kwargs):
	if instance:
		taux = diviser(instance.taux_taxe, 100)
		instance.taxe = multiplier(instance.price, taux)