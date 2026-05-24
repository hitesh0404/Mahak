from django.shortcuts import render
from .models import Brand,Product

def list_all_brands(request):
    brands = Brand.objects.all()
    context = {
        "brands":brands
    }
    print(brands[0].name)
    return render(request,"brands_list.html",context= context)

def list_all_products(request):
    p = Product.objects.all()
    context = {
        "products":p
    }
    return render(request,"product_list.html",context= context)



def product_details(request,slug_text):
    p = Product.objects.get(slug = slug_text )
    context = {
        "product":p
    }
    return render(request,"product_details.html",context= context)



def brand_details(request,slug_text):
    p = Brand.objects.get(slug = slug_text )
    context = {
        "brand":p
    }
    return render(request,"brand_details.html",context= context)
