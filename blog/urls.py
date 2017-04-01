from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^(?P<user_name>\w+)/$', views.account, name='account'),
    url(r'^(?P<user_name>\w+)/post/new/$', views.post_new, name='post_new'),
    url(r'^(?P<user_name>\w+)/post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^$', views.blog_list, name='home'),
]