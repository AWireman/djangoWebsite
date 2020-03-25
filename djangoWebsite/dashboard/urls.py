from django.conf.urls import url, include
from dashboard import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^/redirect$', views.redirect, name='redirect'),
    url(r'^/site$', views.site, name='site'),
    #url('site', TemplateView.as_view(template_name="http://google.com")),
]
