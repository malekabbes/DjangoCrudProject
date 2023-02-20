from django.urls import path
from .views import *

urlpatterns = [
    path('/index/', index, name="event"),
    path('/affiche/<str:classe>', affiche, name="affiche"),
    path('/affiche/', ListEvt,name="list"),
    path('/list/',ListEvtGeneric.as_view()),
    path('/detail/<str:title>',Detail,name="D"),
    path('/Ajout/',AjoutEvt,name="Add"),
    path('/supprimer/<int:id>/', SupprimerEvt, name='supprimer'),


]