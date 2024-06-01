'''Importation des modules'''
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from PIL import Image

User = get_user_model()
# Création des vues
#=====================PAGE D'ACCUEIL=====================================
def index(request):
    
    videoTemoignage  = VideoTemoignage.objects.all()
    professeurs = Professeur.objects.all()
    cours = Matiere.objects.all()[:6]
    context = {
        'videoTemoignage':videoTemoignage,
        'professeurs':professeurs,
        'cours':cours,
    } 
    return render(request, 'accueil/index.html',context)
    # ==================================================================


# ====================COTE AUTHENTIFICATION=============================

#============ATIVATION DE COMPTE ETUDIANT=========================

def activation_compte(request,username):
    non_correspondance =" "
    deja_active=""
    U = get_object_or_404(User,username=username)


    '''
    on doit recuperer:
        le numero (pour la table Etudiant)
        la photo de profile (pour la table Etudiant)
        l'Adresse (pour la table Etudiant)
        l'Email ( pour la table user)
        mot de pass (pour la table user)
        recuperer la checkbox de connexion automatique
    '''
    
    if request.method == "POST":
        # Récupération des données du formulaire
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        adresse = request.POST.get('adresse')
        telephone = request.POST.get('telephone')
        auto_connect = request.POST.get("auto_connect")

        if password1 == password2:
        # Mise à jour des informations utilisateur
    
            U.email = email
            U.set_password(password1)
            U.is_active=True
            U.save()
        
        # Mise à jours de du profil de l'Etudiant
            etudiant = get_object_or_404(Etudiant,user=U)
            if adresse:
                etudiant.adresse = adresse
            if telephone:
                etudiant.telephone = telephone
            # if photo:
            #     etudiant.photo_profile = photo

            etudiant.save()
        
        
        
        # Connexion de l'utilisateur

        if auto_connect:
            U = authenticate(request, username=username, password=password1)
            if U is not None:
                login(request, U)
        
        # Redirection ou autre traitement après activation du compte
            return redirect(index)

    

    context = {
        'U':U
    }
    return render(request, 'account/activation.html',context)
    # ====================================================================================================================

        #Vérification de l'existence des Informations de l'Etudiant
def chercher_etudiant(request):
    error_info_not_found =""
    if request.method == "POST":
        
        ine = request.POST.get('ine')
        pv = request.POST.get('pv')
        try:
            etudiant = Etudiant.objects.get(ine=ine,pv=pv)
            u = etudiant.user
            print(u)
            return redirect(activation_compte, username=u.username)
        except:
            error_info_not_found ="Informations Incorrecte"

    context = {
        'error':error_info_not_found,
    }
    return render(request,'account/verifier.html', context)








def update_password(request, username):
    mot_de_passe_non_identique = ""
    if request.method=="GET":
        return redirect('index')
    if request.method == "POST":
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 == password2:
            utilisateur = get_object_or_404(get_user_model(), username=username)
            if utilisateur:
                utilisateur.set_password(password1)
                utilisateur.save()
                return redirect('index')
        else:
            mot_de_passe_non_identique = "Les mots de passe saisis ne correspondent pas"
    
    return render(request, 'Application/update_password.html', {'mot_de_passe_non_identique': mot_de_passe_non_identique,'username':username})


def connexion(request):
    print("la connexion est appelée")
    auth_error_message=""
    if request.method == "POST": 
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            print("je l'ai connecté")
            messages.success(request,"Vous êtes connecté")
            return redirect('index')
        else:
            # Ajout du message d'erreur dans la session
            messages.error(request, "Matricule ou mot de passe incorrect.")
           
    return render(request,'account/login.html')

# def index(request):
    
#     galerie = Galery.objects.all()
#     carouspic = PhotoCarousel.objects.all()
#     # for image in carouspic:
#     #     img_path = image.image.path
#     #     img = Image.open(img_path)
#     #     img_resized = resizeimage.resize_crop(img, (800, 600))
#     #     img_resized.save(img_path)
#     prog = Departement.objects.all()
#     prof = User.objects.filter(is_professeur=True)
#     programmer = MembresEquipe.objects.all()
#     paginator = Paginator(prof, 3)
#     page = request.GET.get('page')
#     try:
#         prof = paginator.page(page)
#     except PageNotAnInteger:
#         prof = paginator.page(1)
#     except EmptyPage:
#         prof = paginator.page(paginator.num_pages)

