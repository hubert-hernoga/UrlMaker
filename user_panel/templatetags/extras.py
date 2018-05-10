from django import template
from ..models import Groups

register = template.Library()

@register.filter(name='user_in_group')
def user_in_group(name_group):
    group = Groups.objects.get(name=name_group)
    users = group.users.all()

    users = ", ".join([str(user) for user in users])

    return users