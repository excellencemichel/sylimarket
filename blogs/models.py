from django.db import models

from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
from django.db.models.signals import pre_save
from django.utils import timezone

from utils.generator_utils import unique_slug_generator
from utils.files_utils import upload_file_blog



from comments.models import Comment

# Create your models here.


class Categorie(models.Model):
	name = models.CharField(max_length=1000)

	def __str__(self):
		return f"Catégorie {self.name}"


class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    title = models.CharField(max_length=1000)
    slug = models.SlugField()


    image = models.FileField(upload_to=upload_file_blog)
    content = models.TextField()

    created = models.DateTimeField(auto_now=False, auto_now_add=True)

    updated = models.DateTimeField(auto_now=True, auto_now_add=False)




    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blogs:detail", kwargs={"id": self.id, "slug": self.slug})

    @property
    def comments(self):
        instance = self
        qs = Comment.objects.filter_by_instance(instance)
        return qs

    @property
    def get_content_type(self):
        instance = self
        content_type = ContentType.objects.get_for_model(instance.__class__)
        return content_type

    class Meta:
        ordering = ["-created", "-updated"]


def article_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)



pre_save.connect(article_pre_save_receiver, sender=Article)





