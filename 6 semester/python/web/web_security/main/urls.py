from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_main, name='home'),
    path('intro', views.index_intro, name='intro'),
    path('general_docs', views.index_general_docs, name='general_docs'),
    path('docs', views.index_docs, name='docs'),
    path('about', views.index_about, name='about'),
    path('other', views.index_other, name='other'),
]
