from django import forms
from .models import Character


class CharacterForm(forms.ModelForm):
    """
    Die Form des Character Models.
    Dort werden alle Felder, Name und Klasse (favorite activity) angezeigt.
    Darüber hinaus gibt die form in der __init__ Methode den Feldern Klassen,
    wodurch die Eingabefelder mit CSS verändert werden.
    """
    class Meta:
        model = Character
        fields = ('name', 'characterClass', )

    def __init__(self, *args, **kwargs):
        super(CharacterForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'myfieldclass'})
        self.fields['characterClass'].widget.attrs.update({'class': 'myfieldclass'})


class EmptyForm(forms.ModelForm):
    """
    Eine leere Form, damit diese in den Methoden survived und death aufgerufen werden kann.
    Alle Felder des Character Models werden ausgelassen.
    """
    class Meta:
        model = Character
        exclude = ('name', 'characterClass', )



