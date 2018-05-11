from django import template
from ..models import Group

register = template.Library()

@register.filter(name='user_in_group')
def user_in_group(name_group):
    group = Group.objects.get(name=name_group)
    users = group.users.all()

    users = ", ".join([str(user) for user in users])

    return users