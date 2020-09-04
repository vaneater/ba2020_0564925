from django import forms
from .models import Character
from django.db.models import Q


class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = ('name', 'characterClass', )

    def __init__(self, *args, **kwargs):
        super(CharacterForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'myfieldclass'})
        self.fields['characterClass'].widget.attrs.update({'class': 'myfieldclass'})






