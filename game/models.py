from django.conf import settings
from django.db import models
from django.utils import timezone

# HALLO... JEDES mal wenn du diese datei änderst, dann MUSST du
# python manage.py makemigrations game
# machen !!!!!!!!!!!!!

class Character(models.Model):
    # name = models.ForeignKey()
    # strength = models.ForeignKey()
    # magic = models.ForeignKey()
    # knowledge = models.ForeignKey()
    # character_name = models.ForeignKey()


    def start(self):
        self.save()
        # daten in datenbank speichern
        # nächste seite öffnen