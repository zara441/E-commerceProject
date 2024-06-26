from django import template

register = template.Library()

@register.filter(name='chunks')
def chunks(alist,start,size=4):
    stop=start+size
    return alist[start:stop]
    # 0 , 4 ,[0:4]=----->0,1,2,3
    # 4 , 8 ,[4:8]=----->4,5,6,7