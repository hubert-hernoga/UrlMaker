from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
import datetime



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', default=None)
    birth_date = models.DateField(default=datetime.date.today)
    list_groups = models.CharField(max_length=64, null=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def update_profile(request, user_id):
        user = User.objects.get(pk=user_id)
        user.save()


class UserGroups(models.Model):
    name = models.CharField(max_length=24, null=True)
    users = models.ManyToManyField(Profile, related_name='groups')