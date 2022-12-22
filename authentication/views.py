from django.http import HttpResponse


#manually imported
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import login as login_user
from django.contrib.auth import authenticate

"""
#These are imported for sending mail 

from scrapyard import settings
from django.core.mail import send_mail
import smtplib
"""



# Create your views here.
"""
def home(request):
    return HttpResponse("Hello home page")
"""
def login(request):

    if request.method == "POST":
        username    = request.POST['username']
        password    = request.POST['password']

        user = authenticate(username=username,password=password)

        if user is not None:
            login_user(request,user)
            messages.success(request,"You have been successfully logged in ")
            return redirect('/home/home')
        else:
            messages.error(request,"Bad Credentials")
            return render(request,'authentication/login.html')

    return render(request,"authentication/login.html")

def index_sign(request):

    if request.method == "POST":
        lname    = request.POST.get('lname')
        fname    = request.POST.get('fname')
        username = request.POST.get('username')
        email    = request.POST.get('email')
        password = request.POST.get('password')
        password1 = request.POST.get('password1')

       #checking if username exist 
        if User.objects.filter(username=username):
            messages.error(request,"Username already exist! Please try some other username.")
            return redirect('/index_sign')
        #checking length of user
        if len(username)>10:
            messages.error(request,"Username must be less than 10 characters.")
            return redirect('/index_sign')

        #checking username is alphanumeric or not.
        if not username.isalnum():
            messages.error(request,"Username must be Alpha-Numeric!!!")
            return redirect('/index_sign')

        #checking if email exist
        if User.objects.filter(email=email).exists():
            messages.error(request,"This email is already taken! Please use other email.")
            return redirect('/index_sign')
        #checking confirm password
        if password != password1:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('/index_sign')

         #checking password is alphanumeric or not.
        if not password.isalnum():
            messages.error(request,"password must be Alpha-Numeric!!!")
            return redirect('/index_sign')
        

        myuser = User.objects.create_user(username,email,password)
        myuser.first_name = fname
        myuser.last_name  = lname

        #saving the data from post method
        myuser.save()

        messages.success(request,"Your Account has been successfully created.")

        """
        this email function is not working because google has stopped less secure apps option in gmail.so we cannot send mail through gmail 
        # welcome Email after creating account
        my_email = settings.EMAIL_HOST_USER
        rec_emil = [email]
        password = settings.EMAIL_HOST_PASSWORD
        message = " Hello" + myuser.first_name + " !! \n" + "Thank you for visting our website \n we have also sent you a a conformation email, please confirm your email address in order to activate your account.  \n \n  Thanking You \n Creative ScrapYard Team."

        with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=rec_emil,
                msg=message.encode("utf-8")
                )
        """

        return redirect('/login')
    return render(request,"authentication/signup.html")

