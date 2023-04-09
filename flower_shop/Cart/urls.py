from django.urls import path
from . import views
app_name = 'Cart'

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add/<int:flower_id>/', views.add_cart, name='add_cart'),
    path('remove/<int:flower_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('delete_cart/<int:flower_id>/', views.delete_cart, name='delete_cart'),
    path('get_cities/', views.get_cities, name='get_cities'),
    path('success/', views.success, name='success'),
    path('order_placed/', views.order_placed, name='order_placed'),

]
