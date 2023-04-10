from django.urls import path
from . import views

urlpatterns = [

    path('', views.index_general_docs, name='general_docs'),

]
