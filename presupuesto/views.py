from django.shortcuts import render
from django.views.generic import ListView, DetailView
from presupuesto.models import Presupuesto


# Create your views here.
class PresupuestoList(ListView):
    model = Presupuesto
    context_object_name = 'presupuesto'


class PresupuestoDetail(DetailView):

    model = Presupuesto

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(PresupuestoDetail, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['presupuesto_list'] = Presupuesto.objects.all()
        return context
