from django.urls import path
from app.views import *

urlpatterns = [
    path('', HomeView.as_view(),name='HomeView'),
    path('login/', LoginForm.as_view(),name='LoginForm'),
    path('register/', RegisterForm.as_view(),name='RegisterForm'),
    path('registered/', RegisterView.as_view(),name='RegisterView'),
    path('Logined/', LoginView.as_view(),name='LoginView'),
    path('Logout/', Logout.as_view(),name='Logout'),
    path('MyAccount/', MyAccountView.as_view(),name='MyAccountView'),
]