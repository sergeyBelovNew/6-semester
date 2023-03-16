from django.urls import path
from . import views

urlpatterns = [
    path('/sdfesd', views.index_home, name='calculator_home'),
]