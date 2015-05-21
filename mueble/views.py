from django.shortcuts import render, render_to_response
from mueble.models import Tipo_Mueble, Ocupacion,\
    Forma_Mueble, Mueble, Tamano, Tamano_Mueble, \
    Mueble_Ambiente
from mueble.forms import TipoMuebleForm, OcupacionForm,\
    FormaMuebleForm, MuebleForm, TamanoForm, \
    TamanoMuebleForm, MuebleAmbienteForm
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
import simplejson as json
import django.db
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
# lista
def lista_tipo_mueble(request):
    """docstring"""

    if request.method == "POST":
        if "item_id" in request.POST:
            try:
                id_tipomueble = request.POST['item_id']
                p = Tipo_Mueble.objects.get(pk=id_tipomueble)
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

    lista_tipomueble = Tipo_Mueble.objects.all()
    context = {'lista_tipomueble': lista_tipomueble}
    return render(request, 'mueble/tipomueble_lista.html', context)


def lista_ocupacion(request):
    """docstring"""

    if request.method == "POST":
        if "item_id" in request.POST:
            try:
                id_ocupacion = request.POST['item_id']
                p = Ocupacion.objects.get(pk=id_ocupacion)
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

    lista_ocupacion = Ocupacion.objects.all()
    context = {'lista_ocupacion': lista_ocupacion}
    return render(request, 'mueble/ocupacion_lista.html', context)


def lista_forma_mueble(request):
    """docstring"""

    if request.method == "POST":
        if "item_id" in request.POST:
            try:
                id_formamueble = request.POST['item_id']
                p = Forma_Mueble.objects.get(pk=id_formamueble)
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

    lista_formamueble = Forma_Mueble.objects.all()
    context = {'lista_formamueble': lista_formamueble}
    return render(request, 'mueble/formamueble_lista.html', context)


def lista_mueble(request):
    """docstring"""

    if request.method == "POST":
        if "item_id" in request.POST:
            try:
                id_mueble = request.POST['item_id']
                p = Mueble.objects.get(pk=id_mueble)
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

    lista_mueble = Mueble.objects.all()
    context = {'lista_mueble': lista_mueble}
    return render(request, 'mueble/mueble_lista.html', context)


def lista_tamano(request):
    """docstring"""

    if request.method == "POST":
        if "item_id" in request.POST:
            try:
                id_tamano = request.POST['item_id']
                p = Tamano.objects.get(pk=id_tamano)
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

    lista_tamano = Tamano.objects.all()
    context = {'lista_tamano': lista_tamano}
    return render(request, 'mueble/tamano_lista.html', context)


def buscar_tamano_mueble(request, idmueble=0):
    """docstring"""

    if request.method == "POST":
        if "item_id" in request.POST:
            try:
                id_tamanomueble = request.POST['item_id']
                p = Tamano_Mueble.objects.get(pk=id_tamanomueble)
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

    if idmueble != '0':
        try:
            buscar_tamanomueble = Tamano_Mueble.objects.get(mueble=idmueble)
            mensaje = ""
        except ObjectDoesNotExist as ex:
            buscar_tamanomueble = ""
            mensaje = "registro no existe"

        except Exception as ex:
            buscar_tamanomueble = ""
            mensaje = "se ha producido un error"+str(ex)

    else:
        buscar_tamanomueble = Tamano_Mueble.objects.all()
        mensaje = ""

    context = {'buscar_tamanomueble': buscar_tamanomueble, 'mensaje': mensaje}
    return render(request, 'mueble/tamanomueble_lista.html', context)


def buscar_mueble_ambiente(request, idambiente=0):
    """docstring"""

    if request.method == "POST":
        if "item_id" in request.POST:
            try:
                id_muebleambiente = request.POST['item_id']
                p = Mueble_Ambiente.objects.get(pk=id_muebleambiente)
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

    if idambiente != '0':
        try:
            buscar_muebleambiente = Mueble_Ambiente.objects.get(ambiente=idambiente)
            mensaje = ""
        except ObjectDoesNotExist as ex:
            buscar_muebleambiente = ""
            mensaje = "registro no existe"

        except Exception as ex:
            buscar_muebleambiente = ""
            mensaje = "se ha producido un error"+str(ex)

    else:
        buscar_muebleambiente = Mueble_Ambiente.objects.all()
        mensaje = ""
    context = {'buscar_muebleambiente': buscar_muebleambiente, 'mensaje': mensaje}
    return render(request, 'mueble/muebleambiente_lista.html', context)


# agregar nuevo
def add_tipo_mueble(request):
    """docstring"""
    if request.method == 'POST':
        form_tipomueble = TipoMuebleForm(request.POST)
        if form_tipomueble.is_valid():
            form_tipomueble.save()
            return HttpResponseRedirect(reverse('umuebles:lista_tipo_mueble'))
    else:
        form_tipomueble = TipoMuebleForm()
    return render_to_response('mueble/tipomueble_add.html',
                              {'form_tipomueble': form_tipomueble, 'create': True},
                              context_instance=RequestContext(request))


def add_ocupacion(request):
    """docstring"""
    if request.method == 'POST':
        form_ocupacion = OcupacionForm(request.POST)
        if form_ocupacion.is_valid():
            form_ocupacion.save()
            return HttpResponseRedirect(reverse('umuebles:lista_ocupacion'))
    else:
        form_ocupacion = OcupacionForm()
    return render_to_response('mueble/ocupacion_add.html',
                              {'form_ocupacion': form_ocupacion, 'create': True},
                              context_instance=RequestContext(request))


def add_formamueble(request):
    """docstring"""
    if request.method == 'POST':
        form_formamueble = FormaMuebleForm(request.POST)
        if form_formamueble.is_valid():
            form_formamueble.save()
            return HttpResponseRedirect(reverse('umuebles:lista_forma_mueble'))
    else:
        form_formamueble = FormaMuebleForm()
    return render_to_response('mueble/formamueble_add.html',
                              {'form_formamueble': form_formamueble, 'create': True},
                              context_instance=RequestContext(request))


def add_mueble(request):
    """docstring"""
    if request.method == 'POST':
        form_mueble = MuebleForm(request.POST)
        if form_mueble.is_valid():
            form_mueble.save()
            return HttpResponseRedirect(reverse('umuebles:lista_mueble'))
    else:
        form_mueble = MuebleForm()
    return render_to_response('mueble/mueble_add.html',
                              {'form_mueble': form_mueble, 'create': True},
                              context_instance=RequestContext(request))


def add_tamano(request):
    """docstring"""
    if request.method == 'POST':
        form_tamano = TamanoForm(request.POST)
        if form_tamano.is_valid():
            form_tamano.save()
            return HttpResponseRedirect(reverse('umuebles:lista_tamano'))
    else:
        form_tamano = TamanoForm()
    return render_to_response('mueble/tamano_add.html',
                              {'form_tamano': form_tamano, 'create': True},
                              context_instance=RequestContext(request))


def add_tamanomueble(request):
    """docstring"""
    if request.method == 'POST':
        form_tamanomueble = TamanoMuebleForm(request.POST)
        if form_tamanomueble.is_valid():
            form_tamanomueble.save()
            return HttpResponseRedirect(reverse('umuebles:buscar_tamano_mueble'))
    else:
        form_tamanomueble = TamanoMuebleForm()
    return render_to_response('mueble/tamanomueble_add.html',
                              {'form_tamanomueble': form_tamanomueble, 'create': True},
                              context_instance=RequestContext(request))


def add_muebleambiente(request):
    """docstring"""
    if request.method == 'POST':
        form_muebleambiente = MuebleAmbienteForm(request.POST)
        if form_muebleambiente.is_valid():
            form_muebleambiente.save()
            return HttpResponseRedirect(reverse('umuebles:lista_muebleambiente'))
    else:
        form_muebleambiente = MuebleAmbienteForm()
    return render_to_response('mueble/muebleambiente_add.html',
                              {'form_muebleambiente': form_muebleambiente, 'create': True},
                              context_instance=RequestContext(request))


# editar registro
def edit_tipo_mueble(request, pk):
    """docstring"""
    tipomueble = Tipo_Mueble.objects.get(pk=pk)

    if request.method == 'POST':
        # formulario enviado
        form_edit_tipomueble = TipoMuebleForm(request.POST, instance=tipomueble)

        if form_edit_tipomueble.is_valid():
            # formulario validado correctamente
            form_edit_tipomueble.save()

            return HttpResponseRedirect(reverse('umuebles:lista_tipo_mueble'))

    else:
        # formulario inicial
        form_edit_tipomueble = TipoMuebleForm(instance=tipomueble)

    return render_to_response('mueble/tipomueble_edit.html',
                              {'form_edit_tipomueble': form_edit_tipomueble, 'create': False},
                              context_instance=RequestContext(request))


