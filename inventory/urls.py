from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path("brands/",list_all_brands,name="brands_list"),
]