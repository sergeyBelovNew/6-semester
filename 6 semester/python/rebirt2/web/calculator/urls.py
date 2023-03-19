from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_main, name='calculator'),
    path('create', views.index_create, name='create'),
    path('<int:pk>', views.CalculatorDetailView.as_view(), name='detail_equipment'),
    path('<int:pk>/update', views.CalculatorUpdateView.as_view(), name='update_equipment'),
    path('<int:pk>/delete', views.CalculatorDeleteView.as_view(), name='delete_equipment')
]
