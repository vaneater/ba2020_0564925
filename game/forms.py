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

    def get_nameform(self):
        print("in form")
        return self.name


"""     
    def start(self):
        self.save()

    def delete_character(self, *args, **kwargs):
        self.name.delete()
        self.characterClass.delete()
        super().delete(*args, *kwargs)



        def clean_name(self):
        name = self.cleaned_data.get('name')
        qs = Character.objects.filter(name = name)
        if qs.exists():
            raise forms.ValidationError("This adventurer already exists!")
        return name """

