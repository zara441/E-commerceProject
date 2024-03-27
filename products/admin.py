from django.contrib import admin
from . models import Category,Product

# Register your models here.
#for viewing the same things we provided inside name in slug field ---do this-----:creating a class

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}
    list_display=['name','slug']



admin.site.register(Category,CategoryAdmin)

class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('title',)}
    list_display=['title','slug','price','img']
    list_editable=['price','img']

admin.site.register(Product,ProductsAdmin)    