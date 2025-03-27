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
    



class QuoteRequest(models.Model):
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('closed', 'Closed'),
        ('awarded', 'Awarded'),
        ('expired', 'Expired'),
    ]
    
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    product = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    description = models.TextField()
    deadline = models.DateField()
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=20, blank=True)
    annual_volume = models.CharField(max_length=100, blank=True)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    currency = models.CharField(max_length=3, blank=True)
    shipping_terms = models.CharField(max_length=50)
    destination_port = models.CharField(max_length=100, blank=True)
    payment_terms = models.CharField(max_length=50)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='open')
    created_at = models.DateTimeField(auto_now_add=True)
    accepted_bid = models.ForeignKey('supplier.Bid', on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return f"{self.product} - {self.manufacturer.company_name}"
    
    def get_category_display(self):
        # Add this to display human-readable category names
        return self.category.replace('_', ' ').title()
    
    
# Add to manufacturer/models.py
class Feedback(models.Model):
    RATING_CHOICES = [
        (1, '1 - Poor'),
        (2, '2 - Fair'),
        (3, '3 - Good'),
        (4, '4 - Very Good'),
        (5, '5 - Excellent'),
    ]
    
    bid = models.OneToOneField('supplier.Bid', on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES)
    comments = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Feedback for {self.bid.supplier.company_name} by {self.bid.quote.manufacturer.company_name}"