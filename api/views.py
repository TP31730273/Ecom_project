# from unicodedata import category
# from django.shortcuts import render
# from django.http import HttpResponse,JsonResponse
# from rest_framework.parsers import JSONParser
# from rest_framework.response import Response 
# from rest_framework.renderers import JSONRenderer 
from rest_framework.generics import ListAPIView,GenericAPIView,ListCreateAPIView,RetrieveUpdateAPIView,DestroyAPIView,RetrieveUpdateDestroyAPIView
# from rest_framework.mixins import ListModelMixin,CreateModelMixin,UpdateModelMixin,DestroyModelMixin,RetrieveModelMixin
from  app.models import Product
from .serializers import *
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class MyPagination(PageNumberPagination):
    page_size=10
    page_query_param ='p'
    page_size_query_param='records'

# list and create new product
class ProductListView(ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset =Product.objects.all()
    serializer_class= ProductSerializer
    pagination_class=MyPagination
    MyPagination.page_size=3

# delete,retrive and update
class ProductVIewApi(RetrieveUpdateDestroyAPIView):
    queryset =Product.objects.all()
    serializer_class= ProductSerializer

# listing and creating category
class CategoryListView(ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset =Category.objects.all()
    serializer_class= CategorySerializer
    pagination_class=MyPagination
    MyPagination.page_size=5

# delete update and retriveing 
class CategoryViewApi(RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset =Product.objects.all()
    serializer_class= ProductSerializer

class ProductFilterApi(ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class= ProductSerializer
    pagination_class=MyPagination
    MyPagination.page_size=5
    def get_queryset(self):
        return Product.objects.filter(product_category__category_name__contains=self.request.GET.get('product_category'))
    
class ProductSearchApi(ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class= ProductSerializer
    pagination_class=MyPagination
    MyPagination.page_size=5
    def get_queryset(self):
        search=self.request.GET.get('search')
        return Product.objects.filter(Q(product_name__icontains=search)|Q(product_category__category_name__icontains=search))

class SellerListView(ListCreateAPIView):
    queryset =Sellers.objects.all()
    serializer_class= SellerSerializer
    pagination_class=MyPagination
    MyPagination.page_size=3

class CustomerListView(ListCreateAPIView):
    queryset =Customers.objects.all()
    serializer_class= CustomerSerializer
    pagination_class=MyPagination
    MyPagination.page_size=3

# generic api views with modelmixins
# class ProductListView(GenericAPIView,ListModelMixin,CreateModelMixin):
#     queryset =Product.objects.all()
#     serializer_class= ProductSerializer

#     def get(self,request,*args,**kwargs):
#         return self.list(request,*args,**kwargs)

#     def post(self,request,*args,**kwargs):
#         return self.create(request,*args,**kwargs)

# class ProductVIewApi(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
#     queryset =Product.objects.all()
#     serializer_class= ProductSerializer

#     # get perticular product
#     def get(self,request,*args,**kwargs):
#         return self.retrieve(request,*args,**kwargs)

#     # update complete details of product
#     def put(self,request,*args,**kwargs):
#         return self.update(request,*args,**kwargs)

#     # delete a perticular product
#     def delete(self,request,*args,**kwargs):
#         return self.destroy(request,*args,**kwargs)

# class ProductListView(GenericAPIView,CreateModelMixin):
#     queryset =Product.objects.all()
#     serializer_class= ProductSerializer

#     def post(self,request,*args,**kwargs):
#         return self.create(request,*args,**kwargs)




###### ListApiView with custom-method

# class ProductListView(ListAPIView):
#     def get(self,request):
#         product=Product.objects.all()
#         serializer=ProductSerializer(product,many=True)
#         return JsonResponse(serializer.data,safe=False)
        
#     @csrf_exempt
#     def post(self,request):
#         serializer=ProductSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data,safe=False)
#         else:
#             return JsonResponse(serializer.error_messages,safe=False)
#     @csrf_exempt
#     def patch(self, request, pk):
#         product = Product.objects.get(id=pk)
#         serializer = ProductSerializer(product, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         else:
#             return JsonResponse(serializer.errors)

#     def delete(self, request, pk):
#         product = Product.objects.get(id=pk)
#         product.delete()
#         return JsonResponse("Product-Deleted", safe=False)


# class CategoryListView(ListAPIView):
#     def get(self,request):
#         category=Category.objects.all()
#         serializer=CategorySerializer(category,many=True)
#         return JsonResponse(serializer.data,safe=False)
        
#     @csrf_exempt
#     def post(self,request):
#         serializer=CategorySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data,safe=False)
#         else:
#             return JsonResponse(serializer.error_messages,safe=False)
#     @csrf_exempt
#     def patch(self, request, pk):
#         category = Category.objects.get(id=pk)
#         serializer = CategorySerializer(category, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         else:
#             return JsonResponse(serializer.errors)

#     def delete(self, request, pk):
#         category = Category.objects.get(id=pk)
#         category.delete()
#         return JsonResponse("Category Deleted", safe=False)
