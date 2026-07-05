from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login
from django.http import HttpResponseBadRequest
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .forms import RegisterForm,LoginForm
from django.contrib import messages
from .forms import AddressForm
from django.views import View
from .models import Address
from django import forms


def register(request):
    if request.method == "GET":

        form = RegisterForm()
        context = {'form':form}
        return render(request,"register.html",context)
    
    elif request.method=="POST":

        form = RegisterForm(data=request.POST)
        context = {'form':form}
        if form.is_valid():
            user = form.save(commit=False)
            if request.POST.get("password") ==  request.POST.get("confirm_password"):
                User.set_password(user,request.POST.get("password"))
                user.save()
                messages.success(request,"Successfully Registered, Now You can Log in")
                return redirect("login")
            else:
                messages.error(request,"Password and Confirm Password doesn't match")
                return render(request,'register.html',context)
        else:
            messages.error(request,"Invalid Form Details")
            return render(request,"register.html",context)
    else:
        messages.error(request,"Bad Request")
        return HttpResponseBadRequest("Bad Request")

class Login(View):
    def get(self,request):
        form = LoginForm()
        return render(request,"login.html",{"form":form})
    def post(self,request):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect("home")
        else:
            return render(request,"login.html",{"form":form})
        
def my_login(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request,"login.html",{"form":form})
    elif request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect("home")
        else:
            return render(request,"login.html",{"form":form})


class AddAddress(View):
    def get(self,request):
        form = AddressForm()
        return render(request,"add_address.html",{"form":form})
    def post(self,request):
        next = request.POST.get('next', "/")
        form = AddressForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user
            address.save()
            messages.success(request,f"Address of {form.cleaned_data['address_line_one']} added successfully ")
            return redirect(next) 
        else: 
            return render(request,"add_address.html",{"form":form})


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

@login_required
def profile(request):
    addresses = Address.objects.filter(user=request.user)

    return render(request, "profile.html", {
        "addresses": addresses
    })
@login_required
def update_profile(request):

    if request.method == "POST":
        form = UserUpdateForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully.")
            return redirect("profile")

    else:
        form = UserUpdateForm(instance=request.user)

    return render(request, "update_profile.html", {
        "form": form
    })

@login_required
def delete_address(request, id):

    address = Address.objects.get(id=id, user=request.user)
    address.delete()

    messages.success(request, "Address deleted successfully.")

    return redirect("profile")




