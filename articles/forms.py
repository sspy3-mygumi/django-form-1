from django import forms
from .models import Article

# class ArticleForm(forms.Form)
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content',]