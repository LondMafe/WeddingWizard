from django.contrib import admin
from .models import CreditCard

class CreditCard(admin.ModelAdmin):
    list_display = ('cardNumber', 'expirationDate', 'cvv', 'cardHolder', 'user')
