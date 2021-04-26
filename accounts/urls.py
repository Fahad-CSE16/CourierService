from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('',homeView.as_view(), name='home'),
    path('login/', handleLogin, name='login'),
    path('logout/', handleLogout, name='logout'),
]
