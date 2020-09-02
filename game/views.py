from django.shortcuts import render, redirect
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
            form.save()
            model = form.instance
            #character = form.save(commit=False)
            #character.name = request.name
            #character.save()
            return redirect('first_start')
    else:
        form = CharacterForm()
    return render(request, 'game/character_creation.html', {'form': form})

    """def form_valid(self, form):
        print(form.cleaned_data)
        return render(request, 'game/page_1.html', {'character': Character})

    return render(request, 'game/page_1.html', {'character': Character})"""


def deletecharacter(request, pk):
    if request.method == 'POST':
        character = Character.objects.get(pk=pk)
        character.delete()
    return redirect('first_start')


def page_1(request):
    return render(request, 'game/page_1.html', {})


def page_2_choice_follow(request):
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
