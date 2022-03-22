from django.urls import path
from app.views import *

urlpatterns = [
    path('', HomeView.as_view(),name='HomeView'),
]