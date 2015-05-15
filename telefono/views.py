from django.shortcuts import render, render_to_response
from telefono.models import Tipo_telefono, Telefono
from telefono.forms import TipoTelefonoForm, TelefonoForm
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.core.urlresolvers import reverse
import django.db
import simplejson as json


# Create your views here.
# lista
def lista_tipotelefono(request):
    """docstring"""

    if request.method == "POST":
        if "item_id" in request.POST:
            try:
                id_tipotelefono = request.POST['item_id']
                p = Tipo_telefono.objects.get(pk=id_tipotelefono)
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

    obj_list = Tipo_telefono.objects.all()
    context = {'obj_list': obj_list}
    return render(request, 'telefono/tipotelefono_lista.html', context)


def lista_telefono(request):
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

    telefono = Telefono.objects.all()
    context = {'telefono': telefono}
    return render(request, 'telefono/telefono_lista.html', context)


# agregar nuevo
def add_tipotelefono(request):
    """docstring"""

    if request.method == 'POST':
        form_tipotelefono = TipoTelefonoForm(request.POST)
        if form_tipotelefono.is_valid():
            form_tipotelefono.save()
            return HttpResponseRedirect(reverse('utelefonos:lista_tipotelefono'))

    else:
        form_tipotelefono = TipoTelefonoForm()
    return render_to_response('telefono/tipotelefono_add.html',
                              {'form_tipotelefono': form_tipotelefono, 'create': True},
                              context_instance=RequestContext(request))


def add_telefono(request):
    """docstring"""

    if request.method == 'POST':
        form_telefono = TelefonoForm(request.POST)
        if form_telefono.is_valid():
            form_telefono.save()
            return HttpResponseRedirect(reverse('utelefonos:lista_telefono'))
    else:
        form_telefono = TelefonoForm()
    return render_to_response('telefono/telefono_add.html',
                              {'form_telefono': form_telefono, 'create': True},
                              context_instance=RequestContext(request))


# editar
def edit_tipotelefono(request, pk):
    """docstring"""

    id_tipo = Tipo_telefono.objects.get(pk=pk)

    if request.method == 'POST':
        # formulario enviado
        form_edit_tipotelefono = TipoTelefonoForm(request.POST, instance=id_tipo)

        if form_edit_tipotelefono.is_valid():
            # formulario validado correctamente
            form_edit_tipotelefono.save()

            return HttpResponseRedirect(reverse('utelefonos:lista_tipotelefono'))
    else:
        # formulario inicial
        form_edit_tipotelefono = TipoTelefonoForm(instance=id_tipo)

    return render_to_response('telefono/tipotelefono_edit.html',
                              {'form_edit_tipotelefono': form_edit_tipotelefono, 'create': False},
                              context_instance=RequestContext(request))


def edit_telefono(request, pk):
    """docstring"""

    id_telefono = Telefono.objects.get(pk=pk)

    if request.method == 'POST':
        # formulario enviado
        form_edit_telefono = TelefonoForm(request.POST, instance=id_telefono)

        if form_edit_telefono.is_valid():
            # formulario validado correctamente
            form_edit_telefono.save()

            return HttpResponseRedirect(reverse('utelefonos:lista_telefono'))
    else:
        # formulario inicial
        form_edit_telefono = TelefonoForm(instance=id_telefono)

    return render_to_response('telefono/telefono_edit.html',
                              {'form_edit_telefono': form_edit_telefono, 'create': False},
                              context_instance=RequestContext(request))
