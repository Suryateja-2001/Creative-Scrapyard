from django.shortcuts import render,redirect
from home.models import Creative_Items,Cart,Customer,Order_placed
from django.views import View
from django.db.models import Q
from django.http import JsonResponse

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
    user = request.user
    product_id = request.GET.get('prod_id')
    product = Creative_Items.objects.get(id=product_id)
    Cart(user=user,creative=product).save()
    return redirect('/creativesection/showcart')

def showcart(request):
    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0.0
        shipping_amount = 70.0
        total_amount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user == user]
        if cart_product:
            for p in cart_product:
                temp = (p.quantity * p.creative.discount_price)
                amount += temp
            total_amount = amount+70
        return render(request,'creative_pages/cart.html',{'carts':cart,'total_amount':total_amount,'amount':amount})


def plus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(creative = prod_id) & Q(user = request.user))
        c.quantity+=1
        c.save()
        amount = 0.0
        shipping_amount = 70.0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
            temp = (p.quantity * p.creative.discount_price)
            amount += temp
        total_amount = amount+shipping_amount

        data = {
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':total_amount
        }
        return JsonResponse(data)

def minus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(creative = prod_id) & Q(user = request.user))
        c.quantity-=1
        c.save()
        amount = 0.0
        shipping_amount = 70.0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
            temp = (p.quantity * p.creative.discount_price)
            amount += temp
        total_amount = amount+shipping_amount

        data = {
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':total_amount
        }
        return JsonResponse(data)
    
def remove_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(creative = prod_id) & Q(user = request.user))
        c.delete()
        amount = 0.0
        shipping_amount = 70.0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
            temp = (p.quantity * p.creative.discount_price)
            amount += temp
        total_amount = amount+shipping_amount

        data = {
            'amount':amount,
            'totalamount':total_amount
        }
        return JsonResponse(data)
    
def checkout(request):
    user = request.user
    add = Customer.objects.filter(user = user)
    cart_items = Cart.objects.filter(user=user)
    amount = 0.0
    shipping_amount = 70.0
    cart_product = [p for p in Cart.objects.all() if p.user == request.user]
    if cart_product:
        for p in cart_product:
            temp = (p.quantity * p.creative.discount_price)
            amount += temp
        total_amount = amount+shipping_amount


    return render(request,'creative_pages/checkout.html',{'add':add,'totalamount':total_amount,'cartitems':cart_items})

def sucessfullyordered(request):
    user = request.user
    custid = request.GET.get('custid')
    customer = Customer.objects.get(id=custid)
    cart = Cart.objects.filter(user = user)
    for c in cart:
        Order_placed(user=user,customer=customer,creative=c.creative,quantity=c.quantity).save()
        c.delete()
    return redirect("order")

def potraits(request):
    if Creative_Items.objects.filter(category = 'PT') == None:
        potraits = Creative_Items.objects.filter()
    else:
        potraits = Creative_Items.objects.filter(category = 'PT')
    return render(request,'creative_pages/creativesection.html',{'creativesec':potraits})

def paperart(request):
    if Creative_Items.objects.filter(category = 'PA') == None:
        paperart = Creative_Items.objects.filter()
    else:
        paperart = Creative_Items.objects.filter(category = 'PA')
    return render(request,'creative_pages/creativesection.html',{'creativesec':paperart})

def metalart(request,data = None):
    if Creative_Items.objects.filter(category = 'MA') == None:
        metalart = Creative_Items.objects.filter()
    else:
        metalart = Creative_Items.objects.filter(category = 'MA')
    return render(request,'creative_pages/creativesection.html',{'creativesec':metalart})

def glassart(request,data = None):
    if Creative_Items.objects.filter(category = 'GA') == None:
        glassart = Creative_Items.objects.filter()
    else:
        glassart = Creative_Items.objects.filter(category = 'GA')
    return render(request,'creative_pages/creativesection.html',{'creativesec':glassart})

def plasticart(request,data = None):
    if Creative_Items.objects.filter(category = 'PL') == None:
        plasticart = Creative_Items.objects.filter()
    else:
        plasticart = Creative_Items.objects.filter(category = 'PL')
    return render(request,'creative_pages/creativesection.html',{'creativesec':plasticart})
