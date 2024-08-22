from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User


# Create your models here.

#===================LES DEPARTEMENTS============================================================
class Departement(models.Model):
    libele = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(default="description du département")
    photo = models.ImageField(upload_to='photo_département', blank=True, null=True)
    def __str__(self):
        return self.libele
    
#===============LES LICENCES===================================================================
class Licence(models.Model):
    numero = models.IntegerField()
    # departement = models.ForeignKey(Departement, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.numero}'
    pass

#===============LES SEMESTRES=================================================================
class Semestre(models.Model):
    numero = models.IntegerField()
    licence = models.ForeignKey(Licence, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.numero} - {self.licence}'


#=================PROFILE DES ETUDIANTS===========================================================
class Etudiant(models.Model):
    # username qui Represente le Matricule est déjà defini dans le AbstractUser
    # email est déjà defini dans le AbstractUser

    #liaison avec la base table User pour correspondre un utilisateur à un profile Etudiant
    user = models.OneToOneField(User, on_delete=models.CASCADE,blank=True,null=True)
    ine = models.CharField(max_length=50, unique=True)  # INE attribué au Etudiant par Gupol
    pv = models.CharField(max_length=20, unique=True)  # PV du bac
    # nom: le nom se trouve deja dans le AbstractUser comme first_name
    # prenom: le prenom se trouve déjà dans le AbstractUser comme last_name
    pere = models.CharField(max_length=50)  # le prenom du père
    mere = models.CharField(max_length=100)  # le nom complet de la mère
    date_naissance = models.DateField(max_length=10,default="1900-01-01")
    lieu_naissance = models.CharField(max_length=50)
    ecole_origine = models.CharField(max_length=10)
    departement = models.ForeignKey(Departement, on_delete= models.CASCADE)
    #licence = models.ForeignKey(Licence,on_delete=models.CASCADE,blank=True, null=True)
    licence = models.ForeignKey(Licence, on_delete=models.CASCADE)
    genre = models.BooleanField(default=True)
    adresse = models.CharField(max_length=50, default ="Conakry")
  
    tel = models.CharField(max_length=50,blank=True, null=True)
    photo_profile = models.ImageField(upload_to="img_profile_etudiant", blank=True, null=True)
    # is_etudiant = models.BooleanField(default=True,editable=False) #l'attribut editable=False interdit l'edition de ce champ pour que l'Etudiant reste Etudiant, qu'il n'ya aucune possibilité de decocher ce champ
    def __str__(self):
         if self.user:
           return f"{self.user.username} - {self.user.last_name} {self.user.first_name}"
         else:
             return "Etudiant sans utilisateur associé"
   
#=================PROFILE DES PROFESSEURS==================================================
class Professeur(models.Model):
    #les Attributs des Professeurs
    #liaison avec la table User pour faire correspondre un professeur à un profile
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    titre =models.CharField(max_length=4,choices=(("Dr.","Dr."),
                                     ("Mr.","Mr."),
                                     ("Pr.","Pr."),
                                     ("Mme.","Mme.")
                                     ))
    description = models.TextField()  #ici quelques description du professeur et de la matière/des patières qu'il enseigne
    tel = models.CharField(max_length=50,blank=True, null=True)
    competence = models.TextField( blank=True, null=True)
    photo_profile = models.ImageField(upload_to="img_profile_prof", blank=True, null=True)
    # is_professeur = models.BooleanField(default=True, editable=False) #l'attribut editable=False interdit l'edition de ce champ pour que le professeur reste professeur, qu'il n'ya aucune possibilité de decocher ce champ
    def __str__(self):
         if self.user:
             return f"{self.user.username} - {self.user.last_name} {self.user.first_name}"
         else:
             return "Professeur sans utilisateur associé"
    
#================LES MATIERES/COURS =================================================

class Matiere(models.Model):
    libele = models.CharField(max_length=255)
    slug = models.SlugField()
    semestre = models.ForeignKey(Semestre, on_delete=models.CASCADE)
    professeur = models.ForeignKey(Professeur, on_delete=models.CASCADE)
    departement = models.ForeignKey(Departement, on_delete=models.CASCADE)
    description = models.TextField(default="description de la matière")
    image = models.ImageField(upload_to="image_matiere", blank=True, null=True)
    def __str__(self):
        return self.libele

