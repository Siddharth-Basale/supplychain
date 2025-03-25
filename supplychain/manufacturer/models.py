from django.db import models
from django.contrib.auth.models import AbstractUser

class Manufacturer(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    business_type = models.CharField(max_length=100)
    website = models.URLField(blank=True)
    phone_number = models.CharField(max_length=20)
    key_products = models.TextField()
    
    def __str__(self):
        return self.company_name