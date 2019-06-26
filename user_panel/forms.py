from django import forms
from .models import Urls


class UserForm(forms.ModelForm):
    pass


class UrlForm(forms.ModelForm):
    url = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'url'}))

    class Meta:
        model = Urls
        fields = ['url']