#     context = {
#         'carousImg': carouspic, 
#         'prof': prof, 
#         'prog': prog, 
#         'equip': programmer,
#         'galerie':galerie
#         }
#     return render(request, 'Application/index.html', context)

    # ====================================================================================================================

def cours(request):
        print("je suis dans la vue")
        context={}
        semestres = Semestre.objects.all()
        departements = Departement.objects.all()
        programmes = Matiere.objects.all()
        if request.method == "POST":
            print("je suis dans le post")
            # Récupérez les filtres de la requête GETS
            semestre_choosed = request.POST['semestre']
            departement_choosed = request.POST['departement']
            print(f'semestre {semestre_choosed}')
            # Appliquez les filtres
            if departement_choosed:
                programmes = programmes.filter(departement__slug=departement_choosed)
            if semestre_choosed:
                programmes = programmes.filter(semestre__numero=semestre_choosed)

        context = {
            'cours': programmes,
            'semestres': semestres,
            'departements': departements,
        }

        return render(request, 'cours/index.html', context)

login_required(login_url='connexion')
def programme_details(request, slug):
    programme = get_object_or_404(Matiere, slug=slug)
    brochures = Brochure.objects.filter(matiere=programme)
    projets = Projets.objects.filter(matiere=programme) #les projets réalisés dans la matières 
    sujets = AncienSujets.objects.filter(matiere=programme) #les anciens sujets de la matière
    professeur = programme.professeur
    nombre_de_projets = len(projets)
    annee_dispo = {sujet.annee for sujet in sujets}
    #en plus recuperation des projets réalisé dans la matières( mais c'est pas encore implementer dans les models)
    context = {
        "cour": programme,
        "brochures": brochures,
        "professeur": professeur,
        "projets": projets,
        "sujets": sujets,
        "nb_projet":nombre_de_projets,
        "annee_dispo": list(annee_dispo),
        }
    return render(request, 'cours/detailCours/detail.html',context)


# Vue qui renvoie l'emploi du temps d'un semestre
@login_required(login_url='connexion')
def Emploi_du_temps(request):
    # departement_choisi = request.GET.get("departement")
    # licence_choisi = request.GET.get("licence")
    # emploi = Emploi.objects.all()

    # licence = Licence.objects.all()  # Récupération de toutes les licences
    # semestre = Semestre.objects.all()  # Récupération de tous les semestres
    # departement = Departement.objects.all()  # Récupération de tous les semestres

    # # Filtre en fonction du departement
    # if departement_choisi and departement_choisi != "Toutes":
    #     emploi = emploi.filter(departement__slug=departement_choisi)
    #     departement_choisi = 'Develeppement Logiciel' if departement_choisi == 'develeppement-logiciel' else 'NTIC',
    # if licence_choisi and licence_choisi != "Toutes":
    #     emploi = emploi.filter(licence__slug=licence_choisi)

    # context = {
    #     'departement_choisi': departement_choisi,
    #     'licence_choisi': licence_choisi,
    #     'emplois': emploi,
    #     'licences': licence,
    #     'semestres': semestre,
    #     'departements': departement,
    # }
    # return render(request, 'Application/EmploiDuTemps.html', conte
    emploi = Emploi.objects.all().order_by('jour')
    licence = Licence.objects.all()
    departement = Departement.objects.all()
    semestre = Semestre.objects.all()
    jour = Jour.objects.all()
    heure = Heure.objects.all()
    context = {
        'licences': licence,
        'departements' : departement,
        'emplois' : emploi,
        'semestres' : semestre,
        'jours' : jour,
        'heures' : heure,
    }
    return render(request,'Application/EmploiDuTemps.html',context)


