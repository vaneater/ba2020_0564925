from django.urls import path
from . import views

urlpatterns = [
    # path('', views.start, name='start'),
    path('', views.character_creation, name='character_creation'),
]