# Generated by Django 5.0.4 on 2024-06-03 10:54

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Departement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libele', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
                ('description', models.TextField(default='description du département')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='photo_département')),
            ],
        ),
        migrations.CreateModel(
            name='EvalCours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('presentation_cours', models.CharField(max_length=50)),
                ('plan_cours', models.CharField(max_length=50)),
                ('doc_accompagne', models.CharField(max_length=50)),
                ('prepa_leçon', models.TextField()),
                ('correppondance_matetplan', models.CharField(max_length=50)),
                ('condition_materiel', models.CharField(max_length=50)),
                ('planing_sceance', models.CharField(max_length=50)),
                ('respect_horaire', models.CharField(max_length=50)),
                ('nombre_etud_propice', models.CharField(max_length=50, null=True)),
                ('dynamisme_enthousiasme_prof', models.CharField(max_length=50, null=True)),
                ('interet_cours', models.CharField(max_length=50, null=True)),
                ('disponibilite_prof', models.CharField(max_length=50, null=True)),
                ('expression_prof', models.CharField(max_length=50, null=True)),
                ('respect_etudiant', models.CharField(max_length=50, null=True)),
                ('climat_cours', models.CharField(max_length=50, null=True)),
                ('pres_modalite_eval', models.CharField(max_length=50, null=True)),
                ('aspect_eval', models.CharField(max_length=50, null=True)),
                ('delai_correction_travaux', models.CharField(max_length=50, null=True)),
                ('comment_tavaux_eval', models.CharField(max_length=50, null=True)),
                ('sentiment_equite', models.CharField(max_length=50, null=True)),
                ('appreciation_global', models.CharField(max_length=50, null=True)),
                ('points_forts', models.CharField(max_length=50, null=True)),
                ('amelioration_aspects', models.CharField(max_length=50, null=True)),
                ('remarques_precisions_suggestions', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Evenement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libele', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('date_deb', models.DateTimeField(default='08:00:00')),
                ('date_fin', models.DateTimeField(default='12:00:00')),
                ('image', models.ImageField(blank=True, null=True, upload_to='image_evenement')),
            ],
        ),
        migrations.CreateModel(
            name='Galery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to='image_galery')),
            ],
        ),
        migrations.CreateModel(
            name='Heure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libele', models.TimeField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Jour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jour', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Licence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MembresEquipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('prenom', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=50)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='photo_membre')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=30)),
                ('contenu', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Partenaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
                ('logo', models.ImageField(blank=True, null=True, upload_to='logo_partenaire')),
            ],
        ),
        migrations.CreateModel(
            name='PhotoCarousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='photo_carousel')),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('prenom', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('matricule', models.CharField(max_length=50)),
                ('opportunite', models.CharField(max_length=50)),
                ('partenaire', models.CharField(max_length=50)),
                ('motivation', models.TextField()),
                ('adresse', models.CharField(max_length=255)),
                ('telephone', models.CharField(max_length=50)),
                ('code_post', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Salle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libele', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Type_opportunite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libele', models.CharField(max_length=10)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='TypeEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='VideoTemoignage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=50)),
                ('video', models.FileField(blank=True, null=True, upload_to='video_temoignage')),
                ('description', models.TextField()),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Etudiant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ine', models.CharField(max_length=50, unique=True)),
                ('pv', models.CharField(max_length=20, unique=True)),
                ('pere', models.CharField(max_length=50)),
                ('mere', models.CharField(max_length=100)),
                ('date_naissance', models.DateField(default='1900-01-01', max_length=10)),
                ('lieu_naissance', models.CharField(max_length=50)),
                ('ecole_origine', models.CharField(max_length=10)),
                ('genre', models.BooleanField(default=True)),
                ('adresse', models.CharField(default='Conakry', max_length=50)),
                ('tel', models.CharField(blank=True, max_length=50, null=True)),
                ('photo_profile', models.ImageField(blank=True, null=True, upload_to='img_profile_etudiant')),
                ('departement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Application.departement')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('licence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Application.licence')),
            ],
        ),
        migrations.CreateModel(
            name='Matiere',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libele', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
                ('description', models.TextField(default='description de la matière')),
                ('image', models.ImageField(blank=True, null=True, upload_to='image_matiere')),
                ('departement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Application.departement')),
            ],
        ),
        migrations.CreateModel(
            name='Brochure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=255)),
                ('doc', models.FileField(upload_to='documents_televerser')),
                ('date', models.DateTimeField(auto_now=True)),
                ('matiere', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Application.matiere')),
            ],
            options={
                'verbose_name': 'Brochure',
                'verbose_name_plural': 'Brochures',
            },
        ),
        migrations.CreateModel(
            name='AncienSujets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='ancien_sujets')),
                ('annee', models.IntegerField()),
                ('matiere', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Application.matiere')),
            ],
        ),
        migrations.CreateModel(
            name='Presence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('present', models.BooleanField()),
                ('absent', models.BooleanField()),
                ('etudiant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Application.etudiant')),
                ('matiere', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Application.matiere')),
            ],
        ),
        migrations.CreateModel(
            name='Professeur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(choices=[('Dr.', 'Dr.'), ('Mr.', 'Mr.'), ('Pr.', 'Pr.'), ('Mme.', 'Mme.')], max_length=4)),
                ('description', models.TextField()),
                ('tel', models.CharField(blank=True, max_length=50, null=True)),
                ('competence', models.TextField(blank=True, null=True)),
                ('photo_profile', models.ImageField(blank=True, null=True, upload_to='img_profile_prof')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='matiere',
            name='professeur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Application.professeur'),
        ),
        migrations.CreateModel(
            name='Projets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('lien', models.CharField(blank=True, max_length=255, null=True)),
                ('matiere', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Application.matiere')),
                ('membres', models.ManyToManyField(to='Application.etudiant')),
            ],
        ),
        migrations.CreateModel(
            name='Semestre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
                ('licence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Application.licence')),
            ],
        ),
        migrations.AddField(
            model_name='matiere',
            name='semestre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Application.semestre'),
        ),
        migrations.CreateModel(
            name='Opportunite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=200)),
                ('description', models.TextField(default='votre description ici')),
                ('piece_jointe', models.FileField(blank=True, null=True, upload_to='documents_televerser')),
                ('date_pub', models.DateTimeField(auto_now=True)),
                ('date_limite', models.DateTimeField(blank=True, null=True)),
                ('slug', models.SlugField()),
                ('partenaire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Application.partenaire')),
                ('type_op', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Application.type_opportunite')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('date', models.DateTimeField()),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Application.typeevent')),
            ],
        ),
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note1', models.FloatField(default=0.0)),
                ('note2', models.FloatField(default=0.0)),
                ('note3', models.FloatField(default=0.0)),
                ('Etudiant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Application.etudiant')),
                ('matiere', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Application.matiere')),
            ],
            options={
                'unique_together': {('Etudiant', 'matiere')},
            },
        ),
        migrations.CreateModel(
            name='Emploi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heure_deb', models.TimeField()),
                ('heure_fin', models.TimeField()),
                ('departement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Application.departement')),
                ('professeur', models.ForeignKey(limit_choices_to={'is_professeur': True}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('jour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Application.jour')),
                ('licence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Application.licence')),
                ('matiere', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Application.matiere')),
                ('salle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Application.salle')),
                ('semestre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Application.semestre')),
            ],
            options={
                'unique_together': {('jour', 'heure_deb', 'heure_fin', 'salle')},
            },
        ),
    ]
