from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('intro', views.index_intro, name='intro'),
    path('docs', views.index_docs, name='docs'),
    path('about', views.index_about, name='about'),
    path('other', views.index_other, name='other'),
]
