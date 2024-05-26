# Generated by Django 5.0.4 on 2024-05-24 16:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Application', '0015_anciensujets_annee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='Etudiant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Application.etudiant'),
        ),
        migrations.AlterField(
            model_name='presence',
            name='etudiant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Application.etudiant'),
        ),
    ]