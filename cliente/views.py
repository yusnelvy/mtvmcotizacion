from django.shortcuts import render, render_to_response
from cliente.models import Cliente, Email
from telefono.models import Telefono
from direccion.models import Direccion
from cliente.forms import ClienteForm, EmailForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
# lista
def lista_cliente(request):
    """docstring"""
    lista_cliente = Cliente.objects.all()
    context = {'lista_cliente': lista_cliente}
    return render(request, 'cliente/cliente_lista.html', context)


def lista_email(request, id_cli):
    """docstring"""
    cliente = Cliente.objects.get(id=id_cli)

    lista_email = Email.objects.filter(cliente_id=cliente)
    context = {'lista_email': lista_email}
    return render(request, 'cliente/emailcliente_lista.html', context)


def lista_telefono_cliente(request, id_cli):
    """docstring"""
    cliente = Cliente.objects.get(id=id_cli)

    lista_telefono_cliente = Telefono.objects.select_related().filter(cliente=cliente)

    context = {'lista_telefono_cliente': lista_telefono_cliente}
    return render(request, 'cliente/telefonocliente_lista.html', context)


def lista_direccioncliente(request, id_cli):
    """docstring"""

    cliente = Cliente.objects.get(id=id_cli)

    direccioncliente_lista = Direccion.objects.filter(cliente=cliente)

    context = {'direccioncliente_lista': direccioncliente_lista}
    return render(request, 'cliente/direccioncliente_lista.html', context)


# agregar nuevo
def add_cliente(request):

    if request.method == 'POST':
        try:
            cliente_form = ClienteForm(request.POST)

            if cliente_form.is_valid():
                cliente_form.save()

                return HttpResponseRedirect(reverse('uclientes:lista_cliente'))

        except Exception as ex:
            cliente_form = ClienteForm()
            mensaje = "se ha producido un error"+str(ex)

    else:
        cliente_form = ClienteForm()
        mensaje = ''

    return render_to_response('cliente/cliente_add.html',
                              {'cliente_form': cliente_form, 'create': True, 'mensaje': mensaje},
                              context_instance=RequestContext(request))


def add_email(request):

    if request.method == 'POST':
        try:
            email_form = EmailForm(request.POST)
            if email_form.is_valid():
                email_form.save()
                return HttpResponseRedirect(reverse('uclientes:lista_cliente'))
        except Exception as ex:
            email_form = EmailForm()
            mensaje = "se ha producido un error"+str(ex)

    else:
        email_form = EmailForm()
        mensaje = ''

    return render_to_response('cliente/cliente_add.html',
                              {'email_form': email_form, 'create': True, 'mensaje': mensaje},
                              context_instance=RequestContext(request))


# editar un registro
def edit_cliente(request, pk):

    try:
        id_clie = Cliente.objects.get(pk=pk)
    except ObjectDoesNotExist as ex:
        mensaje = "El cliente no existe"
    except Exception as ex:
        mensaje = "se ha producido un error"+str(ex)

    if request.method == 'POST':
        # formulario enviado
        editar_clie = ClienteForm(request.POST, instance=id_clie)

        if editar_clie.is_valid():
            # formulario validado correctamente
            editar_clie.save()

            return HttpResponseRedirect(reverse('uclientes:lista_cliente'))

    else:
        # formulario inicial
        editar_clie = ClienteForm(instance=id_clie)
        mensaje = ""
    return render_to_response('cliente/cliente_edit.html',
                              {'editar_clie': editar_clie, 'id_cli': pk, 'create': False, 'mensaje': mensaje},
                              context_instance=RequestContext(request))


def edit_email(request, id_cli, pk):

    id_email = Email.objects.get(pk=pk)

    if request.method == 'POST':
        # formulario enviado
        form_edit_email = EmailForm(request.POST, instance=id_email)

        if form_edit_email.is_valid():
            # formulario validado correctamente
            form_edit_email.save()

            #return HttpResponseRedirect(reverse('uclientes:lista_email'))
            return HttpResponseRedirect('../../../')
    else:
        # formulario inicial
        form_edit_email = EmailForm(instance=id_email)

    return render_to_response('cliente/emailcliente_edit.html',
                              {'form_edit_email': form_edit_email, 'create': False},
                              context_instance=RequestContext(request))
