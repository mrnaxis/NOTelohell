from django.conf.urls import include, url, patterns
from dashboard import views

urlpatterns = patterns ('',
    url(r'^$', views.dashboard, name="dashboard"),
)
