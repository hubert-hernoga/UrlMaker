from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', default=None)
    birth_date = models.DateField(default='1111-11-11')

    def __str__(self):
        return '{}'.format(self.user.username)

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

class Group(models.Model):
    name = models.CharField(max_length=24, null=True)
    users = models.ManyToManyField(User, related_name='users')

    def __str__(self):
        return '{}'.format(self.name)