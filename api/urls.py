from django.urls import path
from .views import api_products_view,ProductAPI,ProductDetail
urlpatterns = [
    path("products/list/",api_products_view,name="api_products_list"),
    path("products/",ProductAPI.as_view(),name="api_products"),
    path("products/<int:pk>",ProductDetail.as_view(),name="api_products_details"),
]
