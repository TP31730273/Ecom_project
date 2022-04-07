from rest_framework import serializers
from .models import *

class ProductSerializer(serializers.Serializer):
    product_name = serializers.CharField(unique=True,max_length=100)
    product_description = serializers.TextField(blank=True, null=True)
    product_price = serializers.FloatField()
    pass