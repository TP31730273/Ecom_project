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



