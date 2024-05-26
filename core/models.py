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


'''class Category(models.Model):
    name = models.CharField(max_length=255)
    
    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name

class Item(models.Model):
    category = models.ForeignKey(Category, related_name='core_items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='items_images', blank=True, null=True)
    offered_by = models.ForeignKey(CustomUser, related_name='core_items', on_delete=models.CASCADE)
    is_available = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name'''
