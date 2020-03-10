from django.conf.urls import url, include
from dashboard import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url('', views.dashboard, name='dashboard'),
]
