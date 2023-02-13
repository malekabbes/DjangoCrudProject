from django.urls import path
from . import views

urlpatterns = [
    path('/index/', views.index, name="event"),
    path('/affiche/', views.affiche, name="affiche")

]