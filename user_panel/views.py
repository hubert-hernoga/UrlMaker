from urllib.parse import urlsplit
from django.views import View
from django.shortcuts import render
from django.shortcuts import redirect

from .forms import  UrlForm
from .models import Url


class UrlMaker(View):
    def get(self, request):
        url_form = UrlForm()

        ctx = {
            'url_form': url_form
        }
        return render(request, 'add_url.html', ctx)

    def post(self, request):
        url_form = UrlForm(request.POST)


        user_url = self.user_url(url_form)
        short_url = self.shorten_url(user_url)

        db_url = Url.objects.create(url=user_url)
        db_url.short_url = short_url
        db_url.save()

        return redirect('/urls_list')


    def user_url(self, url_form):
        if url_form.is_valid():
            return url_form.cleaned_data['url']

    def shorten_url(self, url):
        parsed_uri = urlsplit(str(url))
        domain = parsed_uri.netloc
        path = parsed_uri.path

        return domain + path[:5]


class UrlsList(View):
    def get(self, request):
        url = Url.objects.latest('id')

        ctx = {
            'url': url
        }
        return render(request, 'urls_list.html', ctx)
