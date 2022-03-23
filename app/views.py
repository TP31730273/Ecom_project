from django import views
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect
from .models import *
from django.contrib.auth.hashers import make_password,check_password
from django.contrib import messages
# Create your views here.
class HomeView(View):
     def get(self,request):
          return render(request,'app/index.html')
class MyAccountView(View):
     def get(self,request):
          return render(request,'app/my-account.html')
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

class RegisterView(View):
     def post(self, request):
          user_name = request.POST.get('username')
          email = request.POST.get('email')
          password = request.POST.get('pswd')
          boo = request.POST.get('check1')
          
          print(type(boo),"*********")
          get_user=Customers.objects.filter(email=email).exists()
          if not get_user and (boo != 'on'):
               if request.method == "POST":
                    user_create=Customers.objects.create(email=email,username=user_name,password=make_password(password))
                    user_create.save()
                    return redirect('LoginForm')
          else:
               messages.warning(request, 'Your account expires in three days.')
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


class Logout(View):
     def get(self, request):
          if 'email' in request.session:
               del request.session['email']
               print("********121234234234234243423423423424234234******")
               return redirect('HomeView')

       