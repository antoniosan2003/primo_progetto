from django.urls import path
from prova_pratica_0.views import index,maxmin,media

app_name="prova_pratica_0"
urlpatterns=[
    path('', index, name='index'),
    path('somma', maxmin, name='somma'),
    path('media', media, name='media'),
]
