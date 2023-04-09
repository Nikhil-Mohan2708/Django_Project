from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views
app_name = 'flowerApp'

urlpatterns = [
    path('', views.home, name='home'),
    path('flowers/<int:flower_id>/', views.flower_details, name='flower_details'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('categories/', views.category_list, name='categories'),
    path('flowers_list/<slug:category_slug>/', views.flower_list, name='flower_list'),
    path('flower_list/<str:color>/', views.flower_list, name='flower_list_by_color'),

]
