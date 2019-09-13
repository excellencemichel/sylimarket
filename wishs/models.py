from django.db import models
from django.conf import settings


from django.db.models.signals import pre_save, post_save

from django.urls import reverse

from utils.generator_utils import unique_slug_generator
from products.models import Product
# Create your models here.


User = settings.AUTH_USER_MODEL



class WishManager(models.Manager):

	def new_or_get(self, request):
		wish_id	= request.session.get("wish_id", None)
		qs	= self.get_queryset().filter(id=wish_id)
		if qs.count()==1:
			new_obj = False
			wish_obj	 = qs.first()
			if request.user.is_authenticated and wish_obj.user is None:
				wish_obj.user = request.user
				wish_obj.save()

		else:
			wish_obj = Wish.objects.new(user=request.user)
			new_obj = True
			request.session["wish_id"] = wish_obj.id
			


		return wish_obj, new_obj


	def new(self, user=None):
		user_obj	= None
		if user is not None:
			if user.is_authenticated:
				user_obj=user
		return self.model.objects.create(user=user_obj)


class Wish(models.Model):
	user 		= models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
	products    = models.ManyToManyField(Product, blank=True)
	updated		= models.DateTimeField(auto_now=True)
	timestamp	= models.DateTimeField(auto_now_add=True)

	objects		= WishManager()

	class Meta:
		ordering = ["-timestamp", "-updated"]
		verbose_name = "Souhait des utilisateurs "
		verbose_name_plural = "Souhaits des utilisateurs"





	def __str__(self):
		return str(self.user)























def tag_pre_save_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)



# pre_save.connect(tag_pre_save_receiver, sender=Tag)