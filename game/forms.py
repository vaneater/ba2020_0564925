from django import forms
from .models import Character


class CreateCharacter(forms.ModelForm):
    class Meta:
        model = Character
        fields = ('name',)

    def clean_name(self):
        name = self.cleaned_data.get('name')
        qs = Character.objects.filter(name = name)
        if qs.exists():
            raise forms.ValidationError("This adventurer already exists!")
        return name