# Vue qui renvoie les notes d'un Etudiant
@login_required(login_url="login")
def Note(request):
    if not request.user.etudiant:
        return redirect('index')
    username = request.user.username
    licences = Licence.objects.all()

    # Utilisez un ensemble pour stocker les slugs uniques
    # unique_slugs = set()

    # # Filtrage des licences pour ne récupérer que les slugs uniques
    # unique_licences = []
    # for licence in licences:
    #     if licence.slug not in unique_slugs:
    #         unique_licences.append(licence)
    #         unique_slugs.add(licence.slug)

    
    semestres = Semestre.objects.all()
    notes = Notes.objects.filter(Etudiant__user__username=username)
    matieres = Matiere.objects.all()

    if request.method == "POST":
        licence_choisie = request.POST.get('licence')
        semestre_choisi = request.POST.get('semestre')
        
        # try:
        #     licence_choisie_converted = int(licence_choisie)
        #     if licence_choisie_converted and licence_choisie != "Toutes":
        #         notes = notes.filter(Etudiant__licence__numero=licence_choisie_converted)
        # except TypeError:
        #     pass
    

        if semestre_choisi and semestre_choisi != "Toutes":
            # matieres = Matiere.objects.filter(semestre__slug=semestre_choisi)
            notes = notes.filter(matiere__semestre__numero=int(semestre_choisi))

    context = {
        # "licences": unique_licences,
        "semestres": semestres,
        "notes": notes,
        "matieres": matieres,
    }
    return render(request, 'notes/notes.html', context)

@login_required(login_url="login")
def opportunite(request):
    type_stages = Type_opportunite.objects.all()
    opportunite = Opportunite.objects.all()

    choix = request.GET.get('type')

    if choix:
        opportunite = opportunite.filter(type_op__slug=choix)
    context = {
        'accueil': 'Trouver des oportunités de stage et d\'emploi avec nos structures partenaires',
        'opportunites': opportunite,
        'type_stages': type_stages,
    }
    return render(request, 'opportunite/opportunite.html', context)

@login_required(login_url='login')
def opportunite_detail(request,opportunite):
    Opporte = get_object_or_404(Opportunite,slug=opportunite)
    context = {
        'opportunite': Opporte,
    }
    return render(request,"opportunite/details_opportunite.html", context)



@login_required(login_url='login')
def postulation(request, opport_id):
    # Récupérez l'objet Etudiant et Opportunite correspondant aux identifiants fournis
    # opportunite = Opportunite.objects.get(pk=id_op)

    if request.method == 'POST':
        # Récupérez les données du formulaire
        
        opport = get_object_or_404(Opportunite,id=opport_id)
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        email = request.POST.get('email')
        motivation = request.POST.get('motivation')
        telephone = request.POST.get('telephone')
        adresse = request.POST.get('adresse')
        post_existant = Post.objects.filter(matricule=request.user.username, code_post=opport_id)
        if post_existant:
            messages.error(request,'Vous avez déja postuler à cette opportunité')
            return redirect('opportunite')
        # Créez une instance de Post et pré-remplissez les champs
        post = Post(
            nom=nom,
            prenom=prenom,
            email=email,
            matricule=request.user.username,
            opportunite=opport,
            partenaire=opport.partenaire.nom,
            motivation=motivation,
            adresse=adresse,
            code_post=opport_id,
            telephone=telephone)
        # Faites d'autres modifications au besoin avant de sauvegarder définitivement
        post.save()
        messages.success(request,f'Votre postulation chez {opport.partenaire.nom} a bien été enregistré')
        return redirect('opportunite')  # Redirection après le traitement
    else:
        # Affichage initial du formulaire avec les données pré-remplies
        # context = {'opportunite': opportunite}
        return render(request, 'opportunite/postulation.html')


@login_required
def deconnexion(request):
    logout(request)
    messages.warning(request,"Vous êtes deconnecté")
    return redirect('index')


##======================Vues Uniquement pour les professeurs=================

