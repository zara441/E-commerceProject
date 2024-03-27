from django.shortcuts import render,get_object_or_404
from . models import *
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.
# 
def home(request):
    prod=Product.objects.all()[:4]
    context={'products':prod}
    return render(request,'index.html',context)

def shop(request,c_slug=None):
    c_page=None
    prodt=None
    query=None # part of search
    if c_slug != None:
        c_page=get_object_or_404(Category,slug=c_slug)
        prodt=Product.objects.filter(category=c_page,available=True)
    else:
        page=1
        if request.GET:
            page=int(request.GET.get('page',1))
        prod=Product.objects.all().filter(available=True) 
        # pagination code starts
        prodt_paginator=Paginator(prod,2)
        prodt=prodt_paginator.get_page(page)

        # pagination code ends

        # search try starts
        if "s" in request.GET or "q" in request.GET:

            query=request.GET.get("s")
            q=request.GET.get("q")
            prodt=Product.objects.all().filter(Q(title__icontains=query)|Q(desc__icontains=query))
        # search try ends    
          
    cate=Category.objects.all()

    return render(request,'products.html',{'products':prodt,'cat':cate})    



   

# def shop(request):
#     prod=list(Product.objects.all())
#     context={'products':prod}

#     return render(request,'products.html',context)  
  
 
def product(request,c_slug,product_slug):
    try:
   
        product=Product.objects.get(category__slug=c_slug,slug=product_slug)

    except Exception as e:
        raise e  

    return render(request,'prodetails.html',{'product':product})    

