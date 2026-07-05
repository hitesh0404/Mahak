from django.urls import path
from .views import *
urlpatterns = [
    path("select-address/",select_address,name="select_address"),
    path("place-order/",place_order,name="place_order"),
]