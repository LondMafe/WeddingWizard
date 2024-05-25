from django.contrib.auth import views as auth_views
from django.urls import path

from . import views
from .forms import LoginForm

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('services/', views.services, name='services'),
    path('signup/', views.signup, name='signup'),
    path('signup/vendors/', views.signupVendors, name='signupVendors'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html',authentication_form=LoginForm), name='login'),
]