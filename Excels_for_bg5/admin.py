from django.contrib import admin
from .models import *
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class UtilisateurResource(resources.ModelResource):
    class Meta:
        model = Utilisateur
        fields = ('username', 'first_name', 'last_name', 'departemen', 'licence', 'is_anonyme', 'is_Etudiant', 'is_professeur', 'is_directeur', 'is_secretaire', 'is_chef_departement')
        import_id_fields = ['username']


@admin.register(Utilisateur)
class UtilisateurAdmin(ImportExportModelAdmin, UserAdmin):
    resource_class = UtilisateurResource
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser', 'ine', 'pv', 'pere', 'mere', 'date_naissance', 'lieu_naissance', 'ecole_origine', 'departemen', 'licence', 'tel', 'photo_profile', 'is_anonyme', 'is_Etudiant', 'is_professeur', 'is_directeur', 'is_secretaire', 'is_chef_departement')

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Informations personnelles', {'fields': ('first_name', 'last_name', 'email', 'ine', 'pv', 'pere', 'mere', 'date_naissance', 'lieu_naissance', 'ecole_origine', 'departemen', 'licence', 'tel', 'photo_profile', 'is_anonyme', 'is_Etudiant', 'is_professeur', 'is_directeur', 'is_secretaire', 'is_chef_departement')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Dates importantes', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )
    list_filter = ('is_Etudiant','is_professeur')


@admin.register(Departement)
class DepartementAdmin(admin.ModelAdmin):
    list_display = ['libele']
    prepopulated_fields = {'slug': ('libele',)}

# Register your models here.


@admin.register(Licence)
class LicenceAdmin(admin.ModelAdmin):
    list_display = ('libele',)
    prepopulated_fields ={'slug':('libele',)}


@admin.register(Semestre)
class SemestreAdmin(admin.ModelAdmin):
    list_display = ('libele','licence')
    prepopulated_fields ={'slug':('libele',)}


@admin.register(Matiere)
class MatiereAdmin(admin.ModelAdmin):
    '''Admin View for Matiere'''

    list_display = ('libele','semestre','professeur')
    prepopulated_fields ={'slug':('libele',)}


@admin.register(Brochure)
class BrochureAdmin(admin.ModelAdmin):
    '''Admin View for salle'''


@admin.register(Jour)
class JourAdmin(admin.ModelAdmin):
    '''Admin View for Jour'''

    list_display = ('jour',)


@admin.register(Emploi)
class EmploiAdmin(admin.ModelAdmin):
    '''Admin View for Emploi'''
    list_display = ('semestre','professeur','licence','departement','matiere','jour','salle','heure_deb','heure_fin')
    list_filter =('licence','semestre')


@admin.register(Type_opportunite)
class Type_opportuniteAdmin(admin.ModelAdmin):
    list_display = ("libele",)
    prepopulated_fields = {'slug':('libele',)}


@admin.register(Opportunite)
class Opportunite(admin.ModelAdmin):
    list_display = ('type_op','description','partenaire','piece_jointe')
    list_filter = ('type_op',)


@admin.register(Partenaire)
class PartenaireAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    prepopulated_fields = {'slug':('nom',)}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    '''Admin View for Poste'''
    list_display = ('matricule','nom','prenom','telephone','adresse','email','motivation','partenaire','opportunite')
    list_filter = ('opportunite',)

@admin.register(Notes)
class NotesAdmin(admin.ModelAdmin):
    list_dispaly =('Etudiant','note1','note2','note3','moyenne')


@admin.register(PhotoCarousel)
class PhotoCarouselAdmin(admin.ModelAdmin):
    '''Admin View for '''

    list_display = ('nom','image','description')


@admin.register(MembresEquipe)
class MembresEquipeAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'contact')


@admin.register(Presence)
class PresenceAdmin(admin.ModelAdmin):

    list_display = ('etudiant','matiere','date',"present",'absent')
    list_filter = ('date','present','matiere','absent','etudiant')


@admin.register(Heure)
class HeureAdmin(admin.ModelAdmin):
    '''Admin View for Heure'''

    list_display = ('libele',)


@admin.register(Salle)
class SalleAdmin(admin.ModelAdmin):
    '''Admin View for Salle'''

    list_display = ('libele',)


@admin.register(VideoTemoignage)
class VideoTemoignageAdmin(admin.ModelAdmin):
    list_display = ('titre', 'video', 'description')


@admin.register(Galery)
class GaleryAdmin(admin.ModelAdmin):
    list_display = ('description', 'image')


@admin.register(TypeEvent)
class TypeEventAdmin(admin.ModelAdmin):
    list_display = ('type', 'slug')
    prepopulated_fields = {'slug':('type',)}


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('type', 'description','date')


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('nom', 'email', 'numero_telephone', 'contenu', 'date_enregistrement')


@admin.register(EvalCours)
class EvalCoursAdmin(admin.ModelAdmin):
    list_display = ('titre_du_cours', 'presentation_cours', 'plan_cours', 'doc_accompagne', 'prepa_leçon',
                    'correppondance_matetplan', 'condition_materiel', 'planing_sceance', 'respect_horaire',
                    'nombre_etud_propice', 'dynamisme_enthousiasme_prof', 'interet_cours', 'disponibilite_prof',
                    'expression_prof', 'respect_etudiant', 'climat_cours', 'pres_modalite_eval', 'aspect_eval',
                    'delai_correction_travaux', 'comment_travaux_eval', 'sentiment_equite', 'appreciation_global',
                    'points_forts', 'amelioration_aspects', 'remarques_precisions_suggestions')


@admin.register(DocumentAdmin)
class DocumentAdminAdmin(admin.ModelAdmin):
    list_display = ('noms', 'niveau', 'departement', 'matricule', 'email', 'filiation', 'infos_naissance',
                    'docu_demande', 'date_de_soumission')
