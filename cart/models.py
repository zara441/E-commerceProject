from django.db import models
from products.models import Product

# Create your models here.
class Cart(models.Model):
    LIVE=1
    DELETE=0
    DELETE_CHOICES=((LIVE,'Live'),(DELETE,'Delete'))
    cart_id=models.CharField(max_length=250,unique=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    
    updated_at=models.DateTimeField(auto_now=True)
    delete_status=models.IntegerField(choices=DELETE_CHOICES,default=LIVE)

class OrderedItems(models.Model):
    product=models.ForeignKey(Product,on_delete=models.SET_NULL,null=True,related_name="added_cart")
    quantity=models.IntegerField(default=1)
    item_owner=models.ForeignKey(Cart,on_delete=models.SET_NULL,null=True,related_name="cart_items")
    active=models.BooleanField(default=True)

    def total(self):
        return self.product.price * self.quantity

