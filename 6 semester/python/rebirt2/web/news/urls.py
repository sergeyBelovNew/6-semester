from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_news, name='news_home'),
    path('create', views.index_create, name='create_news'),
    path('<int:pk>', views.NewsDetailView.as_view(), name='detail_news'),
    path('<int:pk>/update', views.NewsUpdateView.as_view(), name='update_news'),
    path('<int:pk>/delete', views.NewsDeleteView.as_view(), name='delete_news')
]
