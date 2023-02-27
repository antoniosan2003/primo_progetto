from django.contrib import admin
from django.urls import path, include
from forms_app.views import contatti

urlpatterns = [
    path('contattaci/', contatti, name='contatti'),
]