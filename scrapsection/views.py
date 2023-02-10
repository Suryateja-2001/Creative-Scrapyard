from django.shortcuts import render
from home.models import Scrap_Items
from django.views import View

# Create your views here.
def scrapsection(request):
    scrapyardsec = Scrap_Items.objects.filter()
    return render(request,'scrap_pages/scrapsection.html',{'scrapyardsec':scrapyardsec})

#def scrapProductDetail(request):
#    return render(request,'scrap_pages/product_detail.html')

class scrapproductDetailView(View):
    def get(self,request,pk):
        product = Scrap_Items.objects.get(pk=pk)
        return render(request,'scrap_pages/product_detail.html',{'product':product})