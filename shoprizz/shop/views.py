from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(response):
    return render(response, "shop/index.html")

def register(response):
    return render(response, "shop/register.html")