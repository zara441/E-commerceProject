from django.urls import path
from . views import *

urlpatterns=[
    path('login/',login_signup,name='login'),
    path('logout/',logout,name='logout'),
]