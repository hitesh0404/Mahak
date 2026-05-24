from django.urls import path
from .views import *
urlpatterns = [
    path("",home,name="home"),
    path("home/",home),
    path("about/",about_us),
    path("contact/",contact_us),
    path("logout/",my_logout),
]