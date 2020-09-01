from django.shortcuts import render
from .forms import CreateCharacter
from .models import Character



# Create your views here.

# falls ein login vorhanden sein wird, dann hier drüber wählen,
# ob man einen neuen charakter erstellt (registrieren), oder ob
# man mit einem bisherigen charakter weiter macht (login)


def character_creation(request):
    return render(request, 'game/character_creation.html', {})


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


def page_1(request):
    template_name = 'game/character_creation.html'
    form_class = CreateCharacter
    queryset = Character.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return render(request, 'game/page_1.html', {'character': Character})

    return render(request, 'game/page_1.html', {'character': Character})


def page_2_choice_follow(request):
    return render(request, 'game/page_2_choice_follow.html', {})


def page_2_choice_run(request):
    return render(request, 'game/page_2_choice_run.html', {})


def page_2_choice_shout(request):
    return render(request, 'game/page_2_choice_shout.html', {})


def page_3_choice_book(request):
    if Character.magic.__lt__(3):
        return render(request, 'game/page_3_choice_book.html', {})
    else:
        return render(request, 'game/death.html')


def page_3_choice_sword(request):
    if Character.strength.__lt__(3):
        return render(request, 'game/page_3_choice_sword.html', {})
    else:
        return render(request, 'game/death.html')


def page_3_choice_leave(request):
    return render(request, 'game/page_3_choice_leave.html', {})
