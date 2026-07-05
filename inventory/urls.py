from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path("brands/",list_all_brands,name="brands_list"),
    path("brand/details/<slug:slug_text>",brand_details,name="brand_detail"),
    path("products/",ListProducts.as_view(),name="products_list"),
    path("product/details/<slug:slug_text>",ProductDetails.as_view(),name="product_detail"),
]