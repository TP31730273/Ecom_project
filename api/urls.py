from unicodedata import name
from django.urls import path,include
from .views import *

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)
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
    path('seller-create/',SellerListView.as_view(),name="SellerListView"),
    path('seller-list/',SellerListView.as_view(),name="SellerListView"),
    path('customer-create/',CustomerListView.as_view(),name="CustomerListView"),
    path('customer-list/',CustomerListView.as_view(),name="CustomerListView"),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
