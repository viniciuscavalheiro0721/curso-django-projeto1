from django.http import HttpResponse
from django.shortcuts import render


def sobre(request):
    return render(request, 'home.html')


def contato(request):
    return HttpResponse("contato")
# Create your views here.
