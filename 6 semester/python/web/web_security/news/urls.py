from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_news, name='news_home'),
    path('create', views.index_create, name='create'),
]
