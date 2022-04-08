from unicodedata import name
from django.urls import path,include
from .views import *
urlpatterns = [
    path('product_list/',ProductListView.as_view(),name="product_list"),
    path('product_list/<int:pk>',ProductListView.as_view(),name="product_list"),
    path('category_list/',CategoryListView.as_view(),name="CategoryListView"),
    path('category_list/<int:pk>',CategoryListView.as_view(),name="CategoryListView"),
]
