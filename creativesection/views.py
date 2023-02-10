from django.shortcuts import render
from home.models import Creative_Items
from django.views import View

# Create your views here.
def creativesection(request):
    creativesec  = Creative_Items.objects.filter()
    return render(request,'creative_pages/creativesection.html',{'creativesec':creativesec})

#def productDetail(request):
#    return render(request,'creative_pages/productdetail.html')
class productDetailView(View):
    def get(self,request,pk):
        product = Creative_Items.objects.get(pk=pk)
        return render(request,'creative_pages/productdetail.html',{'product':product})


def cart(request):
    return render(request,'creative_pages/cart.html')

