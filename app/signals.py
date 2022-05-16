
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from app.models import Customers, Sellers

# from django.contrib.auth.models import User

@receiver(post_save,sender=Customers)
def create_auth_token(sender, instance, created, **kwargs):
    print(instance,"84933849038948")
    if created:
        Token.objects.create(user=instance)

@receiver(post_save,sender=Sellers)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
