from django.contrib import admin
from . models import OrderedItems

# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = ['product','quantity']
admin.site.register(OrderedItems,OrderAdmin)

