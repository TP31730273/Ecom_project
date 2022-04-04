
from django.db import models
from django.contrib.auth.models import User,AbstractBaseUser


# Create your models here.
class Customers(AbstractBaseUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=40, blank=True, null=True)
    password=models.CharField(max_length=200)
    image = models.ImageField(default = "default.jpg", upload_to = "media")

    class Meta:
        db_table = 'Customer'

    def __str__(self):
        return self.email

class Sellers(AbstractBaseUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=40, blank=True, null=True)
    password=models.CharField(max_length=200)
    shop_name=models.CharField(max_length=100,blank=True, null=True)
    image = models.ImageField(default = "default.jpg", upload_to = "media")

    def __str__(self):
        return self.email

class Category(models.Model):
    category_name = models.CharField(unique=True,max_length=100)

    def __str__(self):
        return self.category_name

class Product(models.Model):
    product_name = models.CharField(unique=True,max_length=100)
    product_description = models.TextField(blank=True, null=True)
    product_price = models.FloatField()
    product_image = models.ImageField(upload_to="images/", blank=True, null=True)
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    seller = models.ForeignKey(Sellers, on_delete=models.CASCADE, blank=True, null=True)
    is_active=models.BooleanField(default=True)
    date_modified = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name




