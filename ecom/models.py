from django.db import models
from django.utils import timezone

# Create your models here.
class Product(models.Model):
    PRODUCT_TYPE_CHOICES = [
        ('electronics', 'Electronics'), 
        ('clothing', 'Clothing'),
        ('home_appliances', 'Home Appliances'),
        ('books', 'Books'),
        ('toys', 'Toys'),
        ('sports', 'Sports'),
        ('beauty', 'Beauty'),
       
    ]
    name=models.CharField( max_length=50)
    image=models.ImageField(upload_to='products/')
    date_added=models.DateTimeField(default=timezone.now)
    type=models.CharField(max_length=20,choices=PRODUCT_TYPE_CHOICES)
    description=models.TextField(default='')

    def __str__(self):
        return self.name
