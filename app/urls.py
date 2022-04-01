from re import template
from django.urls import path
from app.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', HomeView.as_view(),name='HomeView'),
    path('register/', RegisterView.as_view(),name='RegisterView'),
    path('user-login/', UserLoginView.as_view(),name='LoginView'),
    path('seller-login/', SellerLoginView.as_view(),name='SellerLoginView'),
    path('logout/', Logout.as_view(),name='Logout'),
    path('add-product/', AddProductView.as_view(),name='AddProductView'),
    path('user-account/', MyAccountView.as_view(),name='MyAccountView'),
    path('seller-account/', MySellerAccountView.as_view(),name='MySellerAccountView'),
    path('product-list/', ProductListPage.as_view(),name='ProductListPage'),
    # path('', AllProductList.as_view(),name='AllProductList'),
    path('inactive-product-list/', InactiveProductList.as_view(),name='InactiveProductList'),
    path('add-category/', AddCategoryView.as_view(),name='AddCategoryView'),
    path('delete-category/<int:pk>',DeleteCategoryView.as_view(),name='DeleteCategoryView'),
    path('product-page/<int:product>/', ProductView.as_view(),name='product_page'),
    path('inactive-product/<int:product>/', RemoveProductPage.as_view(),name='RemoveProductPage'),
    path('delete-product/<int:pk>/', DeleteProductPage.as_view(),name='DeleteProductPage'),
    path('edit-product/<int:product>/', EditProductView.as_view(),name='EditProductView'),
    path('filtered-products/', FilterFunction.as_view(),name='FilterFunction'),
    path('searched-products/', SearchProduct.as_view(),name='SearchProduct'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)