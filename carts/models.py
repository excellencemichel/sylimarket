from decimal import Decimal 


from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save, post_save, m2m_changed, pre_delete, post_delete
from django.db.models import  F 


from .signals import cart_item_added_signal
from utils.decimal_utils import multiplier, diviser, TWOPLACES


from products.models import Product
# Create your models here.


User = settings.AUTH_USER_MODEL


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
				user_obj=user_obj
		return self.model.objects.create(user=user_obj)

class Cart(models.Model):
	user 		= models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
	subtotal 	= models.DecimalField(default=0.00, max_digits=100, decimal_places =2 )
	total 		= models.DecimalField(default=0.00, max_digits=100, decimal_places =2 )

	updated		= models.DateTimeField(auto_now=True)
	timestamp	= models.DateTimeField(auto_now_add=True)


	objects		= CartManager()




	def __str__(self):
		return ("Panier de:  {user} coûte : {total}".format(user=self.user, total=self.total))








	def add_item(self, product, *args, **kwargs)->"CartItem":
		product = Product.objects.get(id=product.id)

		cart_item_obj = CartItem.objects.create(
			cart=self,
			product = product,
			)
		cart_item_obj.save()
		cart_item_added_signal.send_robust(sender= self.__class__, instance=self, action="added")
		product.stock = F('stock') - 1
		product.save()

		return cart_item_obj


	def remove_item(self, product, *args, **kwargs)->"CartItem":
		product = Product.objects.get(id=product.id)
		try:
			cart_item_obj = CartItem.objects.get(product_id=product.id)
			cart_item_obj.delete()
			product.stock = F('stock') + 1
			product.save()
		except CartItem.MultipleObjectsReturned:
			cart_item_obj = CartItem.objects.filter(product_id=product.id).first()
			cart_item_obj.delete()
			product.stock = F('stock') + 1
			product.save()
		except CartItem.DoesNotExist:
			pass
	
		cart_item_added_signal.send_robust(sender= self.__class__, instance=self, action="removed")



	








def pre_save_cart_receiver(sender, instance,*args, **kwargs):
	if instance.subtotal > 0:
		instance.total = multiplier(instance.subtotal, Decimal(1.08).quantize(TWOPLACES))# + 1.3
	else:
		instance.total = 0.00



pre_save.connect(pre_save_cart_receiver, sender=Cart)





class CartItem(models.Model):
	cart 		= models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
	product		= models.ForeignKey(Product, on_delete=models.CASCADE, related_name="products" )


	def __str__(self):
		return ("{product}".format(product=self.product))





def pre_save_cart_item_receiver(sender, instance, *args, **kwargs):

	cart_item_added_signal.send_robust(sender= instance.__class__, instance=instance.cart, action="added")


def post_save_cart_item_receiver(sender, instance, *args, **kwargs):

	cart_item_added_signal.send_robust(sender= instance.__class__, instance=instance.cart, action="added")

def pre_delete_cart_item_receiver(sender, instance, *args, **kwargs):

	cart_item_added_signal.send_robust(sender= instance.__class__, instance=instance.cart, action="removed")


def post_delete_cart_item_receiver(sender, instance, *args, **kwargs):
	cart_item_added_signal.send_robust(sender= instance.__class__, instance=instance.cart, action="removed")


pre_save.connect(pre_save_cart_item_receiver, sender=CartItem)
# post_save.connect(post_save_cart_item_receiver, sender=CartItem)
pre_delete.connect(pre_delete_cart_item_receiver, sender=CartItem)
# post_delete.connect(post_delete_cart_item_receiver, sender=CartItem)


def cart_item_added_receiver(sender, instance,  action, *args, **kwargs):
	if action == "added" or action == "removed":
		somme = sum(item.product.price for item in instance.items.all())
		print("La somme est : ", somme)

		if instance.subtotal != somme:
			instance.subtotal = somme
			instance.save()




cart_item_added_signal.connect(cart_item_added_receiver)