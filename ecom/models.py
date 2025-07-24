from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

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
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    stock=models.PositiveIntegerField(default=0)



    def __str__(self):
        return self.name

#One to many Relationship
class ProductReview(models.Model):
    REVIEWS=[
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),

    
    ]    
    product =models.ForeignKey(Product, on_delete=models.CASCADE,related_name='reviews')
    User=models.ForeignKey(User,on_delete=models.CASCADE)
    comment=models.TextField(default='')
    date=models.DateTimeField(default=timezone.now)


    def __str__(self):
        return f'{self.User.username} review for {self.product.name}'  


#Many to many relationship
class Store(models.Model):
    name=models.CharField( max_length=50)
    location=models.CharField( max_length=50)
    store=models.ManyToManyField(Product,related_name='stores')

    def __str__(self):
        return self.name
    

#One to one
class ProductCertificate(models.Model):
    product=models.OneToOneField(Product,on_delete=models.CASCADE,related_name='certificate')


    def __str__(self):
        return f'Certificate for {self.name.product}'
