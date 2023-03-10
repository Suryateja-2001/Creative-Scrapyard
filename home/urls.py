"""scrapyard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import views
from django.contrib import admin
# manually imported
from django.urls import path
from home import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('',login_required(views.home.as_view()),name="home"),
    path('logout', views.logout, name="logout"),
    path('contact', views.contact, name="contact"),
    path('about', views.about, name="about"),
    path('profile',login_required(views.profile.as_view()),name='profile'),
    path('address',views.address,name="address"),
    path('order',views.order,name="order"),
]
