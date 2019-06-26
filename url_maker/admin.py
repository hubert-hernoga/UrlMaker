from django.contrib import admin
from .models import Url
from django.utils.html import format_html

class UrlAdmin(admin.ModelAdmin):
    list_display = ['url', 'interactive_url']

    def interactive_url(self, obj):
        return format_html(
            '<a href="{url}">{short_url}</a>'.format(
                url=obj.url,
                short_url=obj.short_url
        ))

    interactive_url.allow_tags = True

admin.site.register(Url, UrlAdmin)