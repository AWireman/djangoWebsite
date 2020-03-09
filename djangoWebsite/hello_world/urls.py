from django.conf.urls import url
from hello_world import views

urlpatterns = [
        url('', views.hello_world, name='hello_world'),
]
