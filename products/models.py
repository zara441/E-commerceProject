from django.db import models
from django.template.defaultfilters import slugify
import datetime
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=200,unique=True)
    slug=models.SlugField(max_length=200,unique=True)

    def __str__(self):
        return '{}'.format(self.name)

    def get_url(self):
        return reverse('product_cate',args=[self.slug]) 

class Product(models.Model):
    LIVE=1
    DELETE=0
    DELETE_CHOICES=((LIVE,'Live'),(DELETE,'Delete'))
    SMALL="S"
    MEDIUM='M'
    LARGE="L"
    XL="XL"
    SIZE_CHOICES=((SMALL,'Small'),(MEDIUM,'Medium'),(LARGE,'Large'),(XL,'XL'))
    title=models.CharField(max_length=250)
    slug=models.SlugField(max_length=250)
    price=models.FloatField()
    desc=models.TextField()
    img=models.ImageField(upload_to='products_images')
    category=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,related_name="products")
    priority=models.IntegerField(default=0)
    delete_status=models.IntegerField(choices=DELETE_CHOICES,default=LIVE)
    size=models.CharField(choices=SIZE_CHOICES,max_length=3,default=MEDIUM)
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)
    stock=models.IntegerField()
    available=models.BooleanField()
    rating=models.FloatField()

    def __str__(self):
        return '{}'.format(self.title)
    
    def get_url(self):
        return reverse('product',args=[self.category.slug,self.slug])
    


