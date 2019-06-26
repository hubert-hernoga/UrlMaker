from django import forms
from .models import Url


class UserForm(forms.ModelForm):
    pass


class UrlForm(forms.ModelForm):
    url = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'url'}))

    class Meta:
        model = Url
        fields = ['url']

    def clean_url(self):
        url = self.cleaned_data['url']
        if not url:
            raise forms.ValidationError('This field can not be empty')
        return url