from django import forms
from .models import Etudiant,Professeur,EvalCours

class EtudiantForm(forms.ModelForm):
    matricule = forms.CharField(max_length=50) 
    nom = forms.CharField(max_length=50) 
    prenom = forms.CharField(max_length=50) 
    
    class Meta:
        model = Etudiant
        exclude = ['adresse','tel','user', 'photo_profile']  # Tous les champs du model Etudiant sauf tel et photo_profile 
        '''parce que c'est pas à l'administrateur d'écrire le numero de télphone et la photo de profile de l'Etudiant'''
    

class ProfesseurForm(forms.ModelForm):
    matricule = forms.CharField(max_length=50,required=True)
    nom = forms.CharField(max_length=50,required=True)
    prenom = forms.CharField(max_length=50,required=True)
    

    class Meta:
        model = Professeur
        exclude = ['user','photo_profile']
    
 

class EvalCoursForm(forms.ModelForm):
    class Meta:
        model = EvalCours
        fields = '__all__'
        widgets = {
            'presentation_cours': forms.Select(attrs={'class': 'form-select'}),
            'plan_cours': forms.Select(attrs={'class': 'form-select'}),
            'doc_accompagne': forms.Select(attrs={'class': 'form-select'}),
            'prepa_leçon': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'correppondance_matetplan': forms.Select(attrs={'class': 'form-select'}),
            'condition_materiel': forms.Select(attrs={'class': 'form-select'}),
            'planing_sceance': forms.Select(attrs={'class': 'form-select'}),
            'respect_horaire': forms.Select(attrs={'class': 'form-select'}),
            'nombre_etud_propice': forms.Select(attrs={'class': 'form-select'}),
            'dynamisme_enthousiasme_prof': forms.Select(attrs={'class': 'form-select'}),
            'interet_cours': forms.Select(attrs={'class': 'form-select'}),
            'disponibilite_prof': forms.Select(attrs={'class': 'form-select'}),
            'expression_prof': forms.Select(attrs={'class': 'form-select'}),
            'respect_etudiant': forms.Select(attrs={'class': 'form-select'}),
            'climat_cours': forms.Select(attrs={'class': 'form-select'}),
            'pres_modalite_eval': forms.Select(attrs={'class': 'form-select'}),
            'aspect_eval': forms.Select(attrs={'class': 'form-select'}),
            'delai_correction_travaux': forms.Select(attrs={'class': 'form-select'}),
            'comment_tavaux_eval': forms.Select(attrs={'class': 'form-select'}),
            'sentiment_equite': forms.Select(attrs={'class': 'form-select'}),
            'appreciation_global': forms.Select(attrs={'class': 'form-select'}),
            'points_forts': forms.Select(attrs={'class': 'form-select'}),
            'amelioration_aspects': forms.Select(attrs={'class': 'form-select'}),
            'remarques_precisions_suggestions': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }