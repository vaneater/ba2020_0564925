from django.conf import settings
from django.conf.urls import url
from django.urls import path
from . import views
import django.views.static


urlpatterns = [
    path('', views.first_start, name='first_start'),
    path('first_start/character_creation/', views.character_creation, name='character_creation'),
    path('page_1/survived/', views.survived, name='survived'),
    path('page_1/death/', views.death, name='death'),
    url(r'^static/(?P<path>.*)$', django.views.static.serve, {'document_root': settings.STATIC_ROOT, 'show_indexes': settings.DEBUG})
]
