from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', default=None)
    birth_date = models.DateField(default=None)
    list_groups = models.CharField(max_length=64, null=True)

class UserGroups(models.Model):
    name = models.CharField(max_length=24, null=True)
    users = models.ManyToManyField(Profile, related_name='groups')