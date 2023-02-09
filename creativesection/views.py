from django.shortcuts import render
from home.models import Creative_Items

# Create your views here.
def creativesection(request):
    creativesec  = Creative_Items.objects.filter()
    return render(request,'creative_pages/creativesection.html',{'creativesec':creativesec})