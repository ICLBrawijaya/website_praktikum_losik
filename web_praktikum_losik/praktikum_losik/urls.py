from django.urls import path
from . import views

urlpatterns = [
    path('loginpage',views.loginpage,name='loginpage'),
    path('performlogin',views.performlogin,name='performlogin'),
    path('performlogout',views.performlogout, name='performlogout'),
    path('',views.index,name='index')
]
