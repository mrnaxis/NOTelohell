from django.conf.urls import include, url
from django.contrib import admin
from usuarios import views

urlpatterns = [
    url(r'^$', views.loginC, name='login')
]
