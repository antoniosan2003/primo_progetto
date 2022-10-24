from tkinter import Y
from django.shortcuts import render
import random 
# Create your views here.
def index(request):
    return render(request, "index2.html")

def somma(request):
    x=random.randint(1, 10)
    y=random.randint(1, 10)
    context={
        'var1' : x,
        'var2' : y,
        'somma' : x+y,
    }
    return render(request, "maxmin.html", context)

def media(request):
    return render(request, "media.html")
