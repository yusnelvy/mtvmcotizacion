from django.shortcuts import render
from premisas.models import Empresa
from django.views.generic import DetailView


# Create your views here.
class EmpresaDetail(DetailView):

    model = Empresa
    context_object_name = "empresa"
    template_name = 'empresa_ficha.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(EmpresaDetail, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        return context
