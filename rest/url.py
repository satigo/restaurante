from django.conf.urls import url
from . import views

urlpatterns = [
   
    url('menu/nuevo/', views.menu_nuevo, name='menu_nuevo'),
    ]