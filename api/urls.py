from unicodedata import name
from django.urls import path,include
from .views import *
urlpatterns = [
    path('product_list/',ProductListView.as_view(),name="product_list"),
    path('product/<int:pk>',ProductVIewApi.as_view(),name="ProductVIewApi"),
    path('category_list/',CategoryListView.as_view(),name="CategoryListView"),
    path('category/<int:pk>',CategoryViewApi.as_view(),name="CategoryViewApi"),
    path('product-filter/',ProductFilterApi.as_view(),name="ProductFilterApi"),
    path('product-search/',ProductSearchApi.as_view(),name="ProductSearchApi"),
]
