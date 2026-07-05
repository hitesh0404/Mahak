from django.urls import path
from .views import *

urlpatterns = [

    path("register/",register,name="register"),  
    path("login/",Login.as_view(),name="login"),
    path("add-address/",AddAddress.as_view(),name="add_address"),
    path("delete-address/<int:id>/", delete_address, name="delete_address"),
    path("profile/update/", update_profile, name="update_profile"),
    path("profile/", profile, name="profile"),

]