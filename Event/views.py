from Event import forms
from django.views.generic import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.contrib.auth.signals import user_logged_out, user_logged_in
from django.db.models import F


from .forms import AddForm

from .models import *


# Create your views here.


def index(request):
    return HttpResponse('Hello , This Event Page ! 😄')


def affiche(request, classe):
    contexte = {"c": classe}
    return render(request, "Event/affiche.html", contexte)


def ListEvt(request):
    evt = Event.objects.all()
    # Affichage via HttpResponse
    # resultat="----".join(e.title for e in evt)
    # return HttpResponse(resultat)
    # Affichage via render() templates
    return render(request, 'Event/AfficheEvt.html', {'e': evt})
# Methode via Generic


class ListEvtGeneric(LoginRequiredMixin, ListView):
    model = Event
    context_object_name = 'e'
    template_name = "Event/AfficheEvt.html"
    ordering = ['-event_date']


def Detail(request, title):
    event = Event.objects.get(title=title)

    # QuerySet get
    return render(request, "Event/Detail.html", {'t': event})


def AjoutEvt(request):
    if request.method == "GET":
        form = AddForm()
        return render(request, 'Event/Ajout.html', {'f': form})
    if request.method == "POST":
        form = AddForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            if Event.objects.filter(title=title).exists():
                messages.error(
                    request, "Un événement avec ce titre existe déja")
                return render(request, 'Event/Ajout.html', {'f': form})
            else:
                new_evt = form.save(commit=False)
                new_evt.save()
                messages.success(
                    request, "L'événement a été ajouté avec succès !")
                return HttpResponseRedirect(reverse('list'))
        else:
            return render(request, 'Event/Ajout.html',
                          {
                              'f': form,
                              "msg_erreur": "Erreur lors de l'ajout d'un evenement"
                          })


def SupprimerEvt(request, id):
    evt = get_object_or_404(Event, id=id)
    evt.delete()
    messages.success(request, "L'événement a été supprimé avec succès !")
    return redirect('list')


class Ajout(CreateView):
    model = Event
    form_class = AddForm
    success_url = reverse_lazy("Aff")


class DetailGeneric(DetailView):
    model = Event
    context_object_name = 't'
    template_name = "Event/Detail.html"

# ALERTS


def show_message_login(sender, user, request, **kwargs):
    messages.success(request, 'You have logged in.')


def show_message_logout(sender, user, request, **kwargs):
    messages.error(request, 'You are logged out')


def show_message_update(sender, user, request, event_name, **kwargs):
    message = f"{event_name} has been updated."
    messages.success(request, message)


class UpdateEvt(UpdateView):
    model = Event
    form_class = AddForm
    template_name = "Event/Update.html"
    success_url = reverse_lazy("list")
    pk_url_kwarg = "pk"
    pk_field = "pk"

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f"{self.object.title} has been updated")
        return response


user_logged_in.connect(show_message_login)
user_logged_out.connect(show_message_logout)


def Participate(request, evt_id):
    event = Event.objects.get(pk=evt_id)
    if Event_Participation.objects.filter(person=request.user, event=event).count() == 0:
        Event_Participation.objects.create(person=request.user, event=event)
        event.save()
        Event.objects.filter(pk=evt_id).update(
            nbe_participant=F('nbe_participant')+1)
        messages.success(request, "Votre participation est enregistrée")
    else:
        messages.error(request, "Vous participez déjà à cet événement")

    return redirect('list')


def cancelParticipation(request, id):
    event = Event.objects.get(pk=id)
    if Event_Participation.objects.filter(
            person=request.user, event=event).count() == 1:
        Event_Participation.objects.filter(
            person=request.user, event=event).delete()
        event.save()
        Event.objects.filter(pk=id).update(
            nbe_participant=F('nbe_participant')-1
        )
        messages.success(request, "Votre participation est annulée")
    else:
        messages.error(request, "Vous ne participez pas à cet événement")

    return redirect('list')
