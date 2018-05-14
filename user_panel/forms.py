from django import forms
from django.forms import ModelForm
from .models import Profile, Group
from django.core.exceptions import ValidationError
from .validators import email_validator

class UserForm(forms.ModelForm):
    username = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'username' }))
    first_name = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'first_name'}))
    last_name = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'last_name'}))
    e_mail = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'e-mail'}))
    password = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'password'}))
    repeat_password = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'repeat_password'}))

    class Meta:
        model = Profile
        fields = ['username', 'first_name', 'last_name', 'e_mail', 'birth_date',
                  'password', 'repeat_password']


    def clean_username(self):
        username = self.cleaned_data['username']

        if not username:
            raise forms.ValidationError('The field can not be empty')
        elif not username.isalpha():
            raise ValidationError("Only alphanumeric characters are allowed.")
        return username

    def clean_email(self):
        user_email = self.cleaned_data['email']

        if not user_email:
            raise forms.ValidationError('The field can not be empty')
        elif self.logged_user_id:
            logged_email = User.objects.get(pk=self.logged_user_id).email
            return email_validator(user_email, logged_email)
        return email_validator(user_email)

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