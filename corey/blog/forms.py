from django import forms
from django.forms import ModelForm
from .models import Post


class blogwriter(ModelForm):
    class Meta:
        model=Post
        fields=["title","content","date_posted","author"]