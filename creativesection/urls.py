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
# manually imported
from django.urls import path
from creativesection import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.creativesection, name="creativesection"),
    path('potraits', views.potraits, name="potraits"),
    path('paperart', views.paperart, name="paperart"),
    path('metalart', views.metalart, name="metalart"),
    path('glassart', views.glassart, name="glassart"),
    path('plasticart', views.plasticart, name="plasticart"),
    path('productDetail/<int:pk>', views.productDetailView.as_view(), name="productDetail"),
    path('cart',views.cart,name="cart"),
    path('showcart',views.showcart,name="showcart"),
    path('pluscart',views.plus_cart,name='plus_cart'),
    path('minuscart',views.minus_cart,name='minus_cart'),
    path('removecart',views.remove_cart,name='remove_cart'),
    path('checkout',views.checkout,name='checkout'),
    path('sucessfullyordered',views.sucessfullyordered,name='sucessfullyordered'),
]