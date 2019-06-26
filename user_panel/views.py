from django.views import View
from django.shortcuts import render
from django.shortcuts import redirect

from .forms import  UrlForm
from .models import Urls


class UrlsList(View):
    def get(self, request):
        url = Urls.objects.latest('id')

        ctx = {
            'urls': url
        }
        return render(request, 'urls_list.html', ctx)


class UrlMaker(View):
    def get(self, request):
        group_form = UrlForm()

        ctx = {
            'group_form': group_form
        }
        return render(request, 'add_group.html', ctx)

    def post(self, request):
        group_form = UrlForm(request.POST)

        if group_form.is_valid():
            url = group_form.cleaned_data['url']
            group = Urls.objects.create(url=url)
            group.save()

            return redirect('/urls_list')

        ctx = {
            'group_form': group_form,
        }
        return render(request, 'add_group.html', ctx)