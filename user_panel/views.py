from urllib.parse import urlparse
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
        url_form = UrlForm()

        ctx = {
            'url_form': url_form
        }
        return render(request, 'add_url.html', ctx)

    def post(self, request):
        url_form = UrlForm(request.POST)

        try:
            url = self.user_url(url_form)
            print('=============================')
            print(url)
            url = Url.objects.create(url=url)


            short_url = self.shorten_url(url)
            print('=============================')
            print(short_url)
            db_url = Url.objects.create(short_url=short_url)
            url.save()
            db_url.save()

            return redirect('/urls_list')

        except:
            print('=============================')
            print('=============================')
            ctx = {
                'url_form': url_form,
            }
            return render(request, 'add_url.html', ctx)

    def user_url(self, url_form):
        if url_form.is_valid():
            return url_form.cleaned_data['url']

    def shorten_url(self, url):
        parsed_uri = urlparse(url)
        domain = parsed_uri.netloc
        path = parsed_uri.path

        return domain + path[:5]
