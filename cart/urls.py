from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('detail/', views.cartDetail, name='cartDetail'),
    path('add/', views.cartAdd, name='cartAdd'),
    path('delete/', views.cartDelete, name='cartDelete'),
    path('update/', views.cartUpdate, name='cartUpdate'),
]