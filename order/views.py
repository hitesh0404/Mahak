from django.shortcuts import render
from authentication.models import Address
from django.shortcuts import redirect
from cart.models import Cart
from django.contrib import messages
# Create your views here.
def place_order(request):
    if request.user.is_authenticated:
        cart_items = Cart.objects.filter(user = request.user)
        if len(cart_items)==0:  
            messages.warning(request,"Sorry your cart is empty")            
            return redirect("/")
        else:
            messages.info(request,"Select the Address to proceed with")
            return redirect("select_address")
        
def select_address(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            all_address = Address.objects.filter(user = request.user)
            if len(all_address)==0:
                messages.info(request,"Please add your first Address to Place Order")
                return redirect("add_address")
            return render(request,"select_address.html",{"addresses":all_address})
        else:
            pass
