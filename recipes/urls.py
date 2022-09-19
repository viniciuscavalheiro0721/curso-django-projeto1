from django.urls import path
from recipes.views import contato, sobre

urlpatterns = [
    path('sobre/', sobre),
    path('contato', contato),
]
