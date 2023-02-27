from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('/index/', index, name="event"),
    path('/affiche/<str:classe>', affiche, name="affiche"),
    path('/affiche/', ListEvt,name="list"),
    path('/list/', ListEvtGeneric.as_view()),

    path('/detail/<str:title>',Detail,name="D"),
    path('/Ajout/',AjoutEvt,name="Add"),
    path('/<int:pk>/update/',UpdateEvt.as_view(template_name='update.html'),name="update"),
    path('/AjoutGeneric/',Ajout.as_view()),
    path('/supprimer/<int:id>/', SupprimerEvt, name='supprimer'),
    path('/login',LoginView.as_view(template_name='login.html'),name="login"),
    path('/logout',LogoutView.as_view(template_name='logout.html'),name="logout"),

]