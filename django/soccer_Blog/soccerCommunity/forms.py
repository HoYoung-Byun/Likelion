from django import forms
from .models import community

class ArticleForm(forms.ModelForm):

    class Meta:
        model = community
        fields = ['title', 'body', 'image']