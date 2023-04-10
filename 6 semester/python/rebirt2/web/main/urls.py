from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_main, name='home'),
    path('about', views.index_about, name='about'),
]
