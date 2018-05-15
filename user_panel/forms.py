from django import forms
from django.contrib.auth.models import User
from .models import Profile, Group
from django.core.exceptions import ValidationError
from .validators import email_validator


class UserForm(forms.ModelForm):
    username = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'username' }))
    first_name = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'first_name'}))
    last_name = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'last_name'}))
    birth_date = forms.DateField(required=False, widget=forms.TextInput(attrs={'class': 'form-control ', 'id': 'birth_date', 'placeholder': 'YYYY-MM-DD'}))
    email = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'e-mail'}))
    password = forms.CharField(required=False, widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'password'}))
    repeat_password = forms.CharField(required=False, widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'repeat_password'}))

    class Meta:
        model = Profile
        fields = ['username', 'first_name', 'last_name', 'email', 'birth_date',
                  'password', 'repeat_password']


    def clean_username(self):
        username = self.cleaned_data['username']

        if not username:
            raise forms.ValidationError('The field can not be empty')
        if User.objects.filter(username=username).exists():
            raise ValidationError("Username: {} already exist!".format(username))
        return username

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']

        if not first_name:
            raise forms.ValidationError('The field can not be empty')
        elif not first_name.isalpha():
            raise ValidationError("Only alphanumeric characters are allowed.")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']

        if not last_name:
            raise forms.ValidationError('The field can not be empty')
        elif not last_name.isalpha():
            raise ValidationError("Only alphanumeric characters are allowed.")
        return last_name

    def clean_birth_date(self):
        birth_date = self.cleaned_data['birth_date']

        if not birth_date:
            raise forms.ValidationError('The field can not be empty')
        return birth_date


    def clean_email(self):
        user_email = self.cleaned_data['email']

        if not user_email:
            raise forms.ValidationError('The field can not be empty')
        return email_validator(user_email)

    def clean_repeat_password(self):
        password1 = self.cleaned_data['password']
        password2 = self.cleaned_data['repeat_password']
        if not password1:
            raise forms.ValidationError('The field can not be empty')
        if not password2:
            raise forms.ValidationError('The field can not be empty')
        if password1 != password2:
            raise ValidationError("Passwords should be identical.")
        return password1


class GroupForm(forms.ModelForm):
    name = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'name'}))
    users = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple(), queryset=User.objects.all())

    class Meta:
        model = Group
        fields = ['name', 'users']

    def clean_name(self):
        name = self.cleaned_data['name']

        if not name:
            raise forms.ValidationError('The field can not be empty')
        return name