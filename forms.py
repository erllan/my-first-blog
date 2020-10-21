from django import forms

from django import forms
from .models import Post


class DocumentForm(forms.Form):
    file = forms.FileField()
