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
from django.db.models import Q


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
    return render(request, 'servicio/complejidad_lista.html', context)


def buscar_servicio_material(request, idserv, idmat):
    """docstring"""

    if request.method == "POST":
        if "item_id" in request.POST:
            try:
                id_serviciomaterial = request.POST['item_id']
                p = Servicio_Material.objects.get(pk=id_serviciomaterial)
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

    if idmat | idserv:

        buscar_serviciomaterial = Servicio_Material.objects.get(Q(material=idmat) | Q(servicio=idserv))
    else:
        buscar_serviciomaterial = Servicio_Material.objects.all()

    context = {'buscar_serviciomaterial': buscar_serviciomaterial}
    return render(request, 'servicio/serviciomaterial_lista.html', context)


def buscar_complejidad_servicio(request, idserv, idcomp):
    """docstring"""

    if request.method == "POST":
        if "item_id" in request.POST:
            try:
                id_complejidadservicio = request.POST['item_id']
                p = Complejidad_Servicio.objects.get(pk=id_complejidadservicio)
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

    if idcomp | idserv:

        buscar_complejidadservicio = Complejidad_Servicio.objects.get(Q(complejidad=idcomp) | Q(servicio=idserv))
    else:
        buscar_complejidadservicio = Complejidad_Servicio.objects.all()

    context = {'buscar_complejidadservicio': buscar_complejidadservicio}
    return render(request, 'servicio/complejidadservicio_lista.html', context)


# agregar nuevo
def add_servicio(request):
    """docstring"""
    if request.method == 'POST':
        form_servicio = ServicioForm(request.POST)
        if form_servicio.is_valid():
            form_servicio.save()
            return HttpResponseRedirect(reverse('uservicios:lista_servicio'))
    else:
        form_servicio = ServicioForm()
    return render_to_response('servicio/servicio_add.html',
                              {'form_servicio': form_servicio, 'create': True},
                              context_instance=RequestContext(request))


def add_material(request):
    """docstring"""
    if request.method == 'POST':
        form_material = MaterialForm(request.POST)
        if form_material.is_valid():
            form_material.save()
            return HttpResponseRedirect(reverse('uservicios:lista_material'))
    else:
        form_material = MaterialForm()
    return render_to_response('servicio/material_add.html',
                              {'form_material': form_material, 'create': True},
                              context_instance=RequestContext(request))


def add_complejidad(request):
    """docstring"""
    if request.method == 'POST':
        form_complejidad = ComplejidadForm(request.POST)
        if form_complejidad.is_valid():
            form_complejidad.save()
            return HttpResponseRedirect(reverse('uservicios:lista_complejidad'))
    else:
        form_complejidad = ComplejidadForm()
    return render_to_response('servicio/complejidad_add.html',
                              {'form_complejidad': form_complejidad, 'create': True},
                              context_instance=RequestContext(request))


def add_serviciomaterial(request):
    """docstring"""
    if request.method == 'POST':
        form_serviciomaterial = ServicioMaterialForm(request.POST)
        if form_serviciomaterial.is_valid():
            form_serviciomaterial.save()
            return HttpResponseRedirect(reverse('uservicios:buscar_servicio_material'))
    else:
        form_serviciomaterial = ServicioMaterialForm()
    return render_to_response('servicio/serviciomaterial_add.html',
                              {'form_serviciomaterial': form_serviciomaterial, 'create': True},
                              context_instance=RequestContext(request))


def add_complejidadservicio(request):
    """docstring"""
    if request.method == 'POST':
        form_complejidadservicio = ComplejidadServicioForm(request.POST)
        if form_complejidadservicio.is_valid():
            form_complejidadservicio.save()
            return HttpResponseRedirect(reverse('uservicios:buscar_complejidad_servicio'))
    else:
        form_complejidadservicio = ComplejidadServicioForm()
    return render_to_response('servicio/complejidadservicio_add.html',
                              {'form_complejidadservicio': form_complejidadservicio, 'create': True},
                              context_instance=RequestContext(request))


