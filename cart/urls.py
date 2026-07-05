from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
   
    path("",cart_page),
    path("add/<slug:slug>",add_to_cart,name="add_to_cart"),
    path("increase/<slug:slug>",increase_quantity,name="increase_quantity"),
    path("decrease/<slug:slug>",decrease_quantity,name="decrease_quantity"),
]