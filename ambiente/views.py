from django.shortcuts import render, render_to_response
from ambiente.models import Tipo_ambiente, Ambiente,\
    Ambiente_Tipo_inmueble
from ambiente.forms import TipoAmbienteForm, AmbienteForm,\
    AmbienteTipoInmuebleForm
from direccion.models import Tipo_Inmueble
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
import simplejson as json
import django.db


# Create your views here.
# lista
def lista_tipo_ambiente(request):
    """docstring"""

    if request.method == "POST":
        if "item_id" in request.POST:
            try:
                id_tipoambiente = request.POST['item_id']
                p = Tipo_ambiente.objects.get(pk=id_tipoambiente)
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

    lista_tipoambiente = Tipo_ambiente.objects.all()
    context = {'lista_tipoambiente': lista_tipoambiente}
    return render(request, 'tipoambiente_lista.html', context)


def lista_ambiente(request):
    """docstring"""
    if request.method == "POST":
        if "item_id" in request.POST:
            try:
                id_ambiente = request.POST['item_id']
                p = Ambiente.objects.get(pk=id_ambiente)
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

    lista_ambiente = Ambiente.objects.all()
    context = {'lista_ambiente': lista_ambiente}
    return render(request, 'ambiente_lista.html', context)


def lista_ambiente_tipo_inmueble(request):
    """docstring"""
    if request.method == "POST":
        if "item_id" in request.POST:
            try:
                id_ambtipoinmueble = request.POST['item_id']
                p = Ambiente_Tipo_inmueble.objects.get(pk=id_ambtipoinmueble)
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

    lista_ambtipoinmueble = Ambiente_Tipo_inmueble.objects.all()
    context = {'lista_ambtipoinmueble': lista_ambtipoinmueble}
    return render(request, 'ambiente_lista.html', context)


def buscar_ambiente(request, id_tipoinmueble):
    """docstring"""
    tipo_inmueble = Tipo_Inmueble.objects.get(id=id_tipoinmueble)

    lista_ambiente = Ambiente.objects.filter(tipo_inmueble_id=tipo_inmueble)
    context = {'lista_ambiente': lista_ambiente}
    return render(request, 'ambiente_lista.html', context)


# agregar nuevo
def add_tipo_ambiente(request):
    """docstring"""
    if request.method == 'POST':
        form_tipoambiente = TipoAmbienteForm(request.POST)
        if form_tipoambiente.is_valid():
            form_tipoambiente.save()
            return HttpResponseRedirect(reverse('uambientes:lista_tipo_ambiente'))
    else:
        form_tipoambiente = TipoAmbienteForm()
    return render_to_response('ambiente/tipoambiente_add.html',
                              {'form_tipoambiente': form_tipoambiente, 'create': True},
                              context_instance=RequestContext(request))


def add_ambiente(request):
    """docstring"""
    if request.method == 'POST':
        form_ambiente = AmbienteForm(request.POST)
        if form_ambiente.is_valid():
            form_ambiente.save()
            return HttpResponseRedirect(reverse('uambientes:lista_ambiente'))
    else:
        form_ambiente = AmbienteForm()
    return render_to_response('ambiente/ambiente_add.html',
                              {'form_ambiente': form_ambiente, 'create': True},
                              context_instance=RequestContext(request))


def add_ambiente_tipoinmueble(request):
    """docstring"""
    if request.method == 'POST':
        form_ambtipoinmueble = AmbienteTipoInmuebleForm(request.POST)
        if form_ambtipoinmueble.is_valid():
            form_ambtipoinmueble.save()
            return HttpResponseRedirect(reverse('uambientes:lista_ambiente'))
    else:
        form_ambtipoinmueble = AmbienteTipoInmuebleForm()
    return render_to_response('ambiente/ambientetipoinmueble_add.html',
                              {'form_ambtipoinmueble': form_ambtipoinmueble, 'create': True},
                              context_instance=RequestContext(request))


# editar un registro
def edit_tipo_ambiente(request, pk):
    """docstring"""
    tipoambiente = Tipo_ambiente.objects.get(pk=pk)

    if request.method == 'POST':
        # formulario enviado
        form_edit_tipoambiente = TipoAmbienteForm(request.POST, instance=tipoambiente)

        if form_edit_tipoambiente.is_valid():
            # formulario validado correctamente
            form_edit_tipoambiente.save()

            return HttpResponseRedirect(reverse('udireciones:lista_tipoambiente'))

    else:
        # formulario inicial
        form_edit_tipoambiente = TipoAmbienteForm(instance=tipoambiente)

    return render_to_response('ambiente/tipoambiente_edit.html',
                              {'form_edit_tipoambiente': form_edit_tipoambiente, 'create': False},
                              context_instance=RequestContext(request))


def edit_ambiente(request, id_tipoinmueble, pk):
    """docstring"""

    id_ambi = Ambiente_Tipo_inmueble.objects.values('ambiente').filter(pk=pk)

    id_ambiente = Ambiente.objects.get(pk=id_ambi)

    if request.method == 'POST':
        # formulario enviado
        form_edit_ambiente = AmbienteForm(request.POST, instance=id_ambiente)

        if form_edit_ambiente.is_valid():
            # formulario validado correctamente
            form_edit_ambiente.save()

            #return HttpResponseRedirect(reverse('uclientes:lista_email'))
            return HttpResponseRedirect('../../../')
    else:
        # formulario inicial
        form_edit_ambiente = AmbienteForm(instance=id_ambiente)

    return render_to_response('ambiente_edit.html',
                              {'form_edit_ambiente': form_edit_ambiente, 'create': False},
                              context_instance=RequestContext(request))


def edit_ambiente_tipoinmueble(request, pk):
    """docstring"""
    ambtipoinmueble = Ambiente_Tipo_inmueble.objects.get(pk=pk)

    if request.method == 'POST':
        # formulario enviado
        form_edit_ambtipoinmueble = AmbienteTipoInmuebleForm(request.POST, instance=ambtipoinmueble)

        if form_edit_ambtipoinmueble.is_valid():
            # formulario validado correctamente
            form_edit_ambtipoinmueble.save()

            return HttpResponseRedirect(reverse('udireciones:lista_ambtipoinmueble'))

    else:
        # formulario inicial
        form_edit_ambtipoinmueble = AmbienteTipoInmuebleForm(instance=ambtipoinmueble)

    return render_to_response('ambiente/ambientetipoinmueble_edit.html',
                              {'form_edit_ambtipoinmueble': form_edit_ambtipoinmueble, 'create': False},
                              context_instance=RequestContext(request))
