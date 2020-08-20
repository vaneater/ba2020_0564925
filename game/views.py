from django.shortcuts import render


# Create your views here.

# falls ein login vorhanden sein wird, dann hier drüber wählen,
# ob man einen neuen charakter erstellt (registrieren), oder ob
# man mit einem bisherigen charakter weiter macht (login)

# def start(request):
#     return render(request, 'game/start.html', {})

def character_creation(request):
    return render(request, 'game/character_creation.html', {})

def page_1(request):
    return render(request, 'game/page_1.html', {})

def page_2_choice_follow(request):
    return render(request, 'game/page_2_choice_follow.html', {})

def page_2_choice_run(request):
    return render(request, 'game/page_2_choice_run.html.html', {})

def page_2_choice_shout(request):
    return render(request, 'game/page_2_choice_shout.html', {})
