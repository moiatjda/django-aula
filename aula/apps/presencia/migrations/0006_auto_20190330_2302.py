# Generated by Django 2.1.7 on 2019-03-30 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('presencia', '0005_auto_20180411_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='impartir',
            name='comentariImpartir',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='nohadeseralaula',
            name='motiu',
            field=models.CharField(choices=[('E', 'Expulsat del centre'), ('A', 'Activitat'), ('L', 'Classe Anul·lada')], max_length=5),
        ),
    ]