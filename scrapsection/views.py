from django.shortcuts import render
from home.models import Scrap_Items
from django.views import View

# Create your views here.
def scrapsection(request):
    scrapyardsec = Scrap_Items.objects.filter()
    return render(request,'scrap_pages/scrapsection.html',{'scrapyardsec':scrapyardsec})

def metalitems(request):
    if Scrap_Items.objects.filter(category = 'MI') == None:
        scrapyardsec = Scrap_Items.objects.filter()
    else:
        scrapyardsec = Scrap_Items.objects.filter(category = 'MI')
    return render(request,'scrap_pages/scrapsection.html',{'scrapyardsec':scrapyardsec})

def woodenitems(request):
    if Scrap_Items.objects.filter(category = 'WI') == None:
        scrapyardsec = Scrap_Items.objects.filter()
    else:
        scrapyardsec = Scrap_Items.objects.filter(category = 'WI')
    return render(request,'scrap_pages/scrapsection.html',{'scrapyardsec':scrapyardsec})

def electricitems(request):
    if Scrap_Items.objects.filter(category = 'EI') == None:
        scrapyardsec = Scrap_Items.objects.filter()
    else:
        scrapyardsec = Scrap_Items.objects.filter(category = 'EI')
    return render(request,'scrap_pages/scrapsection.html',{'scrapyardsec':scrapyardsec})

def glassitems(request):
    if Scrap_Items.objects.filter(category = 'GI') == None:
        scrapyardsec = Scrap_Items.objects.filter()
    else:
        scrapyardsec = Scrap_Items.objects.filter(category = 'GI')
    return render(request,'scrap_pages/scrapsection.html',{'scrapyardsec':scrapyardsec})

def plasticitems(request):
    if Scrap_Items.objects.filter(category = 'PI') == None:
        scrapyardsec = Scrap_Items.objects.filter()
    else:
        scrapyardsec = Scrap_Items.objects.filter(category = 'PI')
    return render(request,'scrap_pages/scrapsection.html',{'scrapyardsec':scrapyardsec})

#def scrapProductDetail(request):
#    return render(request,'scrap_pages/product_detail.html')

class scrapproductDetailView(View):
    def get(self,request,pk):
        product = Scrap_Items.objects.get(pk=pk)
        return render(request,'scrap_pages/product_detail.html',{'product':product})