from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'notEL.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include('usuarios.urls')),
    url(r'^', include('dashboard.urls')),
]
