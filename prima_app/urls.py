from django.urls import path
from prima_app.views import homepage,welcome,lista,chisiamo,variabili,index,es_if

app_name="prima_app"
urlpatterns=[
    path('home', homepage, name='homepage'), 
    path('welcome', welcome, name='welcome' ),
    path('lista', lista, name='lista'),
    path('chisiamo', chisiamo, name='chisiamo'),
    path('variabili', variabili, name='variabili'),
    path('', index, name='index'),
]
app_name="seconda_app"
urlpatterns=[
    path('es_if', es_if, name='es_if'),
]



