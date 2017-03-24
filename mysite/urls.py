from django.conf.urls import include, url
from django.contrib import admin

from blog import views

urlpatterns = [
    url(r'^login/$', 'django.contrib.auth.views.login', {
        'template_name': 'admin\login.html'
    }, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {
        'template_name': 'admin\home.html'
    }, name='logout'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('blog.urls')),
    ]