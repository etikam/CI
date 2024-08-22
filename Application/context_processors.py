# app_name/context_processors.py
from .forms import EvalCoursForm
from .models import Matiere

# this view's return is extends over all pages (so it is accessible anywhere)
def eval_cours_form(request):
    context = {}
    form = EvalCoursForm()

    if request.user.is_authenticated and hasattr(request.user, 'etudiant'):
        etudiant = request.user.etudiant
        cours = Matiere.objects.filter(semestre__licence=etudiant.licence)
        context['matiere_eval'] = cours
        # Passez les matières filtrées au formulaire
        form = EvalCoursForm(matiere_choices=cours)
        print(f'le matières que l\'Etudiant peut noter {cours} ')
    context['eval_cours_form'] = form
    return context