from django import forms
from .models import Tweet

class xform(forms.ModelForm):
    class Meta:
        model = Tweet
        fields =['text','photo']