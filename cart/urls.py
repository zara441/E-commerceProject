from django.urls import path
from . views import *

urlpatterns=[
    path('cartDetails',cart,name='cart'),
    path('addtocart/<product_id>',add_to_cart,name="addtocart"),
    path('remove/<product_id>',item_deletion,name="remove"),
    path('quan_decrement/<product_id>',cart_decrement,name="decrement"),
    path('quan_increment/<product_id>',cart_increment,name="increment"),
    
    
]