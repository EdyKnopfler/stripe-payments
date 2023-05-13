#from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Aqui irá a home page da Kollins Tec.")
