from django.db import models


CHARACTER_CLASS = (
    ('reading', 'Reading'),
    ('exercising', 'Exercising'),
    ('gaming', 'Gaming'),
)


class Character(models.Model):
    """
    Das Character Model.
    Zwei Felder, Name und Klasse (favorite activity).
    Die Klasse hat drei Möglichkeiten: reading, exercising, gaming.
    """
    name = models.CharField(max_length=20, null=False, verbose_name='What would you like to be called?')
    characterClass = models.CharField(max_length=100, choices=CHARACTER_CLASS, null=False, verbose_name='What kind of activity do you prefer?')

    def start(self):
        self.save()

    def __str__(self):
        return self.name


