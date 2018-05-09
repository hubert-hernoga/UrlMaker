from django.shortcuts import render
from django.views import View
from .forms import UserForm
from django.shortcuts import redirect
from django.contrib.auth.models import User
from .models import Profile

class MainPage(View):
    def get(self, request):
        return render(request, 'main_page.html')


class UserList(View):
    def get(self, request):
        users = User.objects.all()

        ctx = {
            'users': users
        }
        return render(request, 'user_list.html', ctx)


class AddUserList(View):
    def get(self, request):
        user_form = UserForm()
        ctx = {
            'user_form': user_form
        }
        return render(request, 'add_user.html', ctx)

    def post(self, request):
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user = User.objects.create_user(username=user_form.cleaned_data['username'],
                                            first_name=user_form.cleaned_data['first_name'],
                                            last_name=user_form.cleaned_data['last_name'],
                                            password=user_form.cleaned_data['password'])
            user.save()

            user = User.objects.get(username=user_form.cleaned_data['username'])
            user.profile.birth_date = user_form.cleaned_data['birth_date']
            user.profile.list_groups = user_form.cleaned_data['list_groups']
            user.save()

            return redirect('/user_list')

        ctx = {
            'user_form': user_form,
        }
        return render(request, 'add_user.html', ctx)