# editar registro
def edit_servicio(request, pk):
    """docstring"""
    servicio = Servicio.objects.get(pk=pk)

    if request.method == 'POST':
        # formulario enviado
        form_edit_servicio = ServicioForm(request.POST, instance=servicio)

        if form_edit_servicio.is_valid():
            # formulario validado correctamente
            form_edit_servicio.save()

            return HttpResponseRedirect(reverse('uservicios:lista_servicio'))

    else:
        # formulario inicial
        form_edit_servicio = ServicioForm(instance=servicio)

    return render_to_response('servicio/servicio_edit.html',
                              {'form_edit_servicio': form_edit_servicio, 'create': False},
                              context_instance=RequestContext(request))


def edit_material(request, pk):
    """docstring"""
    material = Material.objects.get(pk=pk)

    if request.method == 'POST':
        # formulario enviado
        form_edit_material = MaterialForm(request.POST, instance=material)

        if form_edit_material.is_valid():
            # formulario validado correctamente
            form_edit_material.save()

            return HttpResponseRedirect(reverse('uservicios:lista_material'))

    else:
        # formulario inicial
        form_edit_material = MaterialForm(instance=material)

    return render_to_response('servicio/material_edit.html',
                              {'form_edit_material': form_edit_material, 'create': False},
                              context_instance=RequestContext(request))


def edit_complejidad(request, pk):
    """docstring"""
    complejidad = Complejidad.objects.get(pk=pk)

    if request.method == 'POST':
        # formulario enviado
        form_edit_complejidad = ComplejidadForm(request.POST, instance=complejidad)

        if form_edit_complejidad.is_valid():
            # formulario validado correctamente
            form_edit_complejidad.save()

            return HttpResponseRedirect(reverse('uservicios:lista_complejidad'))

    else:
        # formulario inicial
        form_edit_complejidad = ComplejidadForm(instance=complejidad)

    return render_to_response('servicio/complejidad_edit.html',
                              {'form_edit_complejidad': form_edit_complejidad, 'create': False},
                              context_instance=RequestContext(request))


def edit_complejidadservicio(request, pk):
    """docstring"""
    complejidadservicio = Complejidad_Servicio.objects.get(pk=pk)

    if request.method == 'POST':
        # formulario enviado
        form_edit_complejidadservicio = ComplejidadServicioForm(request.POST, instance=complejidadservicio)

        if form_edit_complejidadservicio.is_valid():
            # formulario validado correctamente
            form_edit_complejidadservicio.save()

            return HttpResponseRedirect(reverse('uservicios:buscar_complejidad_servicio'))

    else:
        # formulario inicial
        form_edit_complejidadservicio = ComplejidadServicioForm(instance=complejidadservicio)

    return render_to_response('servicio/complejidadservicio_edit.html',
                              {'form_edit_complejidadservicio': form_edit_complejidadservicio, 'create': False},
                              context_instance=RequestContext(request))


def edit_serviciomaterial(request, pk):
    """docstring"""
    serviciomaterial = Servicio_Material.objects.get(pk=pk)

    if request.method == 'POST':
        # formulario enviado
        form_edit_serviciomaterial = ServicioMaterialForm(request.POST, instance=serviciomaterial)

        if form_edit_serviciomaterial.is_valid():
            # formulario validado correctamente
            form_edit_serviciomaterial.save()

            return HttpResponseRedirect(reverse('uservicios:buscar_servicio_material'))

    else:
        # formulario inicial
        form_edit_serviciomaterial = ServicioMaterialForm(instance=serviciomaterial)

    return render_to_response('servicio/serviciomaterial_edit.html',
                              {'form_edit_serviciomaterial': form_edit_serviciomaterial, 'create': False},
                              context_instance=RequestContext(request))
