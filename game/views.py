from django.shortcuts import render, redirect, get_object_or_404
from .models import Character
from .forms import CharacterForm


# Create your views here.

# falls ein login vorhanden sein wird, dann hier drüber wählen,
# ob man einen neuen charakter erstellt (registrieren), oder ob
# man mit einem bisherigen charakter weiter macht (login)

def first_start(request):
    return render(request, 'game/first_start.html', {})


"""def page_1(request):
    if request.method == 'POST':
        newcharacter = Character(request.POST)
        if newcharacter.is_valid():
            name = newcharacter.cleaned_data['name']
            strength = newcharacter.cleaned_data['strength']
            magic = newcharacter.cleaned_data['magic']
            knowledge = newcharacter.cleaned_data['knowledge']
            newcharacter.save()
            return redirect('game/page_1.html', pk=newcharacter.pk)
            print(name)

    character = Character()
    return render(request, 'game/page_1.html', {'newcharacter': newcharacter})
"""


def character_creation(request):
    print("die request method ist:", request)
    if request.method == "POST":
        form = CharacterForm(request.POST)
        print("vor dem if form.is_valid() ")
        if form.is_valid():
            print("im valid yay")
            character = form.save(commit=False)
            character.save()
            print("nach dem save")
            print("jetzt komt der list versuch")
            this_character_name = Character.objects.get(pk=character.pk)
            print("nach dem versuch, jetzt return")
            return render(request, 'game/page_1.html', {'this_character_name': this_character_name})
    else:
        print("im else, falls keine post method")
        form = CharacterForm()
    print("if request.method übersprungen")
    return render(request, 'game/character_creation.html', {'form': form})


def delete_character(request, pk):
    if request.method == 'DELETE':
        character_to_delete = Character.objects.get(pk=pk)
        character_to_delete.delete()
    return redirect('first_start')


def get_name(request, pk):
    this_character_name = Character.objects.get(pk=pk)
    print("nach dem versuch, jetzt return")
    return render(request, 'game/page_1.html', {'this_character_name': this_character_name})


def page_1(request):
    return render(request, 'game/page_1.html', {})


def page_2_choice_follow(request, pk):
    this_character_name = Character.objects.get(pk=pk)
    return render(request, 'game/page_2_choice_follow.html', {})


def page_2_choice_run(request):
    return render(request, 'game/page_2_choice_run.html', {})


def page_2_choice_shout(request):
    return render(request, 'game/page_2_choice_shout.html', {})


def page_3_choice_book(request):
    if Character.get_character_class() == Character.get_character_class() == 'reading' or 'gaming':
        return render(request, 'game/page_3_choice_book.html', {})
    else:
        return render(request, 'game/death.html')


def page_3_choice_sword(request):
    if Character.get_character_class() == 'exercising' or Character.get_character_class() == 'gaming':
        return render(request, 'game/page_3_choice_sword.html', {})
    else:
        return render(request, 'game/death.html')


def page_3_choice_leave(request):
    return render(request, 'game/page_3_choice_leave.html', {})
