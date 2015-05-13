from django.shortcuts import render
from cliente.models import Cliente


# Create your views here.
def lista_cliente(request):
    list_clie = Cliente.objects.all()
    context = {'list_clie': list_clie}
    return render(request, 'cliente_lista.html', context)
