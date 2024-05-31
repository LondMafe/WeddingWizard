from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'payments'

urlpatterns = [
    path('', views.payments, name='payment'),
    path('creditCardPayment/', views.creditCardPayment, name='creditCardPayment'),
    path('paymentDone/', views.paymentDone, name='paymentDone'),
]
