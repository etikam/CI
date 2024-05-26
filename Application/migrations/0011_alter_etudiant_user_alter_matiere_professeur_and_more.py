# Generated by Django 5.0.4 on 2024-05-15 07:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Application', '0010_alter_etudiant_user_alter_professeur_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='etudiant',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='matiere',
            name='professeur',
            field=models.ForeignKey(limit_choices_to={'is_professeur': True}, on_delete=django.db.models.deletion.CASCADE, to='Application.professeur'),
        ),
        migrations.AlterField(
            model_name='professeur',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
