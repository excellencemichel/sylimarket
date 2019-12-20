from django.shortcuts import render,  redirect, get_object_or_404
from django.urls import reverse, reverse_lazy

from django.contrib.contenttypes.models import ContentType

from django.contrib.auth.decorators import login_required

from django.contrib import messages



from .models import Categorie, Article

from .forms import ArticleForm
# Create your views here.




def home(request):
	articles = Article.objects.all()

	context={


		"articles": articles,
	}

	return render(request, "blogs/home.html", context)



@login_required
def create(request):
	categories = Categorie.objects.all()

	form = ArticleForm(request.POST or None, request.FILES or None)
	if form.is_valid():
	    title = form.cleaned_data.get("title")
	    content = form.cleaned_data.get("content")
	    image 	= form.cleaned_data.get("images")
	    instance = Article.objects.create(user=request.user, title=title, image = image, content=content)
	    instance.save()
	    messages.success(request, "Le blog a bien été créé")

	    return HttpResponseRedirect(instance.get_absolute_url())

	context = {
	    "form": form,
	    "categories": categories,
	}

	return render(request, "blogs/create.html", context)


def detail(request, id=None, slug=None):
    instance = get_object_or_404(Article, id=id, slug=slug)

    share_string = quote_plus(instance.content)

    initial_data = {
        "content_type": instance.get_content_type,
        "object_id": instance.id,
    }

    form = CommentForm(request.POST or None, initial=initial_data)
    if form.is_valid() and request.user.is_authenticated:
        c_type = form.cleaned_data.get("content_type")
        content_type = ContentType.objects.get(model=c_type)
        obj_id = form.cleaned_data.get("object_id")
        content_date = form.cleaned_data.get("content")

        parent_obj = None
        try:
            parent_id = int(request.POST.get("parent_id"))

        except:
            parent_id = None

        if parent_id:
            parent_qs = Comment.objects.filter(id=parent_id)

            if parent_qs.exists() and parent_qs.count() == 1:
                parent_obj = parent_qs.first()

        new_comment, created = Comment.objects.get_or_create(
            user=request.user,
            content_type=content_type,
            object_id=obj_id,
            content=content_date,
            parent=parent_obj,
        )

        return HttpResponseRedirect(new_comment.content_object.get_absolute_url())

    comments = instance.comments

    context = {
        "instance": instance,
        "comments": comments,
        "form": form,
        "share_string": share_string,
    }

    return render(request, "blogs/detail.html", context)

