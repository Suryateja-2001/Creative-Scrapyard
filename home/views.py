from http.client import HTTPResponse

#manually imported
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import logout as logout_user
from django.contrib.auth.decorators import login_required
from django.views import View
from .models import Customer,Creative_Items,Scrap_Items,Cart,Order_placed
# Create your views here.

#@login_required
#def home(request):
#    return render(request,"home/home.html")
class home(View):
    def get(self,request):
        creativesec  = Creative_Items.objects.filter()
        scrapyardsec = Scrap_Items.objects.filter()
        return render(request,"home/home.html",{'creativesec':creativesec,'scrapyardsec':scrapyardsec})

def logout(request):
    logout_user(request)
    messages.success(request,"Logged out Successfully!")
    return redirect('/login')

@login_required
def contact(request):
    if request.method == "POST":
        fullname = request.POST.get('fullname')
        email    = request.POST.get('email')
        description = request.POST.get('description')

        myuser = User.objects(email)
        myuser.fullname = fullname
        myuser.description = description

        #saving the data from post method
        myuser.save()
        messages.success(request,"We have recived your request.we'll contact you soon")
        return redirect('/home')

    return render(request,"home/contact.html")
    
@login_required
def about(request):
    return render(request,"home/about.html")