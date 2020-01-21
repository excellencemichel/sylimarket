from decimal import Decimal 

from utils.decimal_utils import multiplier, diviser, TWOPLACES



from django.db.models.signals import pre_delete, post_delete, pre_save


from .products import Product 


from .clothings import ( MenClothing, WomenClothing, Pantalon,
					Culotte, Jupe, MenShoes,
					WomenShoes, AccessoireClothng

					)



from .computers import (Computer, AccessoireComputer
			)



from .phones import (Phone, Tablette, AccessoirePhone
		)


from .electromenagers import (Electromenager
		)


from .beauty import (Beauty)

from .health import (Health)




def pre_save_taxe(sender, instance, *args, **kwargs):
	if instance:
		taux = diviser(Decimal(instance.taux_taxe), 100)
		instance.taxe = multiplier(instance.price, taux)

	instance.subtotal = instance.price + instance.taxe


pre_save.connect(pre_save_taxe, sender=Product)

pre_save.connect(pre_save_taxe, sender=MenClothing)
pre_save.connect(pre_save_taxe, sender=WomenClothing)
pre_save.connect(pre_save_taxe, sender=Pantalon)
pre_save.connect(pre_save_taxe, sender=Culotte)
pre_save.connect(pre_save_taxe, sender=Jupe)
pre_save.connect(pre_save_taxe, sender=MenShoes)
pre_save.connect(pre_save_taxe, sender=WomenShoes)
pre_save.connect(pre_save_taxe, sender=AccessoireClothng)




pre_save.connect(pre_save_taxe, sender=Computer)
pre_save.connect(pre_save_taxe, sender=AccessoireComputer)


pre_save.connect(pre_save_taxe, sender=Phone)
pre_save.connect(pre_save_taxe, sender=Tablette)
pre_save.connect(pre_save_taxe, sender=AccessoirePhone)

pre_save.connect(pre_save_taxe, sender=Electromenager)



pre_save.connect(pre_save_taxe, sender=Beauty)
pre_save.connect(pre_save_taxe, sender=Health)









def instance_post_delete_receiver(sender, instance, *args, **kwargs):
	try :
		product = Product.objects.get(id=instance.product.id)
		product.delete()

	except Product.MultipleObjectsReturned:
		product = Product.objects.filter(id=instance.product.id).first()
		product.delete()
	except Product.DoesNotExist:
		print("Le produit a supprimer n'existe pas dans la table de produit")






post_delete.connect(instance_post_delete_receiver, sender=MenClothing)
post_delete.connect(instance_post_delete_receiver, sender=WomenClothing)
post_delete.connect(instance_post_delete_receiver, sender=Pantalon)
post_delete.connect(instance_post_delete_receiver, sender=Culotte)
post_delete.connect(instance_post_delete_receiver, sender=Jupe)
post_delete.connect(instance_post_delete_receiver, sender=MenShoes)
post_delete.connect(instance_post_delete_receiver, sender=WomenShoes)
post_delete.connect(instance_post_delete_receiver, sender=AccessoireClothng)







post_delete.connect(instance_post_delete_receiver, sender=Computer)
post_delete.connect(instance_post_delete_receiver, sender=AccessoireComputer)


post_delete.connect(instance_post_delete_receiver, sender=Phone)
post_delete.connect(instance_post_delete_receiver, sender=Tablette)
post_delete.connect(instance_post_delete_receiver, sender=AccessoirePhone)


post_delete.connect(instance_post_delete_receiver, sender=Electromenager)


post_delete.connect(instance_post_delete_receiver, sender=Beauty)
post_delete.connect(instance_post_delete_receiver, sender=Health)


