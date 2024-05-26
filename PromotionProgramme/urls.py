"""PromotionProgramme URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from Application.views import *
from PromotionProgramme import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",index, name="index"),
    path("verifier",chercher_etudiant, name="verifier"),
    path("activation/<str:username>/",activation_compte, name="activation"),
    path("login",connexion,name="login"),
    path("logout",deconnexion,name="logout"),
    path("cours",cours,name="cours"),
    path("details_cours/<str:slug>/",programme_details,name="detail_cour"),
    path("notes", Note, name="notes"),
    path("choix_matiere_note/",prof_choisi_matiere_pour_noter, name="choix_matiere_noter"),
    path("choix_matiere_archive/",prof_choisi_matiere_pour_archiver, name="matiere_a_archiver"),
    path('brochure/<str:matiere_slug>/',brochure,name="brochure"),
    path('notation/<str:matiere>/',notation,name="notation"),
    path('noter/<str:matricule>/<str:matiere_slug>/',noter,name="noter"),
    path("choix_matiere/",prof_choisi_matiere, name="choix_matiere_presence"),
    path('presence/<str:matiere_slug>/',presence,name="presence"),
    path("enregistrer_presence/", enregistrer_presence, name="enregistrer_presence"),
    path('statistique_etudiant/<str:matricule>/<str:matiere>/',statistique_etudiant,name="statistique_etudiant"),


    path('statistiques/<str:matiere>/',statistiques_presence, name="statistiques"),


]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