login_required(login_url='connexion')
def noter(request, matricule, matiere_slug):
    # Récupérer l'utilisateur connecté
   # utilisateur_connecte = request.user.username

     matiere = get_object_or_404(Matiere, slug=matiere_slug)

     if request.method == 'POST':
         etudiant_conserne = request.POST.get('username')
         print(f"======le matricule : {etudiant_conserne}")
         note1_str = request.POST.get('note1', '')
         note2_str = request.POST.get('note2', '')
         note3_str = request.POST.get('note3', '')
         etudiant = get_object_or_404(Etudiant,user__username=etudiant_conserne)

        # Valider les valeurs avant de les convertir en float
         try:
            note1 = float(note1_str)
         except ValueError:
            note1 = 0.0

         try:
            note2 = float(note2_str)
         except ValueError:
            note2 = 0.0

         try:
            note3 = float(note3_str)
         except ValueError:
            note3 = 0.0

        # Rechercher l'instance de Notes pour cet étudiant et cette matière
         instance, created = Notes.objects.get_or_create(Etudiant=etudiant, matiere=matiere)

        # Mettre à jour les notes de l'instance
         if note1 != 0.0:
            instance.note1 = note1
         if note2 != 0.0:
            instance.note2 = note2
         if note3 != 0.0:
            instance.note3 = note3
         instance.save()

        # Rediriger ou effectuer d'autres actions nécessaires
         return redirect('notation',matiere_slug)

    # Gérer le cas où la méthode de la requête n'est pas POST
    # ...
         notes = Notes.objects.all()
         context ={
             'notes':notes
         }

     return render(request, 'notation/notation.html')



    
    
    
    
    # les Vues des professeurs

@login_required(login_url="login")
def notation(request,matiere):
    if request.user.professeur:
        professeur = request.user
        matiere = get_object_or_404(Matiere,slug=matiere)
        if matiere:
            Etudiants = Etudiant.objects.filter(licence=matiere.semestre.licence)
            Etudiants = sorted(Etudiants,key=lambda x: x.user.first_name,reverse=False)
            note_etudiants = Notes.objects.select_related('Etudiant', 'matiere').filter(Etudiant__licence=matiere.semestre.licence)
            note_etudiants = note_etudiants.filter(matiere=matiere)

            # Vérifier si le formulaire a été soumis
            if request.method == 'POST' and 'classement_clicked' in request.POST:
                # Trier les étudiants par moyenne décroissante
                note_etudiants = sorted(note_etudiants, key=lambda x: x.moyenne(), reverse=True)

            context = {
                'matiere': matiere,
                'Etudiants': note_etudiants,
            }

            return render(request, 'notation/notation.html', context)
        else:
            return render(request, 'Application/error.html', {'error_message': 'Aucune matière trouvée.'})
    else:
        return redirect('index')
#====================SOUMISSIONS DES DOCUMENT PAR LES PROFESSEUR================
@login_required(login_url="login")
def brochure(request, matiere_slug):
    if request.user.professeur:
        professeur = request.user
        matiere = None

        try:
            matiere = get_object_or_404(Matiere, slug=matiere_slug)
            print(matiere.slug)
        except Matiere.DoesNotExist:
            return render(request, 'error.html', {'error_message': 'Matiere n\'existe pas pour cet utilisateur'})

        if request.method == "POST":
            titre = request.POST.get('titre')
            fichier = request.FILES.get('fichier')  # Utilisez request.FILES pour les téléchargements de fichiers

            # Assurez-vous que le fichier est valide avant de le sauvegarder
            if titre and fichier:
                # Créez une instance de Brochure et enregistrez-la
                document = Brochure(titre=titre, doc=fichier, matiere=matiere)
                document.save()

                return redirect('index')
            else:
                # Gérez le cas où les données du formulaire ne sont pas valides
                return render(request, 'error.html', {'error_message': 'Veuillez fournir un titre et un fichier valides'})

    else:
        return redirect('index')

    return render(request, 'archive/ajouter.html', {'matiere': matiere})

#====================CHOIX DE MATIÈRE DANS LAQUELLE UN PROFESSEUR VEUT FAIRE L'APPELLE================
@login_required(login_url="login")
def prof_choisi_matiere(request):
    matieres_enseigne = []  # Initialisation par défaut de la variable

    if hasattr(request.user, 'professeur') and request.user.professeur:
        
        professeur = request.user.professeur  # Accéder à l'objet Professeur lié
        matieres_enseigne = Matiere.objects.filter(professeur=professeur)
    if request.method == "POST":
        matiere = request.POST.get('matiere_choisie')
        if matiere:
            return redirect('presence',matiere)
    return render(request,'presence/choix_matiere.html', {'matieres_prof': matieres_enseigne})

#====================CHOIX DE MATIÈRE DANS LAQUELLE UN PROFESSEUR VEUT FAIRE LA NOTATION================
@login_required(login_url='connexion')
def prof_choisi_matiere_pour_noter(request):
    matieres_enseigne = []  # Initialisation par défaut de la variable

    if hasattr(request.user, 'professeur') and request.user.professeur:
        
        professeur = request.user.professeur  # Accéder à l'objet Professeur lié
        matieres_enseigne = Matiere.objects.filter(professeur=professeur)
        
    if request.method == "POST":
        matiere = request.POST.get('matiere_choisie')
        if matiere:
            return redirect('notation', matiere)
    
    return render(request, 'notation/choix_matiere.html', {'matieres_prof': matieres_enseigne})

#====================CHOIX DE MATIÈRE DANS LAQUELLE UN PROFESSEUR VEUT SOUMETTRE LES DOCUMENTATIONS================
def prof_choisi_matiere_pour_archiver(request):
    matieres_enseigne = []  # Initialisation par défaut de la variable

    if hasattr(request.user, 'professeur') and request.user.professeur:
        
        professeur = request.user.professeur  # Accéder à l'objet Professeur lié
        matieres_enseigne = Matiere.objects.filter(professeur=professeur)
    if request.method == "POST":
        matiere = request.POST.get('matiere_choisie')
        if matiere:
            return redirect('brochure',matiere)
    return render(request,'archive/choix_matiere.html', {'matieres_prof': matieres_enseigne})

@login_required(login_url="login")
def presence(request,matiere_slug):
    context = None
    if hasattr(request.user, 'professeur') and request.user.professeur:
        matiere = Matiere.objects.get(slug=matiere_slug)
        Etudiants = Etudiant.objects.filter(licence=matiere.semestre.licence)
        Etudiants = sorted(Etudiants,key=lambda x: x.user.first_name,reverse=True)
       
        context = {
                'matiere': matiere,
                'Etudiants': Etudiants,
            }            
    else:
        #si la personne qui essaie d'y acceder d'une tierse manière n'est pas un professeur, on la garde par force sur la page d'accueil
        return redirect('index')
    return render(request,'presence/presence.html',context)

def enregistrer_presence(request):
    #message_date_error=""
    msg_succes = ""
    msg_etudiants_exist ="La presence des Etudiants: \n"
    msg_etudiant_non_trouver=""
    rien_est_cocher = True
    if request.method == "POST":
        matiere_slug = request.POST.get('matiere_slug')
        etudiant_ids = request.POST.getlist('etudiant_ids[]') #Recupération d'une liste de names 
        presence_states = request.POST.getlist('presence_states[]')
        
        for presence_cocher in presence_states:
            if presence_cocher != "null":
                rien_est_cocher= False
                break
        
        date_du_jour = request.POST.get('date_jour')
        matiere = get_object_or_404(Matiere,slug=matiere_slug)
        # if not date_du_jour:
        #     message_date_error="Vous devez definir la date pour la présence"
        # else
        for etudiant_id, state in zip(etudiant_ids, presence_states):
            etudiant = get_object_or_404(Etudiant, user__username=etudiant_id)
            if not etudiant:
                msg_etudiant_non_trouver += "\n L'Etudiant avec le matricule " + etudiant_id + "n'est pas trouvé"
            if state == "null":
                continue
            # Vérifiez si une instance de Presence existe déjà pour cet étudiant, cette matière et cette date
            presence_instance, created = Presence.objects.get_or_create(
            etudiant=etudiant,
            matiere=matiere,
            date=date_du_jour,
            defaults={
                'present': (state == 'present'),
                'absent': (state == 'absent')
            }
                )
            
            # Si l'instance existe déjà, on met à jour les valeurs de présence
            if not created:
                presence_instance.present = (state == 'present')
                presence_instance.absent = (state == 'absent')
                presence_instance.save()
                
                msg_etudiants_exist +="**" + etudiant.user.username +  "\n"
        message_succes = "Présence Enregistrée avec succès pour la date " + date_du_jour
        
        if msg_etudiants_exist != "La presence des Etudiants <br>":
            msg_etudiants_exist += "A été mise à jour"
        else:
            msg_etudiants_exist = ""
        
        if  rien_est_cocher:
            message_succes = None
        
        messages.success(request,message_succes)
        messages.info(request,msg_etudiants_exist)
        # messages.add_message(request,'rien_est_cocher',rien_est_cocher)
        
        # context = {
        #     "msg_etudiants_exist":msg_etudiants_exist,
        #     "msg_etudiant_non_trouver":msg_etudiant_non_trouver,
        #     "matiere_slug":matiere_slug,
        #     "rien_est_cocher":rien_est_cocher,   
        # }
        return redirect(presence,matiere.slug)
        # return render(request, 'presence/presence.html', context)
    
