from django.conf.urls import include, url, patterns
from usuarios import views
from views import RegistrarView

urlpatterns = patterns ('',
    url(r'^login/$', views.login, name='login'),
    url(r'^registrar/$', RegistrarView.as_view(), name='registrar'),
    url(r'^usuario/$', views.usuario, name='usuario')
)
