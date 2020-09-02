from django.db import models

# HALLO... JEDES mal wenn du diese datei änderst, dann MUSST du
# python manage.py makemigrations game
# python manage.py migrate game
# machen !!!!!!!!!!!!!

"""
class Character(models.Model):
    name = models.CharField(max_length=20, blank=False, default="Your Name")
    strength = models.PositiveSmallIntegerField(default=1, max_length=16)
    magic = models.PositiveSmallIntegerField(default=1, max_length=16)
    knowledge = models.PositiveSmallIntegerField(default=1, max_length=16)

    def save_character(self):
        self.save()

    def __str__(self):
        return self.name

    def get_name(self):
        return self.name

    def get_strength(self):
        return self.strength

    def get_magic(self):
        return self.magic

    def get_knowledge(self):
        return self.knowledge
"""

CHARACTER_CLASS = (
    ('reading', 'Reading'),
    ('exercising', 'Exercising'),
    ('gaming', 'Gaming'),
)

"""
reading -> good in knowledge and magic
exercising -> good in strength and knowledge 
gaming -> good in magic and strength
"""


class Character(models.Model):
    name = models.CharField(max_length=20, blank=False, default="Your Name", verbose_name='What would you like to be called?')
    characterClass = models.CharField(max_length=11, choices=CHARACTER_CLASS, blank=False, verbose_name='What kind of activity do you prefer?')

    def __str__(self):
        return self.name

    def get_name(self):
        return self.name

    def get_character_class(self):
        return self.characterClass

    def start(self):
        self.save()

    def delete_character(self, *args, **kwargs):
        self.name.delete()
        self.characterClass.delete()
        super().delete(*args, *kwargs)

