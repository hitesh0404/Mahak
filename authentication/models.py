from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Address(models.Model):
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    address_line_one = models.CharField(max_length=50)
    address_line_two = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pin_code = models.CharField(max_length=8)