# model de fichiers pour les documents de chaque matière

class Brochure(models.Model):
    titre = models.CharField(max_length=255)
    doc = models.FileField(upload_to='documents_televerser', max_length=100)
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for Brochure."""

        verbose_name = 'Brochure'
        verbose_name_plural = 'Brochures'

    def __str__(self):
        return self.titre

# La tables des anciens sujets d'une matière
class AncienSujets(models.Model):
    image = models.ImageField(upload_to='ancien_sujets')
    annee = models.IntegerField()
    matiere = models.ForeignKey(Matiere,on_delete=models.CASCADE)


#==============La table des Projets Réalisés dans une matière============================
class Projets(models.Model):
    titre = models.CharField(max_length=50)  #pour le titre du projet
    description = models.TextField()        #la description du projet
    membres = models.ManyToManyField(Etudiant) #les Etudiants qui ont participé à la réalisation du projets
    lien = models.CharField(max_length=255, blank=True, null=True)
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return f'{self.titre}'




# =====================creation de la table des notes======================

class Notes(models.Model):
    Etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    note1 = models.FloatField(default=0.0)
    note2 = models.FloatField(default=0.0)
    note3 = models.FloatField(default=0.0)
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)

    def moyenne(self) -> float:
        return round((self.note1 * 0.3) + (self.note2 * 0.3) + (self.note3 * 0.4),2)

    def observation(self):
        if self.moyenne() < 3.5:
            return "Dette"
        if self.moyenne() < 5.0:
            return "Session"

        if self.moyenne() >= 5.0:
            return "Validé"
    def __str__(self):
         return f'{self.Etudiant.user.first_name}   {self.Etudiant.user.last_name}==={self.matiere.libele}'
    class Meta:
        # Ajoutez la contrainte unique
        unique_together = [['Etudiant','matiere',]]

# Creation de la table Partenaire
class Partenaire(models.Model):
    nom = models.CharField(max_length=50)
    slug = models.SlugField()
    logo = models.ImageField(upload_to='logo_partenaire', blank=True, null=True)

    def __str__(self):
        return self.nom


class Type_opportunite(models.Model):
    libele = models.CharField(max_length=10)
    slug = models.SlugField()

    def __str__(self):
        return self.libele


class Opportunite(models.Model):
    titre = models.CharField(max_length=200)
    type_op = models.ForeignKey(Type_opportunite, on_delete=models.CASCADE)
    description = models.TextField(default="votre description ici")
    partenaire = models.ForeignKey(Partenaire, on_delete=models.CASCADE)
    piece_jointe = models.FileField(upload_to='documents_televerser', max_length=100, blank=True, null=True)
    date_pub = models.DateTimeField(auto_now=True)
    date_limite = models.DateTimeField(null=True, blank=True)
    slug = models.SlugField()    


class Post(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, blank=True, null=True)
    matricule = models.CharField(max_length=50)
    opportunite = models.CharField(max_length=50)
    partenaire = models.CharField(max_length=50)
    motivation = models.TextField()
    adresse = models.CharField(max_length=255)
    telephone = models.CharField(max_length=50)
    code_post = models.IntegerField()
    
    def __str__(self):
        return f'{self.nom} {self.prenom}'
    


class Evenement(models.Model):
    libele = models.CharField(max_length=50)
    description = models.TextField()
    date_deb = models.DateTimeField(default='08:00:00')
    date_fin = models.DateTimeField(default='12:00:00')
    image = models.ImageField(upload_to='image_evenement', blank=True, null=True)


class Message(models.Model):
    nom = models.CharField(max_length=50)
    email = models.EmailField(max_length=30)
    contenu = models.TextField()
    models.DateField(auto_now=True)


class Salle(models.Model):
    libele = models.CharField(max_length=50)

    def __str__(self):
        return self.libele


class Jour(models.Model):
    jour = models.CharField(max_length=50)

    def __str__(self):
        return self.jour
    
class Heure(models.Model):
    '''Model de definition for Heure'''
    libele = models.TimeField(auto_now = False, auto_now_add = False, unique = True)

class Emploi(models.Model):
    """Model definition for Emploi."""
    departement = models.ForeignKey(Departement, on_delete=models.CASCADE)
    licence = models.ForeignKey(Licence, on_delete=models.CASCADE)
    semestre = models.ForeignKey(Semestre, on_delete=models.CASCADE)
    professeur = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,limit_choices_to={'is_professeur': True})
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)
    salle = models.ForeignKey(Salle, on_delete=models.CASCADE)
    heure_deb = models.TimeField(auto_now=False, auto_now_add=False)
    heure_fin = models.TimeField(auto_now=False, auto_now_add=False)
    jour = models.ForeignKey(Jour, on_delete=models.CASCADE)
    class Meta:
        unique_together = ('jour', 'heure_deb', 'heure_fin', 'salle')

    def __str__(self):
        return f'{self.professeur.last_name} {self.matiere.libele} {self.jour} {self.salle.libele}'


class PhotoCarousel(models.Model):
    nom = models.CharField(max_length=50)
    image = models.ImageField(upload_to='photo_carousel', blank=True, null=True)
    description = models.TextField()
    


class MembresEquipe(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='photo_membre', blank=True, null=True)
    facebook = models.CharField(max_length=255, blank=True,null=True)
    linkdekdin = models.CharField(max_length=255,blank=True,null=True)
    github = models.CharField(max_length=255,blank=True,null=True)
    


class Presence(models.Model):
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)
    date = models.DateField(auto_now=False)
    present = models.BooleanField()
    absent = models.BooleanField()
    

class VideoTemoignage(models.Model):
    titre = models.CharField(max_length=50)
    video = models.FileField(upload_to='video_temoignage', blank=True, null=True)
    description = models.TextField()
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titre


class EvalCours(models.Model):
    choix=[("Totalement en Désaccord","Totalement en Désaccord"),
             ("En Désaccord","En Désaccord"),
             ("Plutot en Désaccord","Plutot en Désaccord"),
             ("D'accord","D'accord"),
             ("Plutôt D'accord","Plutôt D'accord"),
            ("Tout à fait D'accord","Tout à fait D'accord"),
            ("Aucun Avis","Aucun Avis"),
    ]
    cours = models.CharField(max_length = 150)
    presentation_cours = models.CharField(max_length=50, choices=choix)
    plan_cours = models.CharField(max_length=50,choices=choix)
    doc_accompagne = models.CharField(max_length=50,choices=choix)
    prepa_leçon = models.TextField()
    correppondance_matetplan = models.CharField(max_length=50,choices=choix)
    condition_materiel = models.CharField(max_length=50,choices=choix)
    planing_sceance = models.CharField(max_length=50,choices=choix)
    respect_horaire = models.CharField(max_length=50,choices=choix)
    nombre_etud_propice = models.CharField(max_length=50, null=True,choices=choix)
    dynamisme_enthousiasme_prof = models.CharField(max_length=50, null=True,choices=choix)
    interet_cours = models.CharField(max_length=50, null=True,choices=choix)
    disponibilite_prof = models.CharField(max_length=50, null=True,choices=choix)
    expression_prof = models.CharField(max_length=50, null=True,choices=choix)
    respect_etudiant = models.CharField(max_length=50, null=True , choices=choix)
    climat_cours = models.CharField(max_length=50, null=True, choices=choix)
    pres_modalite_eval = models.CharField(max_length=50, null=True, choices=choix)
    aspect_eval = models.CharField(max_length=50, null=True, choices=choix)
    delai_correction_travaux = models.CharField(max_length=50, null=True, choices=choix)
    comment_tavaux_eval = models.CharField(max_length=50, null=True, choices=choix)
    sentiment_equite = models.CharField(max_length=50, null=True, choices=choix)
    appreciation_global = models.CharField(max_length=50, null=True, choices=choix)
    points_forts = models.CharField(max_length=50, null=True, choices=choix)
    amelioration_aspects = models.CharField(max_length=50, null=True, choices=choix)
    remarques_precisions_suggestions = models.TextField(null=True)
    

class Galery(models.Model):
    description = models.CharField(max_length=20)
    image = models.ImageField(upload_to="image_galery", height_field=None, width_field=None, max_length=None)
    

class TypeEvent(models.Model):
    type = models.CharField(max_length=50)
    slug = models.SlugField()
    
    def __str__(self):
        return self.type
    

class Event(models.Model):
    type = models.ForeignKey(TypeEvent, on_delete=models.CASCADE)
    description = models.TextField()
    date = models.DateTimeField(auto_now=False, auto_now_add=False)