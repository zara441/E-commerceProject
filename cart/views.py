from django.shortcuts import render,redirect,get_object_or_404
from products.models import Product
from . models import Cart,OrderedItems
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def cart(request,total=0,count=0,cart_items=None):
    try:
        ct=Cart.objects.get(cart_id=cart_idd(request))
        ct_items=OrderedItems.objects.filter(item_owner=ct,active=True)
        for i in ct_items:
            total+=(i.product.price * i.quantity)
            count += 1
    except ObjectDoesNotExist:
        pass
    return render(request,'cart.html',{'ordered_products':ct_items,'total':total,'count':count})   

def cart_idd(request):
    ct_id=request.session.session_key
    if not ct_id:
        ct_id=request.session.create()
    return ct_id    
    

def add_to_cart(request,product_id):
    product=Product.objects.get(id=product_id)
    if request.POST or "btn" in request.POST:
        qty=int(request.POST.get('qty'))
        size=request.POST.get('size')
    
    try:
        cart=Cart.objects.get(cart_id=cart_idd(request))
    except Cart.DoesNotExist:
        cart=Cart.objects.create(cart_id=cart_idd(request))
        cart.save()
    try:
        cart_items=OrderedItems.objects.get(product=product,item_owner=cart) 
        if cart_items.quantity < cart_items.product.stock:
            cart_items.quantity += qty
            cart_items.save()
    except OrderedItems.DoesNotExist:
        cart_items=OrderedItems.objects.create(product=product,quantity=qty,item_owner=cart) 
        cart_items.save()
    return redirect('cart')     

def item_deletion(request,product_id):
    item_to_be_deleted=OrderedItems.objects.get(id=product_id) 
    if item_to_be_deleted:
        item_to_be_deleted.delete()
    return redirect('cart')

def cart_decrement(request,product_id):
    ct=Cart.objects.get(cart_id=cart_idd(request))
    prod=Product.objects.get(id=product_id)
    items=OrderedItems.objects.get(product=prod,item_owner=ct)
    if items.quantity >1:
        items.quantity -= 1
        items.save()
    else:
        items.delete()
    return redirect('cart')        
def cart_increment(request,product_id):
    ct=Cart.objects.get(cart_id=cart_idd(request))
    prod=Product.objects.get(id=product_id)
    items=OrderedItems.objects.get(product=prod,item_owner=ct)
    if items.quantity >= 1 and items.quantity < items.product.stock:
        items.quantity += 1
        items.save()
    return redirect('cart')     

