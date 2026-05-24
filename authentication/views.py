from django.shortcuts import render,redirect
from django.http import HttpResponseBadRequest
from .forms import RegisterForm,LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

# Create your views here.
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
                return redirect("login")
            else:
                return render(request,'register.html',context)
        else:
            return render(request,"register.html",context)
    else:
        return HttpResponseBadRequest("Bad Request")

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
