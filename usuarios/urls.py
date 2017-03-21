from django.conf.urls import include, url, patterns
from usuarios import views

urlpatterns = patterns ('',
    url(r'^login/$', views.login, name='login'),
    url(r'^registrar/$', views.registrar, name='registrar'),
    url(r'^usuario/$', views.usuario, name='usuario')
)
