from django.shortcuts import render,redirect
from inventory.models import Product
from .models import Cart
from django.contrib import messages
# Create your views here.
def cart_page(request):
    next_url = request.GET.get('next', 'login')
    if request.user.is_authenticated :
        cart_items = Cart.objects.filter(user = request.user)
        context = {
            "cart_items":cart_items
        }
        return render(request,"cartpage.html",context=context)
    else:
        messages.error(request,"You can't access the cart Page as of You are not loged in please Login First..... ")
        return redirect(next_url)

def add_to_cart(request,slug):
    next_url = request.GET.get('next', '/')
    if request.user.is_authenticated :
        product = Product.objects.get(slug=slug)
        user = request.user
        cart_item = Cart.objects.filter(user = user,product= product)
        if len(cart_item)==0:
            Cart.objects.create(user = user,product = product,quantity = 1)
        else:
            cart_item = cart_item[0]
            if not cart_item.quantity >= product.quantity:
                cart_item.quantity += 1
                cart_item.save()
        return redirect(next_url)
    else:
        return redirect(next_url)

def decrease_quantity(request,slug):
    product = Product.objects.get(slug=slug)
    cart_item = Cart.objects.filter(user = request.user,product= product)[0]
    if cart_item.quantity<=1:
        cart_item.delete()
    else:
        cart_item.quantity -= 1
        cart_item.save()
    return redirect("/cart/")
    


def increase_quantity(request,slug):
    product = Product.objects.get(slug=slug)
    cart_item = Cart.objects.filter(user = request.user,product= product)[0]
    if cart_item.quantity >= product.quantity:
         #    1                     10
        messages.warning(request,f"only {cart_item.quantity} qunatity Availble right now of {product.name}")
    else:
        cart_item.quantity += 1
        cart_item.save()
    return redirect("/cart/")