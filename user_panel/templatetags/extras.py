from django import template
from ..models import Url

register = template.Library()

@register.filter(name='user_in_group')
def user_in_group(name_group):
    print(name_group)
    group = Url.objects.get(result=name_group)
    users = group.users.all()

    return ", ".join([str(user) for user in users])

@register.filter(name='user_groups')
def user_groups(groups, user):
    groups_list = []
    for group in groups:
        if group.users.filter(pk=user.id):
            groups_list.append(group.name)
    return ", ".join([str(group) for group in groups_list])
