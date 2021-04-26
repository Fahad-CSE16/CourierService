from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('',createOrder, name='orders'),
    # path('district/',district, name='district'),
    path('upoz/',upozilas, name='upoz'),
    path('list/',OrderList.as_view(), name='list'),
    
]
