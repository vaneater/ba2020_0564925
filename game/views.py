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


def page_3_choice_book(request):
    character = Character.objects.last()
    this_character_class = character.get_character_class()
    if this_character_class == 'reading' or this_character_class == 'gaming':
        return render(request, 'game/page_3_choice_book.html', {'this_character_class': this_character_class})
    else:
        return render(request, 'game/death.html')


def page_3_choice_sword(request):
    character = Character.objects.last()
    this_character_class = character.get_character_class()
    if this_character_class == 'exercising' or this_character_class == 'gaming':
        return render(request, 'game/page_3_choice_sword.html', {'this_character_class': this_character_class})
    else:
        return render(request, 'game/death.html')


def page_3_choice_leave(request):
    return render(request, 'game/page_3_choice_leave.html', {})
