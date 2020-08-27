from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Character


# Create your views here.

# falls ein login vorhanden sein wird, dann hier drüber wählen,
# ob man einen neuen charakter erstellt (registrieren), oder ob
# man mit einem bisherigen charakter weiter macht (login)

# def start(request):
#     return render(request, 'game/start.html', {})

def character_creation(request):
    # charakter über datenbank nur vom jeweiligen user anzeigen.. vllt mit dem namen?
    # so???? character = Character.objects.filter(name=name.now())
    return render(request, 'game/character_creation.html', {})


def page_1(request):
    return render(request, 'game/page_1.html', {})


def page_2_choice_follow(request):
    return render(request, 'game/page_2_choice_follow.html', {})


def page_2_choice_run(request):
    return render(request, 'game/page_2_choice_run.html', {})


def page_2_choice_shout(request):
    return render(request, 'game/page_2_choice_shout.html', {})


def page_3_choice_help(request):
    return render(request, 'game/page_3_choice_help.html', {})


def page_3_choice_ask(request):
    return render(request, 'game/page_3_choice_ask.html', {})


def page_3_choice_leave(request):
    return render(request, 'game/page_3_choice_leave.html', {})




