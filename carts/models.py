from decimal import Decimal 


from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save, post_save, m2m_changed, pre_delete, post_delete
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType 

from django.db import models



#Local import
from .signals import cart_item_added_signal

# Create your models here.

User = settings.AUTH_USER_MODEL


class CartManager(models.Manager):
	def new_or_get(self, request):
		cart_id = request.session.get("cart_id", None)
		qs = self.get_queryset().filter(id=cart_id)
		if qs.count() == 1:
			new_obj = False
			cart_obj = qs.first()
			if request.user.is_authenticated and cart_obj.user is None:
				cart_obj.user = request.user
				cart_obj.save()
		else:
			cart_obj = Cart.objects.new(user=request.user)
			new_obj = True
			request.session["cart_id"] = cart_obj.id 


		return cart_obj, new_obj


	def new(self, user=None):
		user_obj = None
		if user is not None:
			if user.is_authenticated:
				user_obj = user_obj
		return self.model.objects.create(user=user_obj)


class Cart(models.Model):
	user 		= models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
	subtotal 	= models.DecimalField(default=0.00, max_digits=100, decimal_places =2 )
	total 		= models.DecimalField(default=0.00, max_digits=100, decimal_places =2 )

	updated		= models.DateTimeField(auto_now=True)
	timestamp	= models.DateTimeField(auto_now_add=True)

	objects = CartManager()


	def __str__(self):
		return "Panier pour {user} a la valeur de {total}".format(user=self.user, total=self.total)



	def add_item(self, product, *args, **kwargs)->"CartItem":
		product_content_type = ContentType.objects.get_for_model(product.__class__)

		cart_item_obj = CartItem.objects.create(
			cart=self,
			product_content_type = product_content_type,
			product_object_id = product.pk,
			)
		quantite = product.cart_items.count()
		
		cart_item_obj.quantite = quantite
		cart_item_obj.save()
		cart_item_added_signal.send_robust(sender= self.__class__, instance=self, action="added")

		return cart_item_obj


	def delete_item(self, product, *args, **kwargs)->"CartItem":
		product_content_type = ContentType.objects.get_for_model(product.__class__)
		try:
			cart_item_obj = CartItem.objects.get(product_content_type=product_content_type, product_object_id=product.pk)
			cart_item_obj.delete()
		except CartItem.MultipleObjectsReturned:
			cart_item_obj = CartItem.objects.filter(product_content_type=product_content_type, product_object_id=product.pk).first()
			cart_item_obj.delete()
		except CartItem.DoesNotExist:
			pass


	def cart_item_exists(self, product, *args, **kwargs)-> "CartItem":
		product_content_type = ContentType.objects.get_for_model(product.__class__)
		return CartItem.objects.filter(product_content_type=product_content_type, product_object_id=product.pk).exists()





def pre_save_cart_receiver(sender, instance,*args, **kwargs):
	if instance.subtotal > 0:
		instance.total = Decimal(instance.subtotal) * Decimal(1.08)# + 1.3
	else:
		instance.total = 0.00



pre_save.connect(pre_save_cart_receiver, sender=Cart)



class CartItemQueryset(models.query.QuerySet):
	def by_model(self, model_class, model_queryset=False):
		c_type = ContentType.objects.get_for_model(model_class)
		qs = self.filter(product_content_type=c_type)

		if model_queryset:
			product_added_ids = [x.product_object_id for x in qs]
			return model_class.objects.filter(pk__in=product_added_ids)
		return qs


class CartItemManager(models.Manager):
	def get_queryset(self):
		return CartItemQueryset(self.model, using=self._db)


	def by_model(self, model_class, model_queryset=False):
		return self.get_queryset().by_model(model_class, model_queryset=model_queryset)

	def filter_by_instance(self, instance):
		product_content_type = ContentType.objects.get_for_model(instance.__class__)
		product_object_id = instance.id
		qs = super(CartItemManager, self).filter(product_content_type=product_content_type, product_object_id=product_object_id)
		return qs



class CartItem(models.Model):
	cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
	product_object_id = models.PositiveIntegerField()
	product_content_type = models.ForeignKey(
		ContentType,
		on_delete = models.CASCADE
		)
	product = GenericForeignKey("product_content_type", "product_object_id")

	quantite = models.PositiveIntegerField(default=1)

	objects = CartItemManager()


	def __str__(self):
		return ("{product}".format(product=self.product))



def pre_save_cart_item_receiver(sender, instance, *args, **kwargs):

	cart_item_added_signal.send_robust(sender= instance.__class__, instance=instance.cart, action="added")


def post_save_cart_item_receiver(sender, instance, *args, **kwargs):

	cart_item_added_signal.send_robust(sender= instance.__class__, instance=instance.cart, action="added")

def pre_delete_cart_item_receiver(sender, instance, *args, **kwargs):

	cart_item_added_signal.send_robust(sender= instance.__class__, instance=instance.cart, action="added")


def post_delete_cart_item_receiver(sender, instance, *args, **kwargs):
	cart_item_added_signal.send_robust(sender= instance.__class__, instance=instance.cart, action="added")


pre_save.connect(pre_save_cart_item_receiver, sender=CartItem)
post_save.connect(post_save_cart_item_receiver, sender=CartItem)
pre_delete.connect(pre_delete_cart_item_receiver, sender=CartItem)
post_delete.connect(post_delete_cart_item_receiver, sender=CartItem)


def cart_item_added_receiver(sender, instance,  action, *args, **kwargs):
	if action == "added" or action =="removed":
		somme = sum(item.product.price for item in instance.items.all())

		if instance.subtotal != somme:
			instance.subtotal = somme
			instance.save()




cart_item_added_signal.connect(cart_item_added_receiver)


