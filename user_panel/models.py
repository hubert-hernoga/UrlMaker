from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
import datetime

class Url(models.Model):
    url = models.CharField(max_length=24, null=True)

    def __str__(self):
        return '{}'.format(self.url)