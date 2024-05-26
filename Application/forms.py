from django import forms
from .models import Etudiant,Professeur

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
    
    