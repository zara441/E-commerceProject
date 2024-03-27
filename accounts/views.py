from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Customer
from django.contrib.auth import authenticate,login,logout as authlogout

# Create your views here.
def login_signup(request):
    context={}
    if request.POST and 'signup' in request.POST:
        context['register']=False
        try:
            username=request.POST.get('username')
            fnm=request.POST.get('fname')
            lnm=request.POST.get('lname')
            addre=request.POST.get('address')
            phone=request.POST.get('phone')
            email=request.POST.get('Email')
            paswd1=request.POST.get('password1')
            paswd2=request.POST.get('password1')
            if paswd1==paswd2:
                user=User.objects.create_user(username=username,first_name=fnm,last_name=lnm,email=email,password=paswd1)
                user.save()
                customer=Customer.objects.create(user=user,username=username,address=addre,phone_number=phone)
                messages.success(request,'successfully signed up')
            else:
                messages.info(request,'Invalid credentials')
        except Exception as e:
            error='INVALID! Invalid credentials'
            messages.error(request,error)  
    if request.POST and 'login' in request.POST:
        context['register']=True
        try:
            email=request.POST.get('Email')
            pasd=request.POST.get('password')
            user=authenticate(email=email,password=pasd)
            if user:
                login(request,user)
                return redirect('/')
            else:
                error='INVALID! Invalid credentials'
                messages.error(request,error) 
        except Exception as e:
            error='Invalid credentials'
            messages.error(request,error)             


    return render(request,'login&signup.html') 

def logout(request):
    authlogout(request)
    return redirect('/')