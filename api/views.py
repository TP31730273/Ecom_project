from unicodedata import category
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from numpy import product
from rest_framework.parsers import JSONParser
from rest_framework.response import Response 
from rest_framework.renderers import JSONRenderer 
from rest_framework.generics import ListAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView 
from  app.models import Product
from .serializers import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.decorators import api_view 
from rest_framework import permissions

class ProductListView(ListAPIView):
    def get(self,request):
        product=Product.objects.all()
        serializer=ProductSerializer(product,many=True)
        return JsonResponse(serializer.data,safe=False)
        
    @csrf_exempt
    def post(self,request):
        serializer=ProductSerializer(data=request.data)
        print("##############")
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,safe=False)
        else:
            return JsonResponse(serializer.error_messages,safe=False)
    @csrf_exempt
    def patch(self, request, pk):
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        else:
            return JsonResponse(serializer.errors)

    def delete(self, request, pk):
        product = Product.objects.get(id=pk)
        product.delete()
        return JsonResponse("Product-Deleted", safe=False)


class CategoryListView(ListAPIView):
    def get(self,request):
        category=Category.objects.all()
        serializer=CategorySerializer(category,many=True)
        return JsonResponse(serializer.data,safe=False)
        
    @csrf_exempt
    def post(self,request):
        serializer=CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,safe=False)
        else:
            return JsonResponse(serializer.error_messages,safe=False)
    @csrf_exempt
    def patch(self, request, pk):
        category = Category.objects.get(id=pk)
        serializer = CategorySerializer(category, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        else:
            return JsonResponse(serializer.errors)

    def delete(self, request, pk):
        category = Category.objects.get(id=pk)
        category.delete()
        return JsonResponse("Category Deleted", safe=False)
# Create your views here.

# def product_list(request):

#     if request.method == 'GET':
#         product=Product.objects.all()
#         serializer=ProductSerializer(product,many=True)
#         return JsonResponse(serializer.data,safe=False)
#     elif request.method == 'POST':
#         print(request.POST.get('product_name'),"****************************")
       
#         serializer=ProductSerializer(data=request.data)
#         print("##############")
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data,safe=False)
#         else:
#             return JsonResponse(serializer.error_messages,safe=False)

