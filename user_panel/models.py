from django.db import models


class Url(models.Model):
    url = models.CharField(max_length=300, null=True)
    short_url = models.CharField(max_length=200, null=True)

    def __str__(self):
        return '{}'.format(self.url)
