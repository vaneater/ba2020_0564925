# Generated by Django 2.2.12 on 2020-08-30 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='knowledge',
            field=models.PositiveIntegerField(default=1, max_length=16),
        ),
        migrations.AddField(
            model_name='character',
            name='magic',
            field=models.PositiveIntegerField(default=1, max_length=16),
        ),
        migrations.AddField(
            model_name='character',
            name='name',
            field=models.CharField(default='Your Name', max_length=20),
        ),
        migrations.AddField(
            model_name='character',
            name='strength',
            field=models.PositiveIntegerField(default=1, max_length=16),
        ),
    ]