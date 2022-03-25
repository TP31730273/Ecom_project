from urllib import response
from django import views
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect
from .models import *
from django.contrib.auth.hashers import make_password,check_password
from django.contrib import messages
from django.core.paginator import Paginator
# Create your views here.

class HomeView(View):
     def get(self,request):
          return render(request,'app/index.html')

class MyAccountView(View):
     def get(self,request):
          return render(request,'app/my-account.html')

class MySellerAccountView(View):
     def get(self,request):
          return render(request,'app/seller-account.html')

class ProductListPage(View):
     def get(self,request):
          products = Product.objects.all().order_by('id')
          # paginator = Paginator(product, 5)
          # page_number = request.GET.get('page')
          # page_object = paginator.get_page(page_number)
          return render(request,'app/product-list.html',{"products":products})
     def post(self,request):
          pass

class AddProductPage(View):
     def get(self,request):
          return render(request,'app/add-product.html')

class RegisterForm(View):
     def get(self,request):
          if 'email' in request.session:
              
               return redirect('HomeView')
          else:
               return render(request,'app/register.html')

class LoginForm(View):
     def get(self,request):
          if 'email' in request.session:

               return redirect('HomeView')
          else:
               return render(request,'app/login.html')

class SellerLoginForm(View):
     def get(self,request):
          if 'email' in request.session:

               return redirect('HomeView')
          else:
               return render(request,'app/seller_login.html')

class RegisterView(View):
     def post(self, request):
          user_name = request.POST.get('username')
          email = request.POST.get('email')
          password = request.POST.get('pswd')
          bool = request.POST.get('check1')
          
          print(bool,"***2345435345345******")
          if bool != 'on':
               get_user=Customers.objects.filter(email=email).exists()
               if not get_user:
                    if request.method == "POST":
                         user_create=Customers.objects.create(email=email,username=user_name,password=make_password(password))
                         user_create.save()
                         return redirect('LoginForm')
               else:
                    messages.warning(request, 'Your account expires in three days.')
                    return redirect('RegisterForm')
          else:
               get_seller=Sellers.objects.filter(email=email).exists()
               if not get_seller:
                    if request.method == "POST":
                         seller_create=Sellers.objects.create(email=email,username=user_name,password=make_password(password))
                         seller_create.save()
                         return redirect('SellerLoginForm')
               else:
                    return redirect('RegisterForm')

class LoginView(View):
   
     def post(self, request):

          if request.method == "POST":
               email = request.POST.get('email')
               password = request.POST.get('pswd') 
               get_user=Customers.objects.filter(email=email).exists()
              
               if get_user:
                  
                    user=Customers.objects.get(email=email)
                    if check_password(password,user.password):
                         request.session['email']=email
                         return redirect('HomeView')
                    else:
                         return redirect('LoginForm')
class SellerLoginView(View):
   
     def post(self, request):

          if request.method == "POST":
               email = request.POST.get('email')
               password = request.POST.get('pswd') 
               get_seller=Sellers.objects.filter(email=email).exists()
              
               if get_seller:
                  
                    seller=Sellers.objects.get(email=email)
                    if check_password(password,seller.password):
                         request.session['email']=email
                         return redirect('MySellerAccountView')
                    else:
                         return redirect('SellerLoginForm')

class AddProductView(View):
     def post(self, request):
          if request.method == "POST":
               product_name = request.POST.get('product_name')
               product_description = request.POST.get('product_description')
               product_price = request.POST.get('product_price')
               # product_category = request.POST.get('product_category')
               product_image = request.FILES['product_image']
               exist_product=Product.objects.filter(product_name=product_name).exists()
               live_seller=Sellers.objects.get(email=request.session['email'])


               if not exist_product:
                    create_product=Product.objects.create(product_name=product_name,product_description=product_description,product_price=product_price,product_image=product_image,seller=live_seller)
                    create_product.save()
                    return redirect('ProductListPage')
               else:
                    response={
                         'msg':"This product is already exist in your database please add another product"
                    }
                    return JsonResponse(response)


class Logout(View):
     def get(self, request):
          if 'email' in request.session:
               del request.session['email']
               print("********121234234234234243423423423424234234******")
               return redirect('HomeView')

       