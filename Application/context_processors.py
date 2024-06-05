# app_name/context_processors.py
from .forms import EvalCoursForm

def eval_cours_form(request):
    form = EvalCoursForm()
    return {'eval_cours_form': form}
