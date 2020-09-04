from django.shortcuts import render, redirect, get_object_or_404
from .models import Character
from .forms import CharacterForm


# Create your views here.

# falls ein login vorhanden sein wird, dann hier drüber wählen,
# ob man einen neuen charakter erstellt (registrieren), oder ob
# man mit einem bisherigen charakter weiter macht (login)

def first_start(request):
    return render(request, 'game/first_start.html', {})


def character_creation(request):
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


def page_1(request):
    return render(request, 'game/page_1.html', {})


def delete(request):
    print("im delete")
    character_to_delete = Character.objects.last()
    character_to_delete.delete()
    return render((request, 'game/first_start.html', {}))


def page_2_choice_follow(request):
    character = Character.objects.last()
    this_character_name = character.get_name()
    print("name bekommen aber was ist er")
    if request.method == "POST":
        print("im delete drin")
        character_to_delete = Character.objects.get(pk=character.pk)
        character_to_delete.delete()
        return render(request, 'game/first_start.html', {'this_character_name': this_character_name})
    print("im zweiten return")
    return render(request, 'game/page_2_choice_follow.html', {'this_character_name': this_character_name})


def page_2_choice_run(request):
    character = Character.objects.last()
    this_character_name = character.get_name()
    print("name bekommen aber was ist er")
    if request.method == "POST":
        print("im delete drin")
        character_to_delete = Character.objects.get(pk=character.pk)
        character_to_delete.delete()
        return render(request, 'game/first_start.html', {'this_character_name': this_character_name})
    print("im zweiten return")
    return render(request, 'game/page_2_choice_run.html', {'this_character_name': this_character_name})


def page_2_choice_shout(request):
    character = Character.objects.last()
    this_character_name = character.get_name()
    this_character_class = character.get_character_class()
    print("name bekommen aber was ist er")
    if request.method == "POST":
        print("im delete drin")
        character_to_delete = Character.objects.get(pk=character.pk)
        character_to_delete.delete()
        return render(request, 'game/first_start.html', {'this_character_name': this_character_name})
    print("im zweiten return")
    return render(request, 'game/page_2_choice_shout.html', {'this_character_name': this_character_name})


def survived(request):
    this_character_name = Character.objects.last()
    return render(request, 'game/survived.html', {'this_character_name': this_character_name})


def survived(request):
    this_character_name = Character.objects.last()
    return render(request, 'game/survived.html', {'this_character_name': this_character_name})


def death(request):
    this_character_name = Character.objects.last()
    return render(request, 'game/death.html', {'this_character_name': this_character_name})
