from re import template
from django.urls import path
from app.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', HomeView.as_view(),name='HomeView'),
    path('login/', LoginForm.as_view(),name='LoginForm'),
    path('seller-login/', SellerLoginForm.as_view(),name='SellerLoginForm'),
    path('register/', RegisterForm.as_view(),name='RegisterForm'),
    path('registered/', RegisterView.as_view(),name='RegisterView'),
    path('Logined/', LoginView.as_view(),name='LoginView'),
    path('seller-Logined/', SellerLoginView.as_view(),name='SellerLoginView'),
    path('Logout/', Logout.as_view(),name='Logout'),
    path('Add-product/', AddProductPage.as_view(),name='AddProductPage'),
    path('Added-product/', AddProductView.as_view(),name='AddProductView'),
    path('MyAccount/', MyAccountView.as_view(),name='MyAccountView'),
    path('SellerAccount/', MySellerAccountView.as_view(),name='MySellerAccountView'),
    path('Product-list/', ProductListPage.as_view(),name='ProductListPage'),
    path('add-category/', TemplateView.as_view(template_name='app/add-category.html'),name='AddCategoryView '),
    path('Add-category/', AddCategoryView.as_view(),name='AddCategoryView'),
    path('Product-page/<int:product>/', ProductView.as_view(),name='product_page'),
    path('delete-product/<int:product>/', RemoveProductPage.as_view(),name='RemoveProductPage'),
    path('filtered-data/', FilterFunction.as_view(),name='FilterFunction'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)