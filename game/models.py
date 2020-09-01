from django.db import models

# HALLO... JEDES mal wenn du diese datei änderst, dann MUSST du
# python manage.py makemigrations game
# python manage.py migrate game
# machen !!!!!!!!!!!!!

"""class Character(models.Model):
    name = models.CharField(max_length=20, blank=False, default="Your Name")
    strength = models.PositiveSmallIntegerField(default=1, max_length=16)
    magic = models.PositiveSmallIntegerField(default=1, max_length=16)
    knowledge = models.PositiveSmallIntegerField(default=1, max_length=16)

    def start(self):
        self.save()
        # daten in datenbank speichern

    def __str__(self):
        return self.name"""


class Character(models.Model):
    name = models.CharField(max_length=20, blank=False, default="Your Name")
    strength = models.PositiveSmallIntegerField(default=1, max_length=16)
    magic = models.PositiveSmallIntegerField(default=1, max_length=16)
    knowledge = models.PositiveSmallIntegerField(default=1, max_length=16)

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


class CharacterManage(models.Model):
    def create_character(self, name, strength, magic, knowledge):
        if not name:
            raise ValueError('Your Character needs to have a name!')

        character = self.model(name=self.normalize_name(name), )

        character.save(using=self._db)
        return character
