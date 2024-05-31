from django.db import models

# Create your models here.

class CreditCard(models.Model):
    cardNumber = models.CharField(max_length=16)
    expirationDate = models.CharField(max_length=7)  # Format: MM/YYYY
    cvv = models.CharField(max_length=3)
    cardHolder = models.CharField(max_length=100)
    user = models.ForeignKey('core.CustomUser', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.cardNumber
