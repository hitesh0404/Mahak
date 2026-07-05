from django.db import models
from django.contrib.auth.models import User
from authentication.models import Address
from inventory.models import Product
# Create your models here.

STATUS_CHOICES = [
    ("placed", "Placed"),
    ("dispatched", "Dispatched"),
    ("out_for_delivery", "Out for Delivery"),
    ("delivered", "Delivered"),
    ("cancelled", "Cancelled"),
    ("returned", "Returned"),
]

class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    address = models.ForeignKey(Address,on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=20,choices=STATUS_CHOICES,default="placed")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

class OrderDetail(models.Model):
    order = models.ForeignKey(Order,on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product,on_delete=models.DO_NOTHING)
    quantity = models.IntegerField()