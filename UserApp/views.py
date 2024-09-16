from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index_us(request):
    return HttpResponse("Pagina principal users")

