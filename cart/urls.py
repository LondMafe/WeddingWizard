from django.urls import path
from . import views

urlpatterns = [
    path('', views.cartDetail, name='cartDetail'),
    path('add/', views.cartAdd, name='cartAdd'),
    path('delete/', views.cartDelete, name='cartDelete'),
]