from tkinter import Y
from django.shortcuts import render
import random 
# Create your views here.
def index(request):
    return render(request, "index2.html")

def maxmin(request):
    x=random.randint(1, 10)
    y=random.randint(1, 10)
    context={
        'var1' : x,
        'var2' : y,
        'somma' : x+y,
    }
    return render(request, "maxmin.html", context)

def media(request):
    lista = []
    for i in range(30):
        lista.append(random.randint(0,10))
    context = {
        "lista": lista,
        "media":sum(lista)/len(lista),
    }
    return render(request, "media.html", context)