#=======================================================================================      

@login_required(login_url="login")
def statistiques_presence(request, matiere):
    if request.method == "GET":
        if hasattr(request.user, 'professeur') and request.user.professeur:
            professeur = request.user
            mat = get_object_or_404(Matiere, slug=matiere)

            if mat:
                Etudiants = Etudiant.objects.filter(licence=mat.semestre.licence)
                Etudiants = sorted(Etudiants, key=lambda x: x.user.first_name, reverse=False)
                
                # Statistiques générales
                nb_presents = Presence.objects.filter(matiere__slug=matiere, present=True).count()
                nb_absents = Presence.objects.filter(matiere__slug=matiere, absent=True).count()
                nb_etudiants = Presence.objects.filter(matiere__slug=matiere).count()
                
                taux_present = round((nb_presents * 100) / (nb_etudiants if nb_etudiants else 1), 2)
                taux_absent = round((nb_absents * 100) / (nb_etudiants if nb_etudiants else 1), 2)
                
                # Statistiques par genre
                nb_filles = Presence.objects.filter(etudiant__genre=False).count()
                nb_garcons = Presence.objects.filter(etudiant__genre=True).count()
               
                
                nb_filles_presents = Presence.objects.filter(matiere__slug=matiere, present=True, etudiant__genre=False).count()
                nb_filles_absents = Presence.objects.filter(matiere__slug=matiere, absent=True, etudiant__genre=False).count()
                
                nb_garcons_presents = Presence.objects.filter(matiere__slug=matiere, present=True, etudiant__genre=True).count()
                nb_garcons_absents = Presence.objects.filter(matiere__slug=matiere, absent=True, etudiant__genre=True).count()
                
                taux_filles_presents = round((nb_filles_presents * 100) / (nb_filles if nb_filles else 1), 2)
                taux_filles_absents = round((nb_filles_absents * 100) / (nb_filles if nb_filles else 1), 2)
                
                taux_garcons_presents = round((nb_garcons_presents * 100) / (nb_garcons if nb_garcons else 1), 2)
                taux_garcons_absents = round((nb_garcons_absents * 100) / (nb_garcons if nb_garcons else 1), 2)
                
                print(f"taux_garçon:{taux_garcons_presents}")
                print(f"taux_garçon:{taux_garcons_absents}")
                print(f"taux_fille:{taux_filles_presents}")
                print(f"taux_fille:{taux_filles_absents}")
                context = {
                    'matiere': mat,
                    'Etudiants': Etudiants,
                    'taux_presents': taux_present,
                    'taux_absents': taux_absent,
                    'taux_filles_presents': taux_filles_presents,
                    'taux_filles_absents': taux_filles_absents,
                    'taux_garcons_presents': taux_garcons_presents,
                    'taux_garcons_absents': taux_garcons_absents,
                }
                return render(request, 'presence/statistique.html', context)
    
    if request.method == "POST":
        return redirect("presence", matiere)
    
    return render(request, 'presence/statistique.html', {'matiere': mat})


