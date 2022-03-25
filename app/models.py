from email.policy import default
from tkinter import CASCADE
from unicodedata import name
from django.db import models
from django.contrib.auth.models import User,AbstractBaseUser,PermissionsMixin
from django.core.validators import MaxLengthValidator,MinLengthValidator

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
    Shop_name=models.CharField(max_length=100,blank=True, null=True)
    image = models.ImageField(default = "default.jpg", upload_to = "media")

    def __str__(self):
        return self.username

class Category(models.Model):
    category_name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.category_name

class Product(models.Model):
    product_name = models.CharField(max_length=100, blank=True, null=True)
    product_description = models.CharField(max_length=500, blank=True, null=True)
    product_price = models.PositiveIntegerField(blank=True, null=True)
    product_image = models.ImageField(upload_to="images/", blank=True, null=True)
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    seller = models.ForeignKey(Sellers, on_delete=models.CASCADE, blank=True, null=True)
    soft_product=models.BooleanField(default=False)

    def __str__(self):
        return self.product_name




