from django import forms
from .models import x

class xform(forms.ModelForm):
    class meta:
        model = x
        fields =['text','photo']