from django.urls import path
from prima_app.views import homepage,welcome,lista,chisiamo

app_name="prima_app"
urlpatterns=[
    path('home', homepage, name='homepage'), 
    path('welcome', welcome, name='welcome' ),
    path('lista', lista, name='lista'),
    path('chisiamo', chisiamo, name='chisiamo'),
]

