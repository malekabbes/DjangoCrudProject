from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('Hello , This Event Page ! 😄')
def affiche(request):
    return render(request,"Event/affiche.html")