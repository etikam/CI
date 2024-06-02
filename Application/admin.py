from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import *
from django.contrib import admin
from .forms import EtudiantForm, ProfesseurForm
from django.contrib.auth.admin import UserAdmin 
from import_export import resources
from .resources import EtudiantResource
from import_export.admin import ImportExportModelAdmin

'''
    Cette configuration permet aux tables(models) de votre fichier models.py de 

        s'afficher dans l'interface d'administration selon votre configuration. 

    !!! Vous ne verrez pas une table dans l'interface d'administration de votre application si elle n'est pas configurée ici (sauf la table des Utilisateur (User))
'''

#===========DEPARTEMENT==========================================
@admin.register(Departement)
class DepartementAdmin(admin.ModelAdmin):
    list_display = ['libele']
    prepopulated_fields = {'slug': ('libele',)}
    

#===========lICENCE==========================================
@admin.register(Licence)
class LicenceAdmin(admin.ModelAdmin):
    list_display = ('numero',)
   

#===========SEMESTRE==========================================
@admin.register(Semestre)
class SemestreAdmin(admin.ModelAdmin):
    list_display = ('numero',)

#===========MATIERE==========================================

@admin.register(Matiere)
class MatiereAdmin(admin.ModelAdmin):
    list_display = ('libele', 'semestre', 'professeur')
    prepopulated_fields = {'slug': ('libele',)}

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        # Si c'est une nouvelle matière, créer les instances de Notes pour chaque étudiant existant
        if not change:  # 'change' est False lors de la création d'un nouvel objet
            etudiants = Etudiant.objects.all()
            for etudiant in etudiants:
                Notes.objects.create(Etudiant=etudiant, matiere=obj, note1=0.0, note2=0.0, note3=0.0)

@admin.register(Projets)
class ProjetAdmin(admin.ModelAdmin):
    model= Projets

@admin.register(AncienSujets)
class AncienSujetsAdmin(admin.ModelAdmin):
    model= AncienSujets
#===========BROCHURE==========================================
@admin.register(Brochure)
class BrochureAdmin(admin.ModelAdmin):
    '''Admin View for salle'''
   

#===========JOUR==========================================
@admin.register(Jour)
class JourAdmin(admin.ModelAdmin):
    '''Admin View for Jour'''

    list_display = ('jour',)
    
#===========EMPLOI==========================================
@admin.register(Emploi)
class EmploiAdmin(admin.ModelAdmin):
    '''Admin View for Emploi'''
    list_display = ('semestre','professeur','licence','departement','matiere','jour','salle','heure_deb','heure_fin')
    list_filter =('licence','semestre')

#===========TYPE_OPPORTUNITÉ====================================
@admin.register(Type_opportunite)
class Type_opportuniteAdmin(admin.ModelAdmin):
    list_display = ("libele",)
    prepopulated_fields = {'slug':('libele',)}


#===========OPPORTUNITÉ==========================================
@admin.register(Opportunite)
class Opportunite(admin.ModelAdmin):
    list_display = ('titre','type_op','description','partenaire','piece_jointe')
    list_filter = ('type_op',)
    prepopulated_fields = {'slug':('titre',)}

#===========PARTENAIRE==========================================
@admin.register(Partenaire)
class PartenaireAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    prepopulated_fields = {'slug':('nom',)}
    
#===========POST==========================================
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    '''Admin View for Poste'''
    list_display = ('matricule','nom','prenom','telephone','adresse','email','motivation','partenaire','opportunite')
    list_filter = ('opportunite',)

#===========NOTES==========================================

class DepartementFilter(admin.SimpleListFilter):
    title = 'Département'
    parameter_name = 'departement'

    def lookups(self, request, model_admin):
        departements = set([e.departement for e in Etudiant.objects.all()])
        return [(d.id, d.libele) for d in departements]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(Etudiant__departement__id=self.value())
        return queryset

class LicenceFilter(admin.SimpleListFilter):
    title = 'Licence'
    parameter_name = 'licence'

    def lookups(self, request, model_admin):
        licences = set([e.licence for e in Etudiant.objects.all()])
        return [(l.id, l.numero) for l in licences]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(Etudiant__licence__id=self.value())
        return queryset

class NotesAdmin(admin.ModelAdmin):
    list_display = ('Etudiant', 'note1', 'note2', 'note3', 'moyenne')
    list_filter = (DepartementFilter, LicenceFilter, 'matiere')

admin.site.register(Notes, NotesAdmin)
#===========PHOTO_CAROUSEL==========================================
@admin.register(PhotoCarousel)
class PhotoCarouselAdmin(admin.ModelAdmin):
    '''Admin View for '''
    list_display = ('nom','image','description')

#===========MEMBRE_EQUIPE==========================================
@admin.register(MembresEquipe)
class MembresEquipeAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'contact')


#===========PRESENCE==========================================
@admin.register(Presence)
class PresenceAdmin(admin.ModelAdmin):
    list_display = ('etudiant','matiere','date',"present",'absent')
    list_filter = ('date','present','matiere','absent','etudiant')
    
#===========HEURE==========================================
@admin.register(Heure)
class HeureAdmin(admin.ModelAdmin):
    '''Admin View for Heure'''

    list_display = ('libele',)

#===========SALLE==========================================
@admin.register(Salle)
class SalleAdmin(admin.ModelAdmin):
    '''Admin View for Salle'''
    list_display = ('libele',)

#===========VIDEO_TEMOIGNAGE==========================================
@admin.register(VideoTemoignage)
class VideoTemoignageAdmin(admin.ModelAdmin):
    list_display = ('titre', 'video', 'description')
    
#===========GALERY==========================================
@admin.register(Galery)
class GaleryAdmin(admin.ModelAdmin):
    list_display = ('description', 'image')

#===========TYPE_EVENT (TYPE D'EVENEMENT)==========================================
@admin.register(TypeEvent)
class TypeEventAdmin(admin.ModelAdmin):
    list_display = ('type', 'slug')
    prepopulated_fields = {'slug':('type',)}

#===========EVENT (EVENEMENTS)==========================================
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('type', 'description','date')



#=================ADMINISTRATION DU FORMULAIRE D'ENREGISTREMENT DES ETUDIANTS TOUT EN LES LIANT AU FORMULAIRE USER  ===============================

@admin.register(Etudiant)
class EtudiantAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = EtudiantResource
    form = EtudiantForm

    def save_model(self, request, obj, form, change):
        user, created = User.objects.get_or_create(
            username=form.cleaned_data['matricule'],
            defaults={
                'first_name': form.cleaned_data['prenom'],
                'last_name': form.cleaned_data['nom'],
                'is_active': False,
                'password': 'CI2023@2024',
            }
        )
        if created:
            user.set_password('CI2023@2024')
            user.save()
        obj.user = user
        super().save_model(request, obj, form, change)

        matieres = Matiere.objects.all()
        for matiere in matieres:
            Notes.objects.get_or_create(etudiant=obj, matiere=matiere)


#=================ADMINISTRATION DU FORMULAIRE D'ENREGISTREMENT DES PROFESSEURS TOUT EN LES LIANT AU FORMULAIRE USER  ===============================
@admin.register(Professeur)
class ProfesseurAdmin(admin.ModelAdmin):
    form = ProfesseurForm
 
   
    def save_model(self, request, obj, form, change):
                                        #Créer l'utilisateur avec les données recuperée du formulaire (uniquement les données concernant le User model)
        user = User.objects.create_user(username=form.cleaned_data['matricule'],
                                        password='PROCI2023@2024',
                                        first_name=form.cleaned_data['prenom'],
                                        last_name=form.cleaned_data['nom'],
        )

        # Enregistrer l'utilisateur
        user.save()

        # Créer l'étudiant associé à cet utilisateur (avec les information du meme formulaire mais qui sont destinées à être enregistrées dans le model Etudiant cette fois-ci)
        professeur = Professeur(user=user,
                            titre=form.cleaned_data['titre'],
                            tel=form.cleaned_data['tel'],
                           
                            description=form.cleaned_data['description'],

        )

        # Enregistrer l'étudiant
        professeur.save()
