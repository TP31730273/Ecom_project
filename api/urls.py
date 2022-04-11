from unicodedata import name
from django.urls import path,include
from .views import *
urlpatterns = [
    path('product-list/',ProductListView.as_view(),name="product_list"),
    path('product-create/',ProductListView.as_view(),name="product_list"),
    path('product/<int:pk>',ProductVIewApi.as_view(),name="ProductVIewApi"),
    path('product-delete/<int:pk>',ProductVIewApi.as_view(),name="ProductVIewApi"),
    path('product-update/<int:pk>',ProductVIewApi.as_view(),name="ProductVIewApi"),
    path('category-list/',CategoryListView.as_view(),name="CategoryListView"),
    path('category-create/',CategoryListView.as_view(),name="CategoryListView"),
    path('category/<int:pk>',CategoryViewApi.as_view(),name="CategoryViewApi"),
    path('category-update/<int:pk>',CategoryViewApi.as_view(),name="CategoryViewApi"),
    path('category-delete/<int:pk>',CategoryViewApi.as_view(),name="CategoryViewApi"),
    path('product-filter/',ProductFilterApi.as_view(),name="ProductFilterApi"),
    path('product-search/',ProductSearchApi.as_view(),name="ProductSearchApi"),
]
