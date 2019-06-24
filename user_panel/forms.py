from django import forms
from django.contrib.auth.models import User
from .models import Profile, Group
from django.core.exceptions import ValidationError
from .validators import email_validator


class UserForm(forms.ModelForm):
    pass


class GroupForm(forms.ModelForm):
    url = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'url'}))

    class Meta:
        model = Group
        fields = ['url']

    def clean_name(self):
        name = self.cleaned_data['url']

        if not name:
            raise forms.ValidationError('The field can not be empty')
        return name