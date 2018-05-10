from django.shortcuts import render
from django.views import View
from .forms import UserForm, UserGroupsForm
from .models import Groups, Profile
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.http import QueryDict


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

    def delete(self, request):
        user_id = QueryDict(request.body).get('user_id')
        User.objects.filter(pk=user_id).delete()

        return redirect('/user_list')


class AddUser(View):
    def get(self, request, user_id):
        if user_id:
            selected_user = User.objects.get(pk=user_id)
            selected_user_form = UserForm(initial={
                'username': selected_user.username,
                'first_name': selected_user.first_name,
                'last_name': selected_user.last_name,
                'birth_date': selected_user.profile.birth_date,
                'list_groups': selected_user.profile.list_groups
            })

            ctx = {
                'user_form': selected_user_form
            }
        else:
            user_form = UserForm()

            ctx = {
                'user_form': user_form
            }
        return render(request, 'add_user.html', ctx)

    def post(self, request, user_id):
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            if user_id:
                user = User.objects.get(pk=user_id)
            else:
                user = User.objects.create_user(username=user_form.cleaned_data['username'],
                                                password=user_form.cleaned_data['password'])
                user.save()
                user = User.objects.get(username=user_form.cleaned_data['username'])

            user.first_name=user_form.cleaned_data['first_name']
            user.last_name=user_form.cleaned_data['last_name']
            user.profile.birth_date = user_form.cleaned_data['birth_date']
            user.profile.list_groups = user_form.cleaned_data['list_groups']
            user.save()

            return redirect('/user_list')

        ctx = {
            'user_form': user_form,
        }
        return render(request, 'add_user.html', ctx)


class GroupsList(View):
    def get(self, request):
        groups = Groups.objects.all()

        ctx = {
            'groups': groups
        }
        return render(request, 'groups_list.html', ctx)


class AddGroup(View):
    def get(self, request):
        group_form = UserGroupsForm()

        ctx = {
            'group_form': group_form
        }
        return render(request, 'add_group.html', ctx)

    def post(self, request):
        group_form = UserGroupsForm(request.POST)
        if group_form.is_valid():
            group = Groups.objects.create(name=group_form.cleaned_data['name'])
            group.save()

            users = group_form.cleaned_data['users']
            for user in users:
                group.users.add(user)

            return redirect('/groups_list')

        ctx = {
            'group_form': group_form,
        }
        return render(request, 'add_group.html', ctx)