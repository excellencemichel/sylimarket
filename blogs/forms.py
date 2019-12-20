from django.utils.translation import pgettext, ugettext, ugettext_lazy as _

from django import forms
from .models import Article



class ArticleForm(forms.Form):

    title = forms.CharField(label=_("Le titre de la publication"),
                            widget=forms.TextInput(attrs={"class": "form-control"}),
                            )

    content = forms.CharField(label=_("Contenu de la publication"),

                              help_text=_("Vous pouvez agrandir le la fenêtre"),
                              widget=forms.Textarea(attrs={"class": "form-control",
                                                           "rows": "3", "cols": "3" 
                                                           }
                                                    )
                              )


    images = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple':True}))
