from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.detail_cart, name='detail_cart'),
    path('add/<int:equipment_id>', views.add_to_cart, name='add_cart'),
    path('remove/<int:equipment_id>', views.remove_cart, name='remove_cart'),

]
