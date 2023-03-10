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
from scrapsection import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.scrapsection, name="scrapsection"),
    path('plasticitems', views.plasticitems, name="plasticitems"),
    path('glassitems', views.glassitems, name="glassitems"),
    path('electricitems', views.electricitems, name="electricitems"),
    path('woodenitems', views.woodenitems, name="woodenitems"),
    path('metalitems', views.metalitems, name="metalitems"),
    path('scrapProductDetail/<int:pk>', views.scrapproductDetailView.as_view(), name="scrapProductDetail"),
    path('contactseller/<int:pk>',views.contactseller, name="contactseller"),
]