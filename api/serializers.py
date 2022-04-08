from dataclasses import field
from rest_framework import serializers
from  app.models import *

class ProductSerializer(serializers.ModelSerializer):
   class Meta:
       model=Product
       fields=['product_name','product_description','product_price','product_image','product_category','is_active','seller']

class CategorySerializer(serializers.ModelSerializer):
   class Meta:
       model=Category
       fields=['category_name']

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


