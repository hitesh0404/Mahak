from django.forms import ModelForm,Form
from django.contrib.auth.models import User
from django import forms
from .models import Address


class RegisterForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(max_length=50, widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['username',"first_name","last_name", 'email']
        # fields = "__all__"

class LoginForm(Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput())
    
class AddressForm(ModelForm):
    class Meta:
        model = Address
        exclude = ["user"]

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']