from django.shortcuts import render
from home.models import Scrap_Items
# Create your views here.
def scrapsection(request):
    scrapyardsec = Scrap_Items.objects.filter()
    return render(request,'scrap_pages/scrapsection.html',{'scrapyardsec':scrapyardsec})
