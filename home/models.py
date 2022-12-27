#database tables are created using models


from distutils.command.upload import upload
from tkinter import CASCADE
from unicodedata import category, name
from django.db import models

#manually imported
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinLengthValidator

# Create your models here.
STATE_CHOICES =(
    ('Andhra Pradesh','Andhra Pradesh'),
    ('Arunachal Pradesh','Arunachal Pradesh'),
    ('Assam','Assam'),
    ('Bihar','Bihar'),
    ('Chhattisgarh','Chhattisgarh'),
    ('Goa','Goa'),
    ('Gujarat','Gujarat'),
    ('Haryana','Haryana'),
    ('Himachal Pradesh','Himachal Pradesh'),
    ('Jammu and Kashmir','Jammu and Kashmir'),
    ('Jharkhand','Jharkhand'),
    ('Karnataka','Karnataka'),
    ('Kerala','Kerala'),
    ('Madhya Pradesh','Madhya Pradesh'),
    ('Maharashtra','Maharastra'),
    ('Manipur','Manipur'),
    ('Meghalaya','Meghalaya'),
    ('Mizoram','Mizoram'),
    ('Nagaland','Nagaland'),
    ('Odisha', 'Odisha'),
    ('Punjab','punjab'),
    ('Rajasthan','Rajasthan'),
    ('Sikkim','Sikkim'),
    ('Tamil Nadu','Tamil Nadu'),
    ('Telangana', 'Telangana'),
    ('Tripura', 'Tripura'),
    ('Uttarakhand','Uttarakhand'),
    ('Uttar Pradesh','Uttar Pradesh'),
    ('West Bengal','West Bengal'),
    ('Andaman and Nicobar Islands','Andaman and Nicobar Islands'),
    ('Chandigarh','Chandigarh'),
    ('Dadra and Nagar Haveli','Dadra and Nagar Haveli'),
    ('Daman and Diu','Daman and Diu'),
    ('Delhi','Delhi'),
    ('Lakshadweep','Lakshadweep'),
    ('Puducherry','Puducherry'),
)

#many to one relationship (this is mutiple address of user for shipping)
class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES,max_length=50)

    def __str__(self):
        return str(self.id)

#CREATIVE MODEL
CREATIVE_CHOICES =(
    ('PT','POTRAIT'),
    ('PA','PAPER ART'),
    ('MA','METAL ART'),
    ('GA','GLASS ART'),
    ('PL','PLASTIC ART'),
)
class Creative_Items(models.Model):
    title          = models.CharField(max_length=100)
    selling_price  = models.FloatField()
    discount_price = models.FloatField()
    description    = models.TextField()
    brand          = models.CharField(max_length=100)
    category       = models.CharField(choices=CREATIVE_CHOICES,max_length=2)
    product_image  = models.ImageField(upload_to ='creative_img')
    last_modified  = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.id)

#SCRAPYARD MODEL
SCRAP_CHOICES =(
    ('MI','METAL ITEMS'),
    ('WI','WOODEN ITEMS'),
    ('EI','ELECTRICAL ITEMS'),
    ('GI','GLASS ITEMS'),
    ('PI','PLASTIC ITEMS'),
)
class Scrap_Items(models.Model):
    title          = models.CharField(max_length=100)
    selling_price  = models.FloatField()
    discount_price = models.FloatField()
    description    = models.TextField()
    brand          = models.CharField(max_length=100)
    category       = models.CharField(choices=SCRAP_CHOICES,max_length=2)
    product_images = models.ImageField(upload_to ='scrap_img')
    last_modified  = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.id)

#CART MODEL
class Cart(models.Model):
    user     = models.ForeignKey(User,on_delete=models.CASCADE)
    scrap    = models.ForeignKey(Scrap_Items,on_delete=models.CASCADE)
    creative = models.ForeignKey(Creative_Items,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

#STATUS MODEL
STATUS_CHOICES = (
    ('ACCEPTED','ACCEPTED'),
    ('PACKED','PACKED'),
    ('ON THE WAY','ON THE WAY'),
    ('DELIVERED','DELIVERED'),
    ('CANCEL','CANCEL'),
)

class Order_placed(models.Model):
    user         = models.ForeignKey(User,on_delete = models.CASCADE)
    customer     = models.ForeignKey(Customer,on_delete = models.CASCADE)
    creative     = models.ForeignKey(Creative_Items, on_delete = models.CASCADE)
    scrap        = models.ForeignKey(Scrap_Items,on_delete = models.CASCADE)
    quantity     = models.PositiveIntegerField(default = 1)
    ordered_date = models.DateTimeField(auto_now_add = True)
    status       = models.CharField(max_length=50,choices=STATUS_CHOICES,default='Pending')
