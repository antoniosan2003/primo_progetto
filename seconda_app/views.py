from django.shortcuts import render

# Create your views here.
def es_if(request):
    context = {
        'var1' : 100,
        'var2' : 100.0,
        'var3' : 100.50
    }
    return render(request, "es_if.html", context)