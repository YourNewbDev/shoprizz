from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
from django import forms

# Create your views here.
def index(response):
    return render(response, "shop/index.html")

def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            return redirect('index')
        else:
            messages.success(request, ("Problem in registration"))
            return redirect('register')
        
    else:
        return render(request, "shop/register.html", {'form': form})