from django.shortcuts import render
from django.views import View
from .forms import UserForm
from django.shortcuts import redirect
from django.contrib.auth.models import User


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

#
# class CheckoutAddress(View):
#     def get(self, request, user_id):
#         if user_id:
#             logged_user = User.objects.get(pk=user_id)
#             logged_user_form = UserForm(user_id=user_id,
#                                         initial={
#                 'first_name': logged_user.first_name,
#                 'last_name': logged_user.last_name,
#                 'email': logged_user.email,
#                 'phone_number': logged_user.profile.phone_number,
#                 'company': logged_user.profile.company,
#                 'country': logged_user.profile.country,
#                 'city': logged_user.profile.city,
#                 'postal_code': logged_user.profile.postal_code,
#                 'address1': logged_user.profile.address1,
#                 'address2': logged_user.profile.address2
#             })
#
#             shipping_cost = 0
#             if 'shipping' in request.session.keys():
#                 shipping_id = request.session['shipping']['shipping_method_id']
#                 shipping = ShippingOption.objects.get(pk=shipping_id)
#                 shipping_cost += shipping.cost
#
#             ctx = {
#                 'products_amount': request.session['basket'],
#                 'logged_user': logged_user.id,
#                 'user_form': logged_user_form,
#                 'shipping_cost': format(shipping_cost, '.2f')
#             }
#
#         else:
#             ctx = {
#                 'products_amount': request.session['basket'],
#                 'user_form': UserForm(user_id=user_id),
#                 'shipping_cost': format(0, '.2f')
#             }
#         return render(request, 'checkout-address.html', ctx)

#     def post(self, request, user_id):
#         user_form = UserForm(request.POST or None, user_id=user_id)
#         if user_form.is_valid():
#             if user_id:
#                 user = User.objects.get(pk=user_id)
#             else:
#                 user = User(username=user_form.cleaned_data['email'], email=user_form.cleaned_data['email'])
#                 user.save()
#                 user = User.objects.get(email=user_form.cleaned_data['email'])
#
#             user.first_name = user_form.cleaned_data['first_name']
#             user.last_name = user_form.cleaned_data['last_name']
#             user.profile.phone_number = user_form.cleaned_data['phone_number']
#             user.profile.company = user_form.cleaned_data['company']
#             user.profile.country = user_form.cleaned_data['country']
#             user.profile.city = user_form.cleaned_data['city']
#             user.profile.postal_code = user_form.cleaned_data['postal_code']
#             user.profile.address1 = user_form.cleaned_data['address1']
#             user.profile.address2 = user_form.cleaned_data['address2']
#             user.save()
#
#             return redirect('/checkout_shipping/{}'.format(user.id))
#         ctx = {
#             'products_amount': request.session['basket'],
#             'user_form': user_form,
#             'shipping_cost': format(0, '.2f')
#         }
#         return render(request, 'checkout-address.html', ctx)