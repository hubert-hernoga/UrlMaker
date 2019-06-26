from django.views import View
from django.shortcuts import render
from django.shortcuts import redirect

from .forms import  UrlForm
from .models import Url


class UrlsList(View):
    def get(self, request):
        url = Url.objects.latest('id')

        ctx = {
            'url': url
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
        url = self.user_url(request)
        db_url = Url.objects.create(url=url)
        db_url.save()

        short_url = self.shorten_url(url)
        db_url = Url.objects.create(short_url=short_url)
        db_url.save()

        return redirect('/urls_list')

    def user_url(self, request):
        url_form = UrlForm(request.POST)
        if url_form.is_valid():
            return url_form.cleaned_data['url']

    def shorten_url(self, url):
        return url.upper()