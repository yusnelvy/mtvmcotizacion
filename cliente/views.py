from django.shortcuts import render, render_to_response
from cliente.models import Cliente, Email
from telefono.models import Telefono
from direccion.models import Direccion
from cliente.forms import ClienteForm, EmailForm
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext


# Create your views here.
# lista
def lista_cliente(request):
    """docstring"""
    lista_cliente = Cliente.objects.all()
    context = {'lista_cliente': lista_cliente}
    return render(request, 'cliente_lista.html', context)


def lista_email(request, id_cli):
    """docstring"""
    cliente = Cliente.objects.get(id=id_cli)

    lista_email = Email.objects.filter(cliente_id=cliente)
    context = {'lista_email': lista_email}
    return render(request, 'emailcliente_lista.html', context)


def lista_telefono_cliente(request, id_cli):
    """docstring"""
    cliente = Cliente.objects.get(id=id_cli)

    lista_telefono_cliente = Telefono.objects.select_related().filter(cliente=cliente)

    context = {'lista_telefono_cliente': lista_telefono_cliente}
    return render(request, 'telefonocliente_lista.html', context)


def lista_direccioncliente(request, id_cli):
    """docstring"""

    cliente = Cliente.objects.get(id=id_cli)

    direccioncliente_lista = Direccion.objects.filter(cliente=cliente)

    context = {'direccioncliente_lista': direccioncliente_lista}
    return render(request, 'direccioncliente_lista.html', context)


# agregar nuevo
def add_cliente(request):

    if request.method == 'POST':
        try:
            cliente_form = ClienteForm(request.POST)
            if cliente_form.is_valid():
                cliente_form.save()
                return HttpResponseRedirect(reverse('uclientes:lista_cliente'))

        except Exception, e:
            cliente_form = ClienteForm()
            mensaje = 'Ocurrio un error ' + e

    else:
        cliente_form = ClienteForm()
    return render_to_response('cliente_add.html',
                              {'cliente_form': cliente_form, 'create': True, 'mensaje': mensaje},
                              context_instance=RequestContext(request))
