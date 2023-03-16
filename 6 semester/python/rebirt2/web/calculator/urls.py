from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_main, name='calculator'),
    path('create', views.index_create, name='create'),
    path('<int:pk>', views.NewsDetailView.as_view(), name='detail_equipment'),
    path('<int:pk>/update', views.NewsUpdateView.as_view(), name='update_equipment'),
    path('<int:pk>/delete', views.NewsDeleteView.as_view(), name='delete_equipment')
]
