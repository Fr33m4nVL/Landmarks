from django.views.generic import ListView

from .models import Excursion

class ExcursionList(ListView):
    model = Excursion
    template_name = 'excursions.html'