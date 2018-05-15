"""management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from user_panel.views import MainPage, UserList, AddUser, GroupsList, AddGroup
from django.conf.urls import url


urlpatterns = [
    path('admin/', admin.site.urls),
    url('^$', UserList.as_view(), name='user_list'),
    url('add_user/(?P<user_id>(\d)+|)', AddUser.as_view(), name='add_user'),
    url('add_group/(?P<group_id>(\d)+|)', AddGroup.as_view(), name='add_group'),
    url('groups_list/', GroupsList.as_view(), name='groups_list')
]
