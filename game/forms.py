from django import forms
from .models import Character


class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = ('name', 'characterClass', )

    def __init__(self, *args, **kwargs):
        super(CharacterForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'myfieldclass'})
        self.fields['characterClass'].widget.attrs.update({'class': 'myfieldclass'})


"""     def clean_name(self):
        name = self.cleaned_data.get('name')
        qs = Character.objects.filter(name = name)
        if qs.exists():
            raise forms.ValidationError("This adventurer already exists!")
        return name """

