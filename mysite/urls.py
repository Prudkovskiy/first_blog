from django.conf.urls import include, url
from django.contrib import admin

from blog import views

urlpatterns = [
    url(r'^login/$', views.my_login, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {
        'template_name': 'admin\home.html'
    }, name='logout'),
    url(r'^signup/', views.sign_up, name='signup'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('blog.urls')),
    ]