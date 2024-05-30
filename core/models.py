from django.db import models
from django.contrib.auth.models import AbstractUser

# Custom User model
class CustomUser(AbstractUser):
    is_client = models.BooleanField(default=False)
    is_vendor = models.BooleanField(default=False)

# Profile model
class Profile(models.Model):
    USER_TYPE_CHOICES = (
        ('client', 'Client'),
        ('vendor', 'Vendor'),
    )
    
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='client')
    
    # Client-specific fields
    partner1_name = models.CharField(max_length=100, blank=True, null=True)
    partner2_name = models.CharField(max_length=100, blank=True, null=True)
    birth_year1 = models.IntegerField(blank=True, null=True)
    birth_year2 = models.IntegerField(blank=True, null=True)

    # Vendor-specific fields
    vendor_name = models.CharField(max_length=100, blank=True, null=True)
    vendor_identifier = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.user.username