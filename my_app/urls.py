from django.urls import path
from . import views
from django.contrib import admin
import my_app

urlpatterns = [
    path('', views.home, name='home'),
    path('new_search', views.new_search ,  name='new_search'),
    path('admin/', admin.site.urls)
]