from django.shortcuts import render, redirect, get_object_or_404
from .models import Character
from .forms import CharacterForm, EmptyForm


def first_start(request):
    return render(request, 'game/first_start.html', {})


def character_creation(request):
    """
    Ruft in first_start.html zuerst character_creation.html auf.
    Da es sich beim zweiten Aufruf um eine POST methode handelt, geht die Methode in das if rein.
    Danach wird die CharacterForm aufgerufen.
    Falls diese valid ist, wird sie gespeichert, und man wird auf page_1.html weitergeleitet.
    Dabei wird der Name übergeben.
    """
    if request.method == "POST":
        form = CharacterForm(request.POST)
        if form.is_valid():
            character = form.save(commit=False)
            character.save()
            this_character_name = Character.objects.get(pk=character.pk)
            return render(request, 'game/page_1.html', {'this_character_name': this_character_name, 'pk': character.pk})
    else:
        form = CharacterForm()
    return render(request, 'game/character_creation.html', {'form': form})


def survived(request):
    """
    Ruft in page_1.html  zuerst die survived.html auf.
    Danach wird die eine leere EmptyForm aufgerufen, damit nichts erscheint.
    Da es sich beim zweiten Aufruf, beim drücken auf den "Delete current character" button,
    um eine GET methode handelt, geht die Methode in das if rein.
    Dort wird der eigene gerade benutzte Character dann gelöscht.
    Dabei wird der Name übergeben und man wird an den Anfang bei first_start.html weitergeleitet.
    (Ich hab ehrlich gesagt keine Ahnung, wieso ich diese Methode so seltsam aufgebaut habe.
    Ich habe vieles probiert, und dies hat dann letztendlich am besten funktioniert.)
    """
    this_character_name = Character.objects.last()
    if request.method == "GET":
        form = EmptyForm(request.POST)
        this_character_name.delete()
        return render(request, 'game/first_start.html', {'this_character_name': this_character_name})
    else:
        form = EmptyForm()
    return render(request, 'game/survived.html', {'this_character_name': this_character_name})


def death(request):
    """
    Die selbe Methode wie bei survived, nur dass man in der Story gestorben ist.
    Ruft in page_1.html  zuerst die survived.html auf.
    Danach wird die eine leere EmptyForm aufgerufen, damit nichts erscheint.
    Da es sich beim zweiten Aufruf, beim drücken auf den "Delete current character" button,
    um eine GET methode handelt, geht die Methode in das if rein.
    Dort wird der eigene gerade benutzte Character dann gelöscht.
    Dabei wird der Name übergeben und man wird an den Anfang bei first_start.html weitergeleitet.
    (Ich hab ehrlich gesagt keine Ahnung, wieso ich diese Methode so seltsam aufgebaut habe.
    Ich habe vieles probiert, und dies hat dann letztendlich am besten funktioniert.)
    """
    this_character_name = Character.objects.last()
    if request.method == "GET":
        form = EmptyForm(request.POST)
        this_character_name.delete()
        return render(request, 'game/first_start.html', {'this_character_name': this_character_name})
    else:
        form = EmptyForm()
    return render(request, 'game/death.html', {'this_character_name': this_character_name})



