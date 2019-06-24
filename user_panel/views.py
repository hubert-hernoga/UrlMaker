from django.views import View
from django.shortcuts import render

from django.contrib.auth.models import User
from .forms import UserForm, UrlForm
from .models import Url

from django.shortcuts import redirect
from django.http import QueryDict
#
#
# class UserList(View):
#     def get(self, request):
#         users = User.objects.all()
#         groups = Group.objects.all()
#
#         ctx = {
#             'users': users,
#             'groups': groups
#         }
#         return render(request, 'user_list.html', ctx)
#
#     def delete(self, request):
#         user_id = QueryDict(request.body).get('user_id')
#         User.objects.get(pk=user_id).delete()
#
#         return redirect('/')
#
#
# class AddUser(View):
#     def get(self, request, user_id):
#         if user_id:
#             user_groups = Group.objects.filter(users=user_id)
#             selected_user = User.objects.get(pk=user_id)
#
#             selected_user_form = UserForm(user_id=user_id,
#                                           initial={
#                 'username': selected_user.username,
#                 'first_name': selected_user.first_name,
#                 'last_name': selected_user.last_name,
#                 'email': selected_user.email,
#                 'birth_date': selected_user.profile.birth_date
#             })
#
#             ctx = {
#                 'user_form': selected_user_form,
#                 'user_groups': user_groups
#             }
#         else:
#             user_form = UserForm(user_id=user_id)
#
#             ctx = {
#                 'user_form': user_form
#             }
#         return render(request, 'add_user.html', ctx)
#
#     def post(self, request, user_id):
#         user_form = UserForm(request.POST or None, user_id=user_id)
#         if user_form.is_valid():
#             if user_id:
#                 user = User.objects.get(pk=user_id)
#             else:
#                 user = User.objects.create_user(username=user_form.cleaned_data['username'],
#                                                 password=user_form.cleaned_data['password'])
#                 user.save()
#                 user = User.objects.get(username=user_form.cleaned_data['username'])
#
#             user.first_name = user_form.cleaned_data['first_name']
#             user.last_name = user_form.cleaned_data['last_name']
#             user.profile.birth_date = user_form.cleaned_data['birth_date']
#             user.save()
#
#             return redirect('/')
#
#         ctx = {
#             'user_form': user_form,
#         }
#         return render(request, 'add_user.html', ctx)
#

class GroupsList(View):
    def get(self, request):
        groups = Url.objects.all()

        ctx = {
            'groups': groups
        }
        return render(request, 'groups_list.html', ctx)

    def delete(self, request):
        group_id = QueryDict(request.body).get('group_id')
        Url.objects.filter(pk=group_id).delete()

        return redirect('/groups_list')


class UrlMaker(View):
    def get(self, request):
        group_form = UrlForm()

        ctx = {
            'group_form': group_form
        }
        return render(request, 'add_group.html', ctx)

    def post(self, request):
        group_form = UrlForm(request.POST)
        print("===================")

        if group_form.is_valid():
            url = group_form.cleaned_data['url']

            # if group_id:
            #     group = Url.objects.get(pk=group_id)
            #     group.url = group_form.cleaned_data['url']
            #     group.save()
            # else:
            group = Url.objects.create(url=url)
            group.save()

            return redirect('/groups_list')

        ctx = {
            'group_form': group_form,
        }
        return render(request, 'add_group.html', ctx)