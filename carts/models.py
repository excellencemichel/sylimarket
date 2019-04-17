from decimal import Decimal 


from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save, post_save, m2m_changed, pre_delete, post_delete
from django.db.models import  F 
from django.contrib.postgres.fields import HStoreField


from .signals import cart_item_added_signal
from utils.decimal_utils import multiplier, diviser, TWOPLACES


from products.models import Product
# Create your models here.


User = settings.AUTH_USER_MODEL



from django.contrib.postgres.signals import (
    get_citext_oids, get_hstore_oids, register_type_handlers,
)
from django.db.migrations.operations.base import Operation


class CreateExtension(Operation):
    reversible = True

    def __init__(self, name):
        self.name = name

    def state_forwards(self, app_label, state):
        pass

    def database_forwards(self, app_label, schema_editor, from_state, to_state):
        if schema_editor.connection.vendor != 'postgresql':
            return
        schema_editor.execute("CREATE EXTENSION IF NOT EXISTS %s" % schema_editor.quote_name(self.name))
        # Clear cached, stale oids.
        get_hstore_oids.cache_clear()
        get_citext_oids.cache_clear()
        # Registering new type handlers cannot be done before the extension is
        # installed, otherwise a subsequent data migration would use the same
        # connection.
        register_type_handlers(schema_editor.connection)

    def database_backwards(self, app_label, schema_editor, from_state, to_state):
        schema_editor.execute("DROP EXTENSION %s" % schema_editor.quote_name(self.name))
        # Clear cached, stale oids.
        get_hstore_oids.cache_clear()
        get_citext_oids.cache_clear()

    def describe(self):
        return "Creates extension %s" % self.name










class HStoreExtension(CreateExtension):

    def __init__(self):
        self.name = 'hstore'






class CartManager(models.Manager):

	def new_or_get(self, request):
		cart_id	= request.session.get("cart_id", None)
		qs	= self.get_queryset().filter(id=cart_id)
		if qs.count()==1:
			new_obj = False
			cart_obj	 = qs.first()
			if request.user.is_authenticated and cart_obj.user is None:
				cart_obj.user = request.user
				cart_obj.save()

		else:
			cart_obj = Cart.objects.new(user=request.user)
			new_obj = True
			request.session["cart_id"] = cart_obj.id

		return cart_obj, new_obj


	def new(self, user=None):
		user_obj	= None
		print(user)
		if user is not None:
			if user.is_authenticated:
				user_obj=user
		return self.model.objects.create(user=user_obj, quantite={})

class Cart(models.Model):
	user 		= models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
	products    = models.ManyToManyField(Product, blank=True)
	quantite    = HStoreField(null=True, blank=True)
	subtotal 	= models.DecimalField(default=0.00, max_digits=100, decimal_places =2 )
	total 		= models.DecimalField(default=0.00, max_digits=100, decimal_places =2 )

	updated		= models.DateTimeField(auto_now=True)
	timestamp	= models.DateTimeField(auto_now_add=True)


	objects		= CartManager()




	def __str__(self):
		return ("Panier de:  {user} coûte : {total}".format(user=self.user, total=self.total))



def m2m_changed_cart_receiver(sender, instance, action, *args, **kwargs):
    if action == 'post_add' or action == 'post_remove' or action == 'post_clear':
	    products = instance.products.all()
	    total = 0
	    print(instance.quantite)
	    for x in products:
	    	total += (multiplier(x.price , Decimal(int(instance.quantite[str(x.id)])).quantize(TWOPLACES)))
	    if instance.subtotal != total:
	        instance.subtotal = total
	        instance.save()




m2m_changed.connect(m2m_changed_cart_receiver, sender=Cart.products.through)




def pre_save_cart_receiver(sender, instance,*args, **kwargs):
	if instance.subtotal > 0:
		instance.total = multiplier(instance.subtotal, Decimal(1.08).quantize(TWOPLACES))# + 1.3
	else:
		instance.total = 0.00



pre_save.connect(pre_save_cart_receiver, sender=Cart)