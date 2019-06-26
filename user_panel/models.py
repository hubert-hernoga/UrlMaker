from django.db import models

class Urls(models.Model):
    url = models.CharField(max_length=100, null=True)
    short_url = models.CharField(max_length=80, null=True)

    def __str__(self):
        return '{}'.format(self.url)
