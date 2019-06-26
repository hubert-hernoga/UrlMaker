from django.contrib import admin
from .models import Urls

class UrlsAdmin(admin.ModelAdmin):

    list_display = ['id', 'url', 'short_url']

admin.site.register(Urls, UrlsAdmin)