from django.contrib import admin

#manually imported
from .models import (
    Customer,
    Creative_Items,
    Scrap_Items,
    Cart,
    Order_placed
)

# Register your models here.
@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','name','locality','city','zipcode','state']

@admin.register(Creative_Items)
class Creative_ItemsModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','selling_price','discount_price','description','brand','category','product_image','last_modified']

@admin.register(Scrap_Items)
class Scrap_ItemsModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','selling_price','seller_email','discount_price','description','brand','category','product_images','last_modified']

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','creative','quantity']

@admin.register(Order_placed)
class Order_placedModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','creative','quantity','ordered_date','status']