from .models import Hashtag, Rubrika, Article
from django import forms
from django.forms import ModelForm

class HashtagForm(ModelForm):
    class Meta:
        model = Hashtag
        fields=['title']

class RubrikaForm(ModelForm):
    class Meta:
        model = Rubrika
        fields=['title']

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'