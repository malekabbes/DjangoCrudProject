# Generated by Django 4.1.5 on 2023-03-06 10:07

import Person.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Person', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name': 'Personne'},
        ),
        migrations.AlterField(
            model_name='person',
            name='cin',
            field=models.IntegerField(primary_key=True, serialize=False, validators=[Person.models.Person.cin_length], verbose_name='CIN'),
        ),
    ]
