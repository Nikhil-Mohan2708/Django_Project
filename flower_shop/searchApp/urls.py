from django.urls import path
from . import views
app_name = 'searchApp'

urlpatterns = [
    path('search/', views.SearchResult, name='search')
]