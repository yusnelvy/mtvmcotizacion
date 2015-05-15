from django.shortcuts import render, render_to_response
from servicio.models import Servicio, Material, \
    Servicio_Material, Complejidad, Complejidad_Servicio
from servicio.forms import ServicioForm, MaterialForm,\
    ServicioMaterialForm, ComplejidadForm, ComplejidadServicioForm
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.core.urlresolvers import reverse
import django.db
import simplejson as json


# Create your views here.
# lista
def lista_servicio(request):
    """docstring"""

    if request.method == "POST":
        if "item_id" in request.POST:
            try:
                id_servicio = request.POST['item_id']
                p = Servicio.objects.get(pk=id_servicio)
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

    lista_servicio = Servicio.objects.all()
    context = {'lista_servicio': lista_servicio}
    return render(request, 'servicio/servicio_lista.html', context)


def lista_material(request):
    """docstring"""

    if request.method == "POST":
        if "item_id" in request.POST:
            try:
                id_material = request.POST['item_id']
                p = Material.objects.get(pk=id_material)
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

    lista_material = Material.objects.all()
    context = {'lista_material': lista_material}
    return render(request, 'servicio/material_lista.html', context)


def lista_complejidad(request):
    """docstring"""

    if request.method == "POST":
        if "item_id" in request.POST:
            try:
                id_complejidad = request.POST['item_id']
                p = Complejidad.objects.get(pk=id_complejidad)
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

    lista_complejidad = Complejidad.objects.all()
    context = {'lista_complejidad': lista_complejidad}
    return render(request, 'servicio/complejidad_lista .html', context)


# agregar nuevo
def add_servicio(request):
    """docstring"""
    if request.method == 'POST':
        form_servicio = ServicioForm(request.POST)
        if form_servicio.is_valid():
            form_servicio.save()
            return HttpResponseRedirect(reverse('uambientes:lista_servicio'))
    else:
        form_servicio = ServicioForm()
    return render_to_response('servicio/servicio_add.html',
                              {'form_servicio': form_servicio, 'create': True},
                              context_instance=RequestContext(request))
