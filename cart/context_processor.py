from . models import *
from . views import *

def count(request):
    item_count=0
    if 'admin' in request.path:
        return {}
    else:
        try:
            ct=Cart.objects.filter(cart_id=cart_idd(request))
            ct_items=OrderedItems.objects.all().filter(item_owner=ct[:1])
            for c in ct_items:
                item_count += c.quantity
        except OrderedItems.DoesNotExist:
            item_count = 0
    return dict(itc=item_count)                