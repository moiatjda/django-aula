# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-09 17:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aules', '0004_auto_20180416_1033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservaaula',
            name='motiu',
            field=models.CharField(help_text="Explica el motiu de la reserva o del canvi d'aula.\n                             (Ex: Inclem\xe8ncies del temps.)\n                             (Ex: Visita pares.)\n                             Important: No entreu dades sensibles en aquest camp, no entreu noms d'alumnes ni noms de fam\xedlies,\n                             la primera frase d'una reserva pot ser p\xfablica a tothom.", max_length=120),
        ),
    ]