@login_required(login_url='connexion')
def statistique_etudiant(request, matricule, matiere):
    # Récupérer l'étudiant et la matière
    etudiant = get_object_or_404(Etudiant, user__username=matricule)
    mat = get_object_or_404(Matiere, slug=matiere)
    
    # Calcul des présences et absences
    total_presence = Presence.objects.filter(etudiant=etudiant, matiere=mat).count()
    presence_count = Presence.objects.filter(etudiant=etudiant, matiere=mat, present=True).count()
    absence_count = Presence.objects.filter(etudiant=etudiant, matiere=mat, absent=True).count()
    absences = Presence.objects.filter(etudiant=etudiant, matiere=mat, absent=True)
    
    # Calcul des taux de présence et d'absence
    taux_presence = round(presence_count * 100 / (total_presence if total_presence else 1), 2)
    taux_absence = round(absence_count * 100 / (total_presence if total_presence else 1), 2)
    
    # Récupérer les notes de l'étudiant pour la matière
    etudiant_notes = get_object_or_404(Notes, Etudiant=etudiant, matiere=mat)
    
    # Déterminer l'observation basée sur les notes
    # observation = "Aucune appréciation"
    # if etudiant_notes.note1 != 0.0 and etudiant_notes.moyenne() >= 1.8:
    #     observation = "Il commence plutôt Bien"
    # if etudiant_notes.note2 != 0.0 and etudiant_notes.moyenne() >= 3.6:
    #     observation = "Il évolue en bon élan"
    # if etudiant_notes.note3 != 0.0 and etudiant_notes.moyenne() >= 6:
    #     observation = "Un bon Etudiant"

    notes = [etudiant_notes.note1,etudiant_notes.note2,etudiant_notes.note3]  #les notes de l'Etudiant pour les présenter sur un graphique d'évolution
    
    # Préparer le contexte pour le template
    context = {
        "Etudiant": etudiant,
        "matiere": mat,
        "taux_presence": taux_presence,
        "taux_absence": taux_absence,
        "absences": absences,
        "notes": notes,
    }
    
    # Rendre le template avec le contexte
    return render(request, 'presence/statistiques_individuelle.html', context)



def temoignage(request):
    temoin = VideoTemoignage.objects.all()
    context = {'temoin': temoin}
    return render(request, 'Application/histoire&temoignage.html', context)
@login_required(login_url="login")
def update_profile(request):

        print("je suis rentré dans le update_profile")
        if request.method == "POST":
            user = request.user
            email = request.POST.get('email')
            telephone = request.POST.get('tel')
            photo_profile = request.FILES.get('photo')
            adresse = request.POST.get("adresse")
            print(photo_profile)
            try:
                etudiant = get_object_or_404(Etudiant,user=user) 
                print("j'ai recuperé l'etudiant")
                if email and email != user.email:
                    user.email = email
                print("j'ai enregistré l'email")
                if telephone and telephone != etudiant.tel:
                    etudiant.tel = telephone
                    print("j'ai enregistré le tel")
                if adresse and adresse != etudiant.adresse:
                    etudiant.adresse = adresse
                    print("j'ai enregistré l'adresse")
                if photo_profile:
                    try:
                        # Vérifiez si le fichier téléchargé est une image
                        img = Image.open(photo_profile)
                        img.verify()  # Vérifie si le fichier est une image valide
                        etudiant.photo_profile = photo_profile
                        print("j'ai enregistré l'image")
                    except:
                        messages.error(request, "Le fichier que vous avez soumis n'est pas une image.")
                        return redirect('index')
                etudiant.save()
                user.save()
                messages.success(request,"Profile mise à jour avec succès")
                return redirect('index')
            except:
                 messages.error(request,"Erreur de mise à jour du Profile")
                 return redirect('index')
        
        
    
    
    

    
def events(request):
    # Récupération des types d'événements
    type_event = TypeEvent.objects.all()
    events = Event.objects.all()
    type_list = {}
    
    for type in type_event:
        events_de_type = Event.objects.filter(type=type)  # Utilisez objects.filter() pour filtrer les événements par type
        type_list[type] = events_de_type
    
    for type, event in type_list.items():
        print(f"Type: {type}, Events: {event}")
        
    context = {
        "type_list": type_list,  
    }
    
    # Classement des événements par catégorie (à implémenter)
    
    return render(request, 'Application/evenement.html', context)




