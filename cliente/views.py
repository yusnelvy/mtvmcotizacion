from django.shortcuts import render, render_to_response
from cliente.models import Cliente, Email, Sexo, Estado_civil
from telefono.models import Telefono
from direccion.models import Direccion
from cliente.forms import ClienteForm, EmailForm, SexoForm, EstadoCivilForm
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist
import simplejson as json
import django.db


# Create your views here.
# lista
def lista_sexo(request):
    """docstring"""
    if request.method == "POST":
        if "item_id" in request.POST:
            try:
                id_sexo = request.POST['item_id']
                p = Sexo.objects.get(pk=id_sexo)
                mensaje = {"status": "True", "item_id": p.id, "form": "del"}
                p.delete()

                 # Elinamos objeto de la base de datos
                return HttpResponse(json.dumps(mensaje), content_type='application/json')

            except django.db.IntegrityError:

                mensaje = {"status": "False", "form": "del", "msj": "No se puede eliminar porque \
                tiene algun registro asociado"}
                return HttpResponse(json.dumps(mensaje), content_type='application/json')

            except:
                mensaje = {"status": "False", "form": "del", "msj": " "}
                return HttpResponse(json.dumps(mensaje), content_type='application/json')

    lista_sexo = Sexo.objects.all()
    context = {'lista_sexo': lista_sexo}
    return render(request, 'cliente/sexo_lista.html', context)


def lista_estadocivil(request):
    """docstring"""
    if request.method == "POST":
        if "item_id" in request.POST:
            try:
                id_estadocivil = request.POST['item_id']
                p = Estado_civil.objects.get(pk=id_estadocivil)
                mensaje = {"status": "True", "item_id": p.id, "form": "del"}
                p.delete()

                 # Elinamos objeto de la base de datos
                return HttpResponse(json.dumps(mensaje), content_type='application/json')

            except django.db.IntegrityError:

                mensaje = {"status": "False", "form": "del", "msj": "No se puede eliminar porque \
                tiene algun registro asociado"}
                return HttpResponse(json.dumps(mensaje), content_type='application/json')

            except:
                mensaje = {"status": "False", "form": "del", "msj": " "}
                return HttpResponse(json.dumps(mensaje), content_type='application/json')

    lista_estadocivil = Estado_civil.objects.all()
    context = {'lista_estadocivil': lista_estadocivil}
    return render(request, 'cliente/estadocivil_lista.html', context)


def lista_cliente(request):
    """docstring"""
    if request.method == "POST":
        if "item_id" in request.POST:
            try:
                id_cliente = request.POST['item_id']
                p = Cliente.objects.get(pk=id_cliente)
                mensaje = {"status": "True", "item_id": p.id, "form": "del"}
                p.delete()

                 # Elinamos objeto de la base de datos
                return HttpResponse(json.dumps(mensaje), content_type='application/json')

            except django.db.IntegrityError:

                mensaje = {"status": "False", "form": "del", "msj": "No se puede eliminar porque \
                tiene algun registro asociado"}
                return HttpResponse(json.dumps(mensaje), content_type='application/json')

            except:
                mensaje = {"status": "False", "form": "del", "msj": " "}
                return HttpResponse(json.dumps(mensaje), content_type='application/json')

    lista_cliente = Cliente.objects.all()
    context = {'lista_cliente': lista_cliente}
    return render(request, 'cliente/cliente_lista.html', context)


def lista_email(request, id_cli):
    """docstring"""
    if request.method == "POST":
        if "item_id" in request.POST:
            try:
                id_email = request.POST['item_id']
                p = Email.objects.get(pk=id_email)
                mensaje = {"status": "True", "item_id": p.id, "form": "del"}
                p.delete()

                 # Elinamos objeto de la base de datos
                return HttpResponse(json.dumps(mensaje), content_type='application/json')

            except django.db.IntegrityError:

                mensaje = {"status": "False", "form": "del", "msj": "No se puede eliminar porque \
                tiene algun registro asociado"}
                return HttpResponse(json.dumps(mensaje), content_type='application/json')

            except:
                mensaje = {"status": "False", "form": "del", "msj": " "}
                return HttpResponse(json.dumps(mensaje), content_type='application/json')

    cliente = Cliente.objects.get(id=id_cli)

    lista_email = Email.objects.filter(cliente_id=cliente)
    context = {'lista_email': lista_email}
    return render(request, 'cliente/emailcliente_lista.html', context)


