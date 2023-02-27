from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('/index/', index, name="event"),
    path('/affiche/<str:classe>', affiche, name="affiche"),
    path('/affiche/', ListEvt,name="list"),
    path('/list/',ListEvtGeneric.as_view()),
    path('/detail/<str:title>',Detail,name="D"),
    path('/Ajout/',AjoutEvt,name="Add"),
    path('/AjoutGeneric/',Ajout.as_view()),
    path('/supprimer/<int:id>/', SupprimerEvt, name='supprimer'),
    path('/login',LoginView.as_view(template_name='login.html')),
    path('/logout',LogoutView.as_view(template_name='logout.html')),

]