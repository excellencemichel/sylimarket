from django.db.models.signals import pre_delete, post_delete


from .products import Product 


from .clothings import ( MenClothing, WomenClothing, Pantalon,
					Culotte, Jupe, MenShoes,
					WomenShoes, AccessoireClothng

					)



from .computers import (Computer, AccessoireComputer
			)



from .phones import (Phone, Tablette, AccessoirePhone
		)






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