def edit_ocupacion(request, pk):
    """docstring"""
    ocupacion = Ocupacion.objects.get(pk=pk)

    if request.method == 'POST':
        # formulario enviado
        form_edit_ocupacion = OcupacionForm(request.POST, instance=ocupacion)

        if form_edit_ocupacion.is_valid():
            # formulario validado correctamente
            form_edit_ocupacion.save()

            return HttpResponseRedirect(reverse('umuebles:lista_ocupacion'))

    else:
        # formulario inicial
        form_edit_ocupacion = OcupacionForm(instance=ocupacion)

    return render_to_response('mueble/ocupacion_edit.html',
                              {'form_edit_ocupacion': form_edit_ocupacion, 'create': False},
                              context_instance=RequestContext(request))


def edit_forma_mueble(request, pk):
    """docstring"""
    formamueble = Forma_Mueble.objects.get(pk=pk)

    if request.method == 'POST':
        # formulario enviado
        form_edit_formamueble = FormaMuebleForm(request.POST, instance=formamueble)

        if form_edit_formamueble.is_valid():
            # formulario validado correctamente
            form_edit_formamueble.save()

            return HttpResponseRedirect(reverse('umuebles:lista_forma_mueble'))

    else:
        # formulario inicial
        form_edit_formamueble = FormaMuebleForm(instance=formamueble)

    return render_to_response('mueble/formamueble_edit.html',
                              {'form_edit_formamueble': form_edit_formamueble, 'create': False},
                              context_instance=RequestContext(request))


def edit_mueble(request, pk):
    """docstring"""
    mueble = Mueble.objects.get(pk=pk)

    if request.method == 'POST':
        # formulario enviado
        form_edit_mueble = MuebleForm(request.POST, instance=mueble)

        if form_edit_mueble.is_valid():
            # formulario validado correctamente
            form_edit_mueble.save()

            return HttpResponseRedirect(reverse('umuebles:lista_mueble'))

    else:
        # formulario inicial
        form_edit_mueble = MuebleForm(instance=mueble)

    return render_to_response('mueble/mueble_edit.html',
                              {'form_edit_mueble': form_edit_mueble, 'create': False},
                              context_instance=RequestContext(request))


def edit_tamano(request, pk):
    """docstring"""
    tamano = Tamano(request, pk).objects.get(pk=pk)

    if request.method == 'POST':
        # formulario enviado
        form_edit_tamano = TamanoForm(request.POST, instance=tamano)

        if form_edit_tamano.is_valid():
            # formulario validado correctamente
            form_edit_tamano.save()

            return HttpResponseRedirect(reverse('umuebles:lista_tamano'))

    else:
        # formulario inicial
        form_edit_tamano = TamanoForm(instance=tamano)

    return render_to_response('mueble/tamano_edit.html',
                              {'form_edit_tamano': form_edit_tamano, 'create': False},
                              context_instance=RequestContext(request))


def edit_tamanomueble(request, pk):
    """docstring"""
    tamanomueble = Tamano_Mueble(request, pk).objects.get(pk=pk)

    if request.method == 'POST':
        # formulario enviado
        form_edit_tamanomueble = TamanoMuebleForm(request.POST, instance=tamanomueble)

        if form_edit_tamanomueble.is_valid():
            # formulario validado correctamente
            form_edit_tamanomueble.save()

            return HttpResponseRedirect(reverse('umuebles:lista_tamanomueble'))

    else:
        # formulario inicial
        form_edit_tamanomueble = TamanoMuebleForm(instance=tamanomueble)

    return render_to_response('mueble/tamanomueble_edit.html',
                              {'form_edit_tamanomueble': form_edit_tamanomueble, 'create': False},
                              context_instance=RequestContext(request))


def edit_muebleambiente(request, pk):
    """docstring"""
    muebleambiente = Mueble_Ambiente(request, pk).objects.get(pk=pk)

    if request.method == 'POST':
        # formulario enviado
        form_edit_muebleambiente = MuebleAmbienteForm(request.POST, instance=muebleambiente)

        if form_edit_muebleambiente.is_valid():
            # formulario validado correctamente
            form_edit_muebleambiente.save()

            return HttpResponseRedirect(reverse('umuebles:lista_muebleambiente'))

    else:
        # formulario inicial
        form_edit_muebleambiente = MuebleAmbienteForm(instance=muebleambiente)

    return render_to_response('mueble/muebleambiente_edit.html',
                              {'form_edit_muebleambiente': form_edit_muebleambiente, 'create': False},
                              context_instance=RequestContext(request))
