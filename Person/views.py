from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import FormSignUp
from django.contrib.auth import login
# Create your views here.

def index(request):
    return HttpResponse('Hello , This Person Page ! 😄 ')

def SignUp(request):
    form = FormSignUp()
    print('REQQQ',request)
    if request.user.is_authenticated:
        return redirect('Aff')
    if request.method == "POST":
        form = FormSignUp(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('Aff')
    return render(request, 'Person/signup.html', {'form': form})
    
