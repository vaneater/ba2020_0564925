from django.urls import path
from . import views

urlpatterns = [
    path('', views.first_start, name='first_start'),
    path('first_start/character_creation/', views.character_creation, name='character_creation'),
    path('page_1/survived/', views.survived, name='survived'),
    path('page_1/death/', views.death, name='death'),

]
