from dataclasses import field
from optparse import Values
from rest_framework import serializers
from  app.models import *
import re

# product serializer
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
       model=Product
       fields=['product_name','product_description','product_price','product_image','product_category','is_active','seller']
    def validate_product_price(self,value):
        if value <= 0:
            raise serializers.ValidationError('product price should be greater then zero')
        return value
        
    def validate_product_name(self,value):
        if value == '' or value.isspace():
            raise serializers.ValidationError('product NAME should not be blank or should not contain spaces')
        return value

# category serializer
class CategorySerializer(serializers.ModelSerializer):
   class Meta:
       model=Category
       fields=['category_name']

   def validate_category_name(self,value):
        if len(value) <= 0 or value == '':
            raise serializers.ValidationError('Category NAME should not be blank or should not contain spaces')
        return value

class SellerSerializer(serializers.ModelSerializer):
   class Meta:
       model=Sellers
       fields='__all__'

   def validate_seller(self,value):
        if value == 'False':
            raise serializers.ValidationError('Please choose seller is true')
        return value

class CustomerSerializer(serializers.ModelSerializer):
   class Meta:
       model=Sellers
       fields=['email','username','password']

# class ProductSerializer(serializers.Serializer):
#     product_name = serializers.CharField(max_length=100)
#     product_description = serializers.CharField(max_length=100)
#     product_price = serializers.FloatField()

#     def create(self, validated_data):
#         return Product.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Snippet` instance, given the validated data.
#         """
#         instance.product_name = validated_data.get('product_name', instance.product_name)
#         instance.product_description = validated_data.get('product_description', instance.product_description)
#         instance.product_price = validated_data.get('product_price', instance.product_price)
#         instance.save()
#         return instance


