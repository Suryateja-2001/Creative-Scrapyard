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
from .forms import CustomerProfileForm
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

class profile(View):
    def get(self,request):
        form = CustomerProfileForm()
        return render(request,"home/profile.html",{'form':form})
    
    def post(self,request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']

            save = Customer(user = user,name = name,locality = locality,city =city,state = state,zipcode = zipcode)
            save.save()
            messages.success(request,'Successfully added new Address')
        return render(request,"home/profile.html",{'form':form})

@login_required
def address(request):
    add = Customer.objects.filter(user=request.user)
    return render(request,"home/address.html",{'add':add})

@login_required
def order(request):
    op = Order_placed.objects.filter(user=request.user)
    return render(request,"home/orders.html",{'order_placed':op})