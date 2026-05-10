from django.shortcuts import render
from .models import Brand
# Create your views here.

def list_all_brands(request):
    brands = Brand.objects.all()
    context = {
        "brands":brands
    }
    print(brands[0].name)
    return render(request,"brands_list.html",context= context)