def lista_telefono_cliente(request, id_cli):
    """docstring"""
    if request.method == "POST":
        if "item_id" in request.POST:
            try:
                id_telefono = request.POST['item_id']
                p = Telefono.objects.get(pk=id_telefono)
                mensaje = {"status": "True", "item_id": p.id, "form": "del"}
                p.delete()

                 # Elinamos objeto de la base de datos
                return HttpResponse(json.dumps(mensaje), content_type='application/json')

            except django.db.IntegrityError:

                mensaje = {"status": "False", "form": "del", "msj": "No se puede eliminar porque \
                tiene algun registro asociado"}
                return HttpResponse(json.dumps(mensaje), content_type='application/json')

            except:
                mensaje = {"status": "False", "form": "del", "msj": " "}
                return HttpResponse(json.dumps(mensaje), content_type='application/json')

    cliente = Cliente.objects.get(id=id_cli)

    lista_telefono_cliente = Telefono.objects.select_related().filter(cliente=cliente)

    context = {'lista_telefono_cliente': lista_telefono_cliente}
    return render(request, 'cliente/telefonocliente_lista.html', context)


def lista_direccioncliente(request, id_cli):
    """docstring"""
    if request.method == "POST":
        if "item_id" in request.POST:
            try:
                id_direccion = request.POST['item_id']
                p = Direccion.objects.get(pk=id_direccion)
                mensaje = {"status": "True", "item_id": p.id, "form": "del"}
                p.delete()

                 # Elinamos objeto de la base de datos
                return HttpResponse(json.dumps(mensaje), content_type='application/json')

            except django.db.IntegrityError:

                mensaje = {"status": "False", "form": "del", "msj": "No se puede eliminar porque \
                tiene algun registro asociado"}
                return HttpResponse(json.dumps(mensaje), content_type='application/json')

            except:
                mensaje = {"status": "False", "form": "del", "msj": " "}
                return HttpResponse(json.dumps(mensaje), content_type='application/json')

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


def add_sexo(request):

    if request.method == 'POST':
        try:
            sexo_form = SexoForm(request.POST)

            if sexo_form.is_valid():
                sexo_form.save()

                return HttpResponseRedirect(reverse('uclientes:lista_sexo'))

        except Exception as ex:
            sexo_form = SexoForm()
            mensaje = "se ha producido un error"+str(ex)

    else:
        sexo_form = SexoForm()
        mensaje = ''

    return render_to_response('cliente/sexo_add.html',
                              {'sexo_form': sexo_form, 'create': True, 'mensaje': mensaje},
                              context_instance=RequestContext(request))


def add_estadocivil(request):

    if request.method == 'POST':
        try:
            estadocivil_form = EstadoCivilForm(request.POST)

            if estadocivil_form.is_valid():
                estadocivil_form.save()

                return HttpResponseRedirect(reverse('uclientes:lista_estadocivil'))

        except Exception as ex:
            estadocivil_form = EstadoCivilForm()
            mensaje = "se ha producido un error"+str(ex)

    else:
        estadocivil_form = EstadoCivilForm()
        mensaje = ''

    return render_to_response('cliente/estadocivil_add.html',
                              {'estadocivil_form': estadocivil_form, 'create': True, 'mensaje': mensaje},
                              context_instance=RequestContext(request))


def add_email(request):

    if request.method == 'POST':
        try:
            email_form = EmailForm(request.POST)
            if email_form.is_valid():
                id_reg = email_form.save()
                id_cli = Email.objects.get(id=id_reg.id)
                return HttpResponseRedirect(reverse('uclientes:ficha_cliente', args=(id_cli.cliente.id,)))
        except Exception as ex:
            mensaje = "se ha producido un error"+str(ex)
            email_form = EmailForm()

    else:
        email_form = EmailForm()
        mensaje = ''

    return render_to_response('cliente/Emailcliente_add.html',
                              {'email_form': email_form, 'create': True, 'mensaje': mensaje},
                              context_instance=RequestContext(request))


# editar un registro
def edit_cliente(request, pk):

    redirect_to = request.REQUEST.get('next', '')

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
            #return HttpResponseRedirect(reverse('uclientes:lista_cliente'))
        if redirect_to:
            return HttpResponseRedirect(redirect_to)
        else:
            return HttpResponseRedirect(reverse('uclientes:ficha_cliente', args=(id_clie.id,)))

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


def ficha_cliente(request, pk):

    lista_cliente = Cliente.objects.filter(pk=pk)
    lista_email = Email.objects.filter(cliente_id=pk)
    lista_telefono_cliente = Telefono.objects.filter(cliente=pk)
    direccioncliente_lista = Direccion.objects.filter(cliente=pk)

    context = {
        'lista_cliente': lista_cliente,
        'lista_email': lista_email,
        'lista_telefono_cliente': lista_telefono_cliente,
        'direccioncliente_lista': direccioncliente_lista
        }
    return render(request, 'cliente/cliente_ficha.html', context)
