from django.shortcuts import render

# Create your views here.
def es_if(request):
    context = {
        'var1' : 100,
        'var2' : 100.0,
        'var3' : 100.50
    }
    return render(request, "es_if.html", context)

def es_for(request):
    context = {
        'list1': [1, datetime.date(2019,7,16), 'Do not give up!'],
        'list2': [1, datetime.date(2019,7,16), 'Do not give up!'],
    }
    return render(request, "es_for.html", context)