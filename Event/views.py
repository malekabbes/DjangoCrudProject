from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

from .forms import AddForm

from.models import *
from django.views.generic import *

from Event import forms

# Create your views here.

def index(request):
    return HttpResponse('Hello , This Event Page ! 😄')
def affiche(request,classe):
    contexte = {"c":classe}
    return render(request,"Event/affiche.html",contexte)
def ListEvt(request):
    evt=Event.objects.all()
    #Affichage via HttpResponse
    # resultat="----".join(e.title for e in evt)
    # return HttpResponse(resultat)
    #Affichage via render() templates
    return render(request,'Event/AfficheEvt.html',{'e':evt})
#Methode via Generic
class ListEvtGeneric(ListView):
    model=Event
    context_object_name='e'
    #On garde le template par defaut event_list.html
    #fields="__all__"
    template_name="Event/AfficheEvt.html"
    ordering=['-event_date']
def Detail(request,title):
    event=Event.objects.get(title=title)
    return render(request,"Event/Detail.html",{'t':event})

def AjoutEvt(request):
    if request.method == "GET":
        form= AddForm()
        return render(request,'Event/Ajout.html',{'f':form})
    if request.method=="POST":
        form=AddForm(request.POST)
        if form.is_valid():
            title=form.cleaned_data['title']
            if Event.objects.filter(title=title).exists():
                messages.error(request,"Un événement avec ce titre existe déja")
                return render(request,'Event/Ajout.html',{'f':form})
            else:
                new_evt=form.save(commit=False)
                new_evt.save()
                messages.success(request, "L'événement a été ajouté avec succès !")
                return HttpResponseRedirect(reverse('list'))            
        else:
            return render(request,'Event/Ajout.html',
                          {
                'f':form,
                "msg_erreur":"Erreur lors de l'ajout d'un evenement"
                          })
def SupprimerEvt(request,id):
    evt=get_object_or_404(Event,id=id)
    evt.delete()
    messages.success(request,"L'événement a été supprimé avec succès !")
    return redirect('list')

