from django import forms
from django.forms import ModelForm
from .models import Profile, Group, GroupMember
from django.core.exceptions import ValidationError


class UserForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput)
    first_name = forms.CharField(widget=forms.TextInput)
    last_name = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput())
    repeat_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Profile
        fields = ['username', 'first_name', 'last_name', 'birth_date',
                  'password', 'repeat_password']


    def clean_repeat_password(self):
        password1 = self.cleaned_data['password']
        password2 = self.cleaned_data['repeat_password']
        if password1 != password2:
            raise ValidationError("Passwords should be identical.")
        return password1


class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'users']