from django.shortcuts import render, render_to_response
from direccion.models import Pais, Provincia, Ciudad, \
    Zona, Tipo_direccion, Direccion, Tipo_Inmueble, \
    Complejidad_Inmueble, Inmueble
from direccion.forms import PaisForm, ProvinciaForm, \
    CiudadForm, ZonaForm, TipoDireccionForm, \
    DireccionForm, TipoInmuebleForm, \
    ComplejidadInmuebleForm, InmuebleForm
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
import simplejson as json
import django.db


# Create your views here.
# lista
def lista_pais(request):
    """docstring"""

    if request.method == "POST":
        if "item_id" in request.POST:
            try:
                id_pais = request.POST['item_id']
                p = Pais.objects.get(pk=id_pais)
                mensaje = {"status": "True", "item_id": p.id, "form": "del"}
                p.delete()

                 # Elinamos objeto de la base de datos
                return HttpResponse(json.dumps(mensaje), content_type='application/json')

            except django.db.IntegrityError:

                mensaje = {"status": "False", "form": "del", "msj": "No se puede eliminar porque \
                tiene algun registro asociado"}
                return HttpResponse(json.dumps(mensaje), content_type='application/json')

            except django.db.DatabaseError:

                mensaje = {"status": "False", "form": "del", "msj": "Error de BD"}
                return HttpResponse(json.dumps(mensaje), content_type='application/json')

            except:
                mensaje = {"status": "False", "form": "del", "msj": " "}
                return HttpResponse(json.dumps(mensaje), content_type='application/json')

    lista_pais = Pais.objects.all()
    context = {'lista_pais': lista_pais}
    return render(request, 'direccion/pais_lista.html', context)


def lista_provincia(request):
    """docstring"""

    if request.method == "POST":
        if "item_id" in request.POST:
            try:
                id_provincia = request.POST['item_id']
                p = Provincia.objects.get(pk=id_provincia)
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

    lista_provincia = Provincia.objects.all()
    context = {'lista_provincia': lista_provincia}
    return render(request, 'direccion/provincia_lista.html', context)


def lista_ciudad(request):
    """docstring"""

    if request.method == "POST":
        if "item_id" in request.POST:
            try:
                id_ciudad = request.POST['item_id']
                p = Ciudad.objects.get(pk=id_ciudad)
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

    lista_ciudad = Ciudad.objects.all()
    context = {'lista_ciudad': lista_ciudad}
    return render(request, 'direccion/ciudad_lista.html', context)


def lista_zona(request):
    """docstring"""

    if request.method == "POST":
        if "item_id" in request.POST:
            try:
                id_zona = request.POST['item_id']
                p = Zona.objects.get(pk=id_zona)
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

    lista_zona = Zona.objects.all()
    context = {'lista_zona': lista_zona}
    return render(request, 'direccion/zona_lista.html', context)


def lista_tipo_direccion(request):
    """docstring"""

    if request.method == "POST":
        if "item_id" in request.POST:
            try:
                id_tipodireccion = request.POST['item_id']
                p = Tipo_direccion.objects.get(pk=id_tipodireccion)
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

    lista_tipodireccion = Tipo_direccion.objects.all()
    context = {'lista_tipodireccion': lista_tipodireccion}
    return render(request, 'direccion/tipodireccion_lista.html', context)


def lista_direccion(request):
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

    lista_direccion = Direccion.objects.all()
    context = {'lista_direccion': lista_direccion}
    return render(request, 'direccion/direccion_lista.html', context)


def lista_tipo_inmueble(request):
    """docstring"""

    if request.method == "POST":
        if "item_id" in request.POST:
            try:
                id_tipoinmueble = request.POST['item_id']
                p = Tipo_Inmueble.objects.get(pk=id_tipoinmueble)
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

    lista_tipo_inmueble = Tipo_Inmueble.objects.all()
    context = {'lista_tipo_inmueble': lista_tipo_inmueble}
    return render(request, 'direccion/tipo_inmueble_lista.html', context)


def lista_complejidad_inmueble(request):
    """docstring"""

    if request.method == "POST":
        if "item_id" in request.POST:
            try:
                complejidad = request.POST['item_id']
                p = Complejidad_Inmueble.objects.get(pk=complejidad)
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

    lista_complejidad_inmueble = Complejidad_Inmueble.objects.all()
    context = {'lista_complejidad_inmueble': lista_complejidad_inmueble}
    return render(request, 'direccion/complejidad_inmueble_lista.html', context)


def lista_inmueble(request):
    """docstring"""

    if request.method == "POST":
        if "item_id" in request.POST:
            try:
                inmueble = request.POST['item_id']
                p = Inmueble.objects.get(pk=inmueble)
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

    lista_inmueble = Inmueble.objects.all()
    context = {'lista_inmueble': lista_inmueble}
    return render(request, 'direccion/inmueble_lista.html', context)


# agregar nuevo
def add_pais(request):
    """docstring"""
    if request.method == 'POST':
        form_pais = PaisForm(request.POST)
        if form_pais.is_valid():
            form_pais.save()
            return HttpResponseRedirect(reverse('udireciones:lista_pais'))
    else:
        form_pais = PaisForm()
    return render_to_response('direccion/pais_add.html',
                              {'form_pais': form_pais, 'create': True},
                              context_instance=RequestContext(request))


def add_provincia(request):
    """docstring"""
    if request.method == 'POST':
        form_provincia = ProvinciaForm(request.POST)
        if form_provincia.is_valid():
            form_provincia.save()
            return HttpResponseRedirect(reverse('udireciones:lista_provincia'))
    else:
        form_provincia = ProvinciaForm()
    return render_to_response('direccion/provincia_add.html',
                              {'form_provincia': form_provincia, 'create': True},
                              context_instance=RequestContext(request))


def add_ciudad(request):
    """docstring"""
    if request.method == 'POST':
        form_ciudad = CiudadForm(request.POST)
        if form_ciudad.is_valid():
            form_ciudad.save()
            return HttpResponseRedirect(reverse('udireciones:lista_ciudad'))
    else:
        form_ciudad = CiudadForm()
    return render_to_response('direccion/ciudad_add.html',
                              {'form_ciudad': form_ciudad, 'create': True},
                              context_instance=RequestContext(request))


def add_zona(request):
    """docstring"""
    if request.method == 'POST':
        form_zona = ZonaForm(request.POST, request.FILES)
        if form_zona.is_valid():
            form_zona.save()
            return HttpResponseRedirect(reverse('udireciones:lista_zona'))
    else:
        form_zona = ZonaForm()
    return render_to_response('direccion/zona_add.html',
                              {'form_zona': form_zona, 'create': True},
                              context_instance=RequestContext(request))


def add_tipo_direccion(request):
    """docstring"""
    if request.method == 'POST':
        form_tipodireccion = TipoDireccionForm(request.POST)
        if form_tipodireccion.is_valid():
            form_tipodireccion.save()
            return HttpResponseRedirect(reverse('udireciones:lista_tipo_direccion'))
    else:
        form_tipodireccion = TipoDireccionForm()

    return render_to_response('direccion/tipodireccion_add.html',
                              {'form_tipodireccion': form_tipodireccion, 'create': True},
                              context_instance=RequestContext(request))


def add_direccion(request):
    """docstring"""
    if request.method == 'POST':
        form_direccion = DireccionForm(request.POST)
        if form_direccion.is_valid():
            form_direccion.save()
            return HttpResponseRedirect(reverse('udireciones:lista_direccion'))
    else:
        form_direccion = DireccionForm()
    return render_to_response('direccion/direccion_add.html',
                              {'form_direccion':form_direccion, 'create': True},
                              context_instance=RequestContext(request))


def add_tipo_inmueble(request):
    """docstring"""
    if request.method == 'POST':
        form_tipo_inmueble = TipoInmuebleForm(request.POST)
        if form_tipo_inmueble.is_valid():
            form_tipo_inmueble.save()
            return HttpResponseRedirect(reverse('udireciones:lista_tipo_inmueble'))
    else:
        form_tipo_inmueble = TipoInmuebleForm()

    return render_to_response('direccion/tipo_inmueble_add.html',
                              {'form_tipo_inmueble': form_tipo_inmueble, 'create': True},
                              context_instance=RequestContext(request))


def add_complejidad_inmueble(request):
    """docstring"""
    if request.method == 'POST':
        form_complejidad = ComplejidadInmuebleForm(request.POST)
        if form_complejidad.is_valid():
            form_complejidad.save()
            return HttpResponseRedirect(reverse('udireciones:lista_complejidad_inmueble'))
    else:
        form_complejidad = ComplejidadInmuebleForm()

    return render_to_response('direccion/complejidad_inmueble_add.html',
                              {'form_complejidad': form_complejidad, 'create': True},
                              context_instance=RequestContext(request))


def add_inmueble(request):
    """docstring"""
    if request.method == 'POST':
        form_inmueble = InmuebleForm(request.POST)
        if form_inmueble.is_valid():
            form_inmueble.save()
            return HttpResponseRedirect(reverse('udireciones:lista_inmueble'))
    else:
        form_inmueble = InmuebleForm()

    return render_to_response('direccion/inmueble_add.html',
                              {'form_inmueble': form_inmueble, 'create': True},
                              context_instance=RequestContext(request))


# editar registro
def edit_pais(request, pk):
    """docstring"""
    pais = Pais.objects.get(pk=pk)

    if request.method == 'POST':
        # formulario enviado
        form_edit_pais = PaisForm(request.POST, instance=pais)

        if form_edit_pais.is_valid():
            # formulario validado correctamente
            form_edit_pais.save()

            return HttpResponseRedirect(reverse('udireciones:lista_pais'))

    else:
        # formulario inicial
        form_edit_pais = PaisForm(instance=pais)

    return render_to_response('direccion/pais_edit.html',
                              {'form_edit_pais': form_edit_pais, 'create': False},
                              context_instance=RequestContext(request))


def edit_provincia(request, pk):
    """docstring"""
    provincia = Provincia.objects.get(pk=pk)

    if request.method == 'POST':
        # formulario enviado
        form_edit_provincia = ProvinciaForm(request.POST, instance=provincia)

        if form_edit_provincia.is_valid():
            # formulario validado correctamente
            form_edit_provincia.save()

            return HttpResponseRedirect(reverse('udireciones:lista_provincia'))

    else:
        # formulario inicial
        form_edit_provincia = ProvinciaForm(instance=provincia)

    return render_to_response('direccion/provincia_edit.html',
                              {'form_edit_provincia': form_edit_provincia, 'create': False},
                              context_instance=RequestContext(request))


def edit_ciudad(request, pk):
    """docstring"""
    ciudad = Ciudad.objects.get(pk=pk)

    if request.method == 'POST':
        # formulario enviado
        form_edit_ciudad = CiudadForm(request.POST, instance=ciudad)

        if form_edit_ciudad.is_valid():
            # formulario validado correctamente
            form_edit_ciudad.save()

            return HttpResponseRedirect(reverse('udireciones:lista_ciudad'))

    else:
        # formulario inicial
        form_edit_ciudad = CiudadForm(instance=ciudad)

    return render_to_response('direccion/ciudad_edit.html',
                              {'form_edit_ciudad': form_edit_ciudad, 'create': False},
                              context_instance=RequestContext(request))


def edit_zona(request, pk):
    """docstring"""
    zona = Zona.objects.get(pk=pk)

    if request.method == 'POST':
        # formulario enviado
        form_edit_zona = ZonaForm(request.POST, instance=zona)

        if form_edit_zona.is_valid():
            # formulario validado correctamente
            form_edit_zona.save()

            return HttpResponseRedirect(reverse('udireciones:lista_zona'))

    else:
        # formulario inicial
        form_edit_zona = ZonaForm(instance=zona)

    return render_to_response('direccion/zona_edit.html',
                              {'form_edit_zona': form_edit_zona, 'create': False},
                              context_instance=RequestContext(request))


def edit_tipo_direccion(request, pk):
    """docstring"""
    tipodireccion = Tipo_direccion.objects.get(pk=pk)

    if request.method == 'POST':
        # formform_tipodireccionulario enviado
        form_edit_tipodireccion = TipoDireccionForm(request.POST, instance=tipodireccion)

        if form_edit_tipodireccion.is_valid():
            # formulario validado correctamente
            form_edit_tipodireccion.save()

            #return HttpResponseRedirect('udireciones:lista_tipo_direccion')

            return HttpResponseRedirect(reverse('udireciones:lista_tipo_direccion'))

    else:
        # formulario inicial
        form_edit_tipodireccion = TipoDireccionForm(instance=tipodireccion)

    return render_to_response('direccion/tipodireccion_edit.html',
                              {'form_edit_tipodireccion': form_edit_tipodireccion, 'create': False},
                              context_instance=RequestContext(request))


def edit_direccion(request, pk):
    """docstring"""
    direccion = Direccion.objects.get(pk=pk)

    if request.method == 'POST':
        # formform_direccionulario enviado
        form_edit_direccion = DireccionForm(request.POST, instance=direccion)

        if form_edit_direccion.is_valid():
            # formulario validado correctamente
            form_edit_direccion.save()

            return HttpResponseRedirect(reverse('udireciones:lista_direccion'))

    else:
        # formulario inicial
        form_edit_direccion = DireccionForm(instance=direccion)

    return render_to_response('direccion/direccion_edit.html',
                              {'form_edit_direccion': form_edit_direccion, 'create': False},
                              context_instance=RequestContext(request))


def edit_tipo_inmueble(request, pk):
    """docstring"""
    tipo_inmueble = Tipo_Inmueble.objects.get(pk=pk)

    if request.method == 'POST':
        form_edit_tipo_inmueble = TipoInmuebleForm(request.POST, instance=tipo_inmueble)
        if form_edit_tipo_inmueble.is_valid():
            form_edit_tipo_inmueble.save()
            return HttpResponseRedirect(reverse('udireciones:lista_tipo_inmueble'))
    else:
        form_edit_tipo_inmueble = TipoInmuebleForm(instance=tipo_inmueble)

    return render_to_response('direccion/tipo_inmueble_edit.html',
                              {'form_edit_tipo_inmueble': form_edit_tipo_inmueble,
                               'create': True}, context_instance=RequestContext(request))


def edit_complejidad_inmueble(request, pk):
    """docstring"""

    complejidad_inmueble = Complejidad_Inmueble.objects.get(pk=pk)

    if request.method == 'POST':
        form_edit_complejidad_inmueble = ComplejidadInmuebleForm(request.POST, instance=complejidad_inmueble)
        if form_edit_complejidad_inmueble.is_valid():
            form_edit_complejidad_inmueble.save()
            return HttpResponseRedirect(reverse('udireciones:lista_complejidad_inmueble'))
    else:
        form_edit_complejidad_inmueble = ComplejidadInmuebleForm(instance=complejidad_inmueble)

    return render_to_response('direccion/complejidad_inmueble_edit.html',
                              {'form_edit_complejidad_inmueble': form_edit_complejidad_inmueble,
                               'create': True}, context_instance=RequestContext(request))


def edit_inmueble(request, pk):
    """docstring"""
    inmueble = Inmueble.objects.get(pk=pk)

    if request.method == 'POST':
        form_edit_inmueble = InmuebleForm(request.POST, instance=inmueble)
        if form_edit_inmueble.is_valid():
            form_edit_inmueble.save()
            return HttpResponseRedirect(reverse('udireciones:lista_inmueble'))
    else:
        form_edit_inmueble = InmuebleForm()

    return render_to_response('direccion/inmueble_add.html',
                              {'form_edit_inmueble': form_edit_inmueble, 'create': True},
                              context_instance=RequestContext(request))
