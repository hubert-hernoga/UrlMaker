from django.views import View
from django.shortcuts import render

from django.contrib.auth.models import User
from .forms import UserForm, GroupForm
from .models import Group

from django.shortcuts import redirect
from django.http import QueryDict


class MainPage(View):
    def get(self, request):
        return render(request, 'user_list.html')


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

        return redirect('/')


class AddUser(View):
    def get(self, request, user_id):
        if user_id:
            user_groups = Group.objects.filter(users=user_id)
            selected_user = User.objects.get(pk=user_id)

            selected_user_form = UserForm(initial={
                'username': selected_user.username,
                'first_name': selected_user.first_name,
                'last_name': selected_user.last_name,
                'birth_date': selected_user.profile.birth_date
            })

            ctx = {
                'user_form': selected_user_form,
                'user_groups': user_groups
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

            user.first_name = user_form.cleaned_data['first_name']
            user.last_name = user_form.cleaned_data['last_name']
            user.profile.birth_date = user_form.cleaned_data['birth_date']
            user.save()

            return redirect('/user_list')

        ctx = {
            'user_form': user_form,
        }
        return render(request, 'add_user.html', ctx)


class GroupsList(View):
    def get(self, request):
        groups = Group.objects.all()

        ctx = {
            'groups': groups
        }
        return render(request, 'groups_list.html', ctx)

    def delete(self, request):
        group_id = QueryDict(request.body).get('group_id')
        Group.objects.filter(pk=group_id).delete()

        return redirect('/groups_list')


class AddGroup(View):
    def get(self, request, group_id):
        if group_id:
            selected_group = Group.objects.get(pk=group_id)
            selected_group_form = GroupForm(initial={
                'name': selected_group.name,
            })

            ctx = {
                'group_form': selected_group_form['name'],
                'users': selected_group.users.all()
            }
        else:
            group_form = GroupForm()

            ctx = {
                'group_form': group_form
            }
        return render(request, 'add_group.html', ctx)

    def post(self, request, group_id):
        group_form = GroupForm(request.POST)
        if group_form.is_valid():
            if group_id:
                group = Group.objects.get(pk=group_id)
                group.name = group_form.cleaned_data['name']
                group.save()
            else:
                group = Group.objects.create(name=group_form.cleaned_data['name'])
                group.save()

            users = group_form.cleaned_data['users']
            for user in users:
                group.users.add(user)

            return redirect('/groups_list')

        ctx = {
            'group_form': group_form,
        }
        return render(request, 'add_group.html', ctx)