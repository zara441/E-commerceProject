from django.urls import path
from . views import *

urlpatterns=[
            path('',home,name='home'),
            path('shop/',shop,name='shop'),
            path('shop/<slug:c_slug>',shop,name='product_cate'),
            path('<slug:c_slug>/<slug:product_slug>',product,name='product'),
            
]