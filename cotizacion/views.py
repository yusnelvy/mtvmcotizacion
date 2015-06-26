from django.shortcuts import render, render_to_response
from cotizacion.models import Estado_Cotizacion, \
    Piso, Tiempo_Carga, Cotizacion, Vehiculo, \
    Vehiculo_Cotizacion, Cotizacion_direccion, \
    Cotizacion_trabajador, Cotizacion_Ambiente, \
    Cotizacion_Mueble, Cotizacion_Servicio, \
    Cotizacion_Material, Cotizacion_Contenido
from cotizacion.forms import EstadoCotizacionForm, \
    PisoForm, TiempoCargaForm, CotizacionForm, VehiculoForm, \
    VehiculoCotizacionForm, CotizaciondireccionForm, \
    CotizaciontrabajadorForm, CotizacionAmbienteForm, \
    CotizacionMuebleForm, CotizacionServicioForm, \
    CotizacionMaterialForm, CotizacionContenidoForm
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
import simplejson as json
import django.db
from django.db.models import F

from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
# lista
@login_required
def lista_estado_cotizacion(request):
    """docstring"""

    if request.method == "POST":
        if "item_id" in request.POST:
            try:
                id_estadocotizacion = request.POST['item_id']
                p = Estado_Cotizacion.objects.get(pk=id_estadocotizacion)
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

    lista_estadocotizacion = Estado_Cotizacion.objects.all()
    paginator = Paginator(lista_estadocotizacion, 25)
    # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        estadoscotizacion = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        estadoscotizacion = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        estadoscotizacion = paginator.page(paginator.num_pages)
    context = {'lista_estadocotizacion': lista_estadocotizacion, 'estadoscotizacion': estadoscotizacion}
    return render(request, 'cotizacion/estadocotizacion_lista.html', context)


def lista_piso(request):
    """docstring"""

    if request.method == "POST":
        if "item_id" in request.POST:
            try:
                id_piso = request.POST['item_id']
                p = Piso.objects.get(pk=id_piso)
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

    lista_piso = Piso.objects.all()
    context = {'lista_piso': lista_piso}
    return render(request, 'cotizacion/piso_lista.html', context)


def lista_tiempocarga(request):
    """docstring"""

    if request.method == "POST":
        if "item_id" in request.POST:
            try:
                id_tiempocarga = request.POST['item_id']
                p = Tiempo_Carga.objects.get(pk=id_tiempocarga)
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

    lista_tiempocarga = Tiempo_Carga.objects.all()
    paginator = Paginator(lista_tiempocarga, 25)
    # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        tiempocargas = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        tiempocargas = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        tiempocargas = paginator.page(paginator.num_pages)
    context = {'lista_tiempocarga': lista_tiempocarga, 'tiempocargas': tiempocargas}
    return render(request, 'cotizacion/tiempocarga_lista.html', context)


@login_required
def lista_cotizacion(request):
    """docstring"""

    if request.method == "POST":
        if "item_id" in request.POST:
            try:
                id_cotizacion = request.POST['item_id']
                p = Cotizacion.objects.get(pk=id_cotizacion)
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

    lista_cotizacion = Cotizacion.objects.all()
    context = {'lista_cotizacion': lista_cotizacion}
    return render(request, 'cotizacion/cotizacion_lista.html', context)


def lista_vehiculo(request):
    """docstring"""

    if request.method == "POST":
        if "item_id" in request.POST:
            try:
                id_vehiculo = request.POST['item_id']
                p = Vehiculo.objects.get(pk=id_vehiculo)
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

    lista_vehiculo = Vehiculo.objects.all()

    paginator = Paginator(lista_vehiculo, 25)
    # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        vehiculos = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        vehiculos = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        vehiculos = paginator.page(paginator.num_pages)

    context = {'lista_vehiculo': lista_vehiculo, 'vehiculos': vehiculos}
    return render(request, 'cotizacion/vehiculo_lista.html', context)


def buscar_vehiculocotizacion(request, idcotizacion):
    """docstring"""

    if request.method == "POST":
        if "item_id" in request.POST:
            try:
                id_vehiculocotizacion = request.POST['item_id']
                p = Vehiculo_Cotizacion.objects.get(pk=id_vehiculocotizacion)
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

    id_cotizacion = Cotizacion.objects.get(id=idcotizacion)
    buscar_vehiculocotizacion = Vehiculo_Cotizacion.objects.filter(cotizacion_id=id_cotizacion)
    context = {'buscar_vehiculocotizacion': buscar_vehiculocotizacion}
    return render(request, 'cotizacion/vehiculocotizacion_lista.html', context)


def buscar_direccioncotizacion(request, idcotizacion):
    """docstring"""

    if request.method == "POST":
        if "item_id" in request.POST:
            try:
                id_direccioncotizacion = request.POST['item_id']
                p = Cotizacion_direccion.objects.get(pk=id_direccioncotizacion)
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

    id_cotizacion = Cotizacion.objects.get(id=idcotizacion)
    buscar_direccioncotizacion = Cotizacion_direccion.objects.filter(cotizacion_id=id_cotizacion)
    context = {'buscar_direccioncotizacion': buscar_direccioncotizacion}
    return render(request, 'cotizacion/direccioncotizacion_lista.html', context)


def buscar_cotizaciontrabajador(request, idcotizacion):
    """docstring"""

    if request.method == "POST":
        if "item_id" in request.POST:
            try:
                id_cotizaciontrabajador = request.POST['item_id']
                p = Cotizacion_trabajador.objects.get(pk=id_cotizaciontrabajador)
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

    id_cotizacion = Cotizacion.objects.get(id=idcotizacion)
    buscar_cotizaciontrabajador = Cotizacion_trabajador.objects.filter(cotizacion_id=id_cotizacion)
    context = {'buscar_cotizaciontrabajador': buscar_cotizaciontrabajador}
    return render(request, 'cotizacion/cotizaciontrabajador_lista.html', context)


def buscar_cotizacionambiente(request, idcotizacion):
    """docstring"""

    if request.method == "POST":
        if "item_id" in request.POST:
            try:
                id_cotizacionambiente = request.POST['item_id']
                p = Cotizacion_Ambiente.objects.get(pk=id_cotizacionambiente)
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

    id_cotizacion = Cotizacion.objects.get(id=idcotizacion)
    buscar_cotizacionambiente = Cotizacion_Ambiente.objects.filter(cotizacion_id=id_cotizacion)
    context = {'buscar_cotizacionambiente': buscar_cotizacionambiente}
    return render(request, 'cotizacion/cotizacionambiente_lista.html', context)


def buscar_cotizacionmueble(request, idcotizacionambiente):
    """docstring"""

    if request.method == "POST":
        if "item_id" in request.POST:
            try:
                id_cotizacionmueble = request.POST['item_id']
                p = Cotizacion_Mueble.objects.get(pk=id_cotizacionmueble)
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

    id_cotizacionambiente = Cotizacion_Ambiente.objects.get(id=idcotizacionambiente)
    buscar_cotizacionmueble = Cotizacion_Mueble.objects.filter(cotizacion_ambiente_id=id_cotizacionambiente)
    context = {'buscar_cotizacionmueble': buscar_cotizacionmueble}
    return render(request, 'cotizacion/cotizacionmueble_lista.html', context)


def buscar_cotizacionservicio(request, idcotizacionmueble):
    """docstring"""

    if request.method == "POST":
        if "item_id" in request.POST:
            try:
                id_cotizacionservicio = request.POST['item_id']
                p = Cotizacion_Servicio.objects.get(pk=id_cotizacionservicio)
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

    id_cotizacionmueble = Cotizacion_Mueble.objects.get(id=idcotizacionmueble)
    buscar_cotizacionservicio = Cotizacion_Servicio.objects.filter(cotizacion_mueble_id=id_cotizacionmueble)
    context = {'buscar_cotizacionservicio': buscar_cotizacionservicio}
    return render(request, 'cotizacion/cotizacionservicio_lista.html', context)


def buscar_cotizacionmaterial(request, idcotizacionservicio):
    """docstring"""

    if request.method == "POST":
        if "item_id" in request.POST:
            try:
                id_cotizacionmaterial = request.POST['item_id']
                p = Cotizacion_Material.objects.get(pk=id_cotizacionmaterial)
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

    id_cotizacionservicio = Cotizacion_Servicio.objects.get(id=idcotizacionservicio)
    buscar_cotizacionmaterial = Cotizacion_Material.objects.filter(cotizacion_servicio_id=id_cotizacionservicio)
    context = {'buscar_cotizacionmaterial': buscar_cotizacionmaterial}
    return render(request, 'cotizacion/cotizacionmaterial_lista.html', context)


def buscar_cotizacioncontenido(request, idcotizacionmueble):
    """docstring"""

    if request.method == "POST":
        if "item_id" in request.POST:
            try:
                id_cotizacioncontenido = request.POST['item_id']
                p = Cotizacion_Contenido.objects.get(pk=id_cotizacioncontenido)
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

    id_cotizacionmueble = Cotizacion_Mueble.objects.get(id=idcotizacionmueble)
    buscar_cotizacioncontenido = Cotizacion_Contenido.objects.filter(cotizacion_mueble_id=id_cotizacionmueble)
    context = {'buscar_cotizacioncontenido': buscar_cotizacioncontenido}
    return render(request, 'cotizacion/cotizacioncontenido_lista.html', context)


def buscar_cotizacion(request, pk):
    """docstring"""

    buscar_cotizacion = Cotizacion.objects.filter(pk=pk)
    det_direccion = Cotizacion_direccion.objects.filter(cotizacion_id=pk)
    det_vehiculo = Vehiculo_Cotizacion.objects.filter(cotizacion_id=pk)
    det_trabajador = Cotizacion_trabajador.objects.filter(cotizacion_id=pk)
    det_ambiente = Cotizacion_Ambiente.objects.filter(cotizacion_id=pk)
    det_mueble = Cotizacion_Mueble.objects.filter(cotizacion_ambiente__cotizacion_id=pk)
    det_servicio = Cotizacion_Servicio.objects.filter(cotizacion_mueble__cotizacion_ambiente__cotizacion_id=pk, cotizacion_contenido_id=None)
    det_material = Cotizacion_Material.objects.filter(cotizacion_servicio__cotizacion_mueble__cotizacion_ambiente__cotizacion_id=pk)
    det_contenido = Cotizacion_Contenido.objects.filter(cotizacion_mueble__cotizacion_ambiente__cotizacion_id=pk)
    det_servicio_contenido = Cotizacion_Servicio.objects.filter(cotizacion_mueble__cotizacion_ambiente__cotizacion_id=pk).exclude(cotizacion_contenido_id=None)

    for modelObject in buscar_cotizacion:
        suma = modelObject.volumen_contenedores + modelObject.volumen_muebles_cotizado

    context = {
        'buscar_cotizacion': buscar_cotizacion,
        'det_direccion': det_direccion,
        'det_vehiculo': det_vehiculo,
        'det_trabajador': det_trabajador,
        'det_ambiente': det_ambiente,
        'total_m': suma,
        'det_mueble': det_mueble,
        'det_servicio': det_servicio,
        'det_material': det_material,
        'det_contenido': det_contenido,
        'det_servicio_contenido': det_servicio_contenido

    }
    return render(request, 'cotizacion/cotizacion_buscar2.html', context)


# agregar nuevo
def add_estadocotizacion(request):
    """docstring"""

    if request.method == 'POST':
        form_estadocotizacion = EstadoCotizacionForm(request.POST)
        if form_estadocotizacion.is_valid():
            form_estadocotizacion.save()
            return HttpResponseRedirect(reverse('ucotizaciones:lista_estado_cotizacion'))

    else:
        form_estadocotizacion = EstadoCotizacionForm()
    return render_to_response('cotizacion/estadocotizacion_add.html',
                              {'form_estadocotizacion': form_estadocotizacion, 'create': True},
                              context_instance=RequestContext(request))


def add_piso(request):
    """docstring"""

    if request.method == 'POST':
        form_piso = PisoForm(request.POST)
        if form_piso.is_valid():
            form_piso.save()
            return HttpResponseRedirect(reverse('ucotizaciones:lista_piso'))

    else:
        form_piso = PisoForm()
    return render_to_response('cotizacion/piso_add.html',
                              {'form_piso': form_piso, 'create': True},
                              context_instance=RequestContext(request))


def add_tiempocarga(request):
    """docstring"""

    if request.method == 'POST':
        form_tiempocarga = TiempoCargaForm(request.POST)
        if form_tiempocarga.is_valid():
            form_tiempocarga.save()
            return HttpResponseRedirect(reverse('ucotizaciones:lista_tiempocarga'))

    else:
        form_tiempocarga = TiempoCargaForm()
    return render_to_response('cotizacion/tiempocarga_add.html',
                              {'form_tiempocarga': form_tiempocarga, 'create': True},
                              context_instance=RequestContext(request))


def add_cotizacion(request):
    """docstring"""

    if request.method == 'POST':
        form_cotizacion = CotizacionForm(request.POST)
        if form_cotizacion.is_valid():
            form_cotizacion.save()
            return HttpResponseRedirect(reverse('ucotizaciones:lista_cotizacion'))

    else:
        form_cotizacion = CotizacionForm()
    return render_to_response('cotizacion/cotizacion_add.html',
                              {'form_cotizacion': form_cotizacion, 'create': True},
                              context_instance=RequestContext(request))


def add_vehiculo(request):
    """docstring"""

    if request.method == 'POST':
        form_vehiculo = VehiculoForm(request.POST)
        if form_vehiculo.is_valid():
            form_vehiculo.save()
            return HttpResponseRedirect(reverse('ucotizaciones:lista_vehiculo'))

    else:
        form_vehiculo = VehiculoForm()
    return render_to_response('cotizacion/vehiculo_add.html',
                              {'form_vehiculo': form_vehiculo, 'create': True},
                              context_instance=RequestContext(request))


def add_vehiculocotizacion(request):
    """docstring"""

    if request.method == 'POST':
        form_vehiculocotizacion = VehiculoCotizacionForm(request.POST)
        if form_vehiculocotizacion.is_valid():
            id_reg = form_vehiculocotizacion.save()
            id_cot = Vehiculo_Cotizacion.objects.get(id=id_reg.id)

            return HttpResponseRedirect(reverse('ucotizaciones:buscar_vehiculocotizacion', args=(id_cot.cotizacion.id,)))

    else:
        form_vehiculocotizacion = VehiculoCotizacionForm()
    return render_to_response('cotizacion/vehiculocotizacion_add.html',
                              {'form_vehiculocotizacion': form_vehiculocotizacion, 'create': True},
                              context_instance=RequestContext(request))


def add_cotizaciondireccion(request, idcotizacion):
    """docstring"""

    if request.method == 'POST':
        form_cotizaciondireccion = CotizaciondireccionForm(request.POST)
        if form_cotizaciondireccion.is_valid():
            id_reg = form_cotizaciondireccion.save()
            id_cot = Cotizacion_direccion.objects.get(id=id_reg.id)
            return HttpResponseRedirect(reverse('ucotizaciones:buscar_direccioncotizacion', args=(id_cot.cotizacion.id,)))

    else:
        form_cotizaciondireccion = CotizaciondireccionForm(initial={'cotizacion': idcotizacion})
    return render_to_response('cotizacion/direccioncotizacion_add.html',
                              {'form_cotizaciondireccion': form_cotizaciondireccion, 'create': True},
                              context_instance=RequestContext(request))


def add_cotizaciontrabajador(request, idcotizacion):
    """docstring"""

    if request.method == 'POST':
        form_cotizaciontrabajador = CotizaciontrabajadorForm(request.POST)
        if form_cotizaciontrabajador.is_valid():
            id_reg = form_cotizaciontrabajador.save()
            id_cot = Cotizacion_trabajador.objects.get(id=id_reg.id)
            return HttpResponseRedirect(reverse('ucotizaciones:buscar_cotizaciontrabajador', args=(id_cot.cotizacion.id,)))

    else:
        form_cotizaciontrabajador = CotizaciontrabajadorForm(initial={'cotizacion': idcotizacion})
    return render_to_response('cotizacion/cotizaciontrabajador_add.html',
                              {'form_cotizaciontrabajador': form_cotizaciontrabajador, 'create': True},
                              context_instance=RequestContext(request))


def add_cotizacionambiente(request, idcotizacion):
    """docstring"""

    if request.method == 'POST':
        form_cotizacionambiente = CotizacionAmbienteForm(request.POST)
        if form_cotizacionambiente.is_valid():
            id_reg = form_cotizacionambiente.save()
            id_cot = Cotizacion_Ambiente.objects.get(id=id_reg.id)
            return HttpResponseRedirect(reverse('ucotizaciones:buscar_cotizacionambiente', args=(id_cot.cotizacion.id,)))

    else:
        form_cotizacionambiente = CotizacionAmbienteForm(initial={'cotizacion': idcotizacion})
    return render_to_response('cotizacion/cotizacionambiente_add.html',
                              {'form_cotizacionambiente': form_cotizacionambiente, 'create': True},
                              context_instance=RequestContext(request))


def add_cotizacionmueble(request, idcotizacionambiente):
    """docstring"""

    if request.method == 'POST':
        form_cotizacionmueble = CotizacionMuebleForm(request.POST)
        if form_cotizacionmueble.is_valid():
            id_reg = form_cotizacionmueble.save()
            id_cot = Cotizacion_Mueble.objects.get(id=id_reg.id)
            return HttpResponseRedirect(reverse('ucotizaciones:buscar_cotizacionmueble', args=(id_cot.cotizacion_ambiente.id,)))

    else:
        form_cotizacionmueble = CotizacionMuebleForm(initial={'cotizacion_ambiente': idcotizacionambiente})
    return render_to_response('cotizacion/cotizacionmueble_add.html',
                              {'form_cotizacionmueble': form_cotizacionmueble, 'create': True},
                              context_instance=RequestContext(request))


def add_cotizacionservicio(request, idcotizacionmueble, idcotizacioncontenido=None):
    """docstring"""

    if request.method == 'POST':
        form_cotizacionservicio = CotizacionServicioForm(request.POST)
        if form_cotizacionservicio.is_valid():
            id_reg = form_cotizacionservicio.save()
            id_cot = Cotizacion_Servicio.objects.get(id=id_reg.id)
            return HttpResponseRedirect(reverse('ucotizaciones:buscar_cotizacionservicio', args=(id_cot.cotizacion_mueble.id,)))

    else:
        if idcotizacioncontenido is None:

            data = {'cotizacion_mueble': idcotizacionmueble}

        else:
            data = {
                'cotizacion_mueble': idcotizacionmueble,
                'cotizacion_contenido': idcotizacioncontenido
                }

        form_cotizacionservicio = CotizacionServicioForm(initial=data)
    return render_to_response('cotizacion/cotizacionservicio_add.html',
                              {'form_cotizacionservicio': form_cotizacionservicio, 'create': True},
                              context_instance=RequestContext(request))


def add_cotizacionmaterial(request, idcotizacionservicio):
    """docstring"""

    if request.method == 'POST':
        form_cotizacionmaterial = CotizacionMaterialForm(request.POST)
        if form_cotizacionmaterial.is_valid():
            id_reg = form_cotizacionmaterial.save()
            id_cot = Cotizacion_Material.objects.get(id=id_reg.id)

            return HttpResponseRedirect(reverse('ucotizaciones:buscar_cotizacionmaterial', args=(id_cot.cotizacion_servicio.id,)))

    else:

        form_cotizacionmaterial = CotizacionMaterialForm(initial={'cotizacion_servicio': idcotizacionservicio})

    return render_to_response('cotizacion/cotizacionmaterial_add.html',
                              {'form_cotizacionmaterial': form_cotizacionmaterial, 'create': True},
                              context_instance=RequestContext(request))


def add_cotizacioncontenido(request, idcotizacionmueble):
    """docstring"""

    if request.method == 'POST':
        form_cotizacioncontenido = CotizacionContenidoForm(request.POST)
        if form_cotizacioncontenido.is_valid():
            id_reg = form_cotizacioncontenido.save()
            id_cot = Cotizacion_Contenido.objects.get(id=id_reg.id)
            return HttpResponseRedirect(reverse('ucotizaciones:buscar_cotizacioncontenido', args=(id_cot.cotizacion_mueble.id,)))

    else:
        form_cotizacioncontenido = CotizacionContenidoForm(initial={'cotizacion_mueble': idcotizacionmueble})
    return render_to_response('cotizacion/cotizacioncontenido_add.html',
                              {'form_cotizacioncontenido': form_cotizacioncontenido, 'create': True},
                              context_instance=RequestContext(request))


# editar un registro
def edit_estadocotizacion(request, pk):

    try:
        id_estadocotizacion = Estado_Cotizacion.objects.get(pk=pk)
    except ObjectDoesNotExist as ex:
        mensaje = "El registro no existe"
    except Exception as ex:
        mensaje = "se ha producido un error"+str(ex)

    redirect_to = request.REQUEST.get('next', '')

    if request.method == 'POST':
        # formulario enviado
        editar_estadocotizacion = EstadoCotizacionForm(request.POST, instance=id_estadocotizacion)

        if editar_estadocotizacion.is_valid():
            # formulario validado correctamente
            editar_estadocotizacion.save()

            if redirect_to:
                return HttpResponseRedirect(redirect_to)
            else:
                return HttpResponseRedirect(reverse('ucotizaciones:lista_estado_cotizacion'))

    else:
        # formulario inicial
        editar_estadocotizacion = EstadoCotizacionForm(instance=id_estadocotizacion)
        mensaje = ""
    return render_to_response('cotizacion/estadocotizacion_edit.html',
                              {'editar_estadocotizacion': editar_estadocotizacion, 'id_estadocotizacion': pk, 'create': False, 'mensaje': mensaje},
                              context_instance=RequestContext(request))


def edit_piso(request, pk):

    try:
        id_piso = Piso.objects.get(pk=pk)
    except ObjectDoesNotExist as ex:
        mensaje = "El piso no existe"
    except Exception as ex:
        mensaje = "se ha producido un error"+str(ex)

    if request.method == 'POST':
        # formulario enviado
        editar_piso = PisoForm(request.POST, instance=id_piso)

        if editar_piso.is_valid():
            # formulario validado correctamente
            editar_piso.save()

            return HttpResponseRedirect(reverse('ucotizaciones:lista_piso'))

    else:
        # formulario inicial
        editar_piso = PisoForm(instance=id_piso)
        mensaje = ""
    return render_to_response('cotizacion/piso_edit.html',
                              {'editar_piso': editar_piso, 'id_piso': pk, 'create': False, 'mensaje': mensaje},
                              context_instance=RequestContext(request))


def edit_tiempocarga(request, pk):

    try:
        id_tiempocarga = Tiempo_Carga.objects.get(pk=pk)
    except ObjectDoesNotExist as ex:
        mensaje = "El tiempo de carga no existe"
    except Exception as ex:
        mensaje = "se ha producido un error"+str(ex)

    if request.method == 'POST':
        # formulario enviado
        editar_tiempocarga = TiempoCargaForm(request.POST, instance=id_tiempocarga)

        if editar_tiempocarga.is_valid():
            # formulario validado correctamente
            editar_tiempocarga.save()

            return HttpResponseRedirect(reverse('ucotizaciones:lista_tiempocarga'))

    else:
        # formulario inicial
        editar_tiempocarga = TiempoCargaForm(instance=id_tiempocarga)
        mensaje = ""
    return render_to_response('cotizacion/tiempocarga_edit.html',
                              {'editar_tiempocarga': editar_tiempocarga, 'id_tiempocarga': pk, 'create': False, 'mensaje': mensaje},
                              context_instance=RequestContext(request))


@permission_required('cotizacion.change_cotizacion')
def edit_cotizacion(request, pk):

    redirect_to = request.REQUEST.get('next', '')

    try:
        id_cotizacion = Cotizacion.objects.get(pk=pk)
    except ObjectDoesNotExist as ex:
        mensaje = "la cotizacion no existe"
    except Exception as ex:
        mensaje = "se ha producido un error"+str(ex)

    if request.method == 'POST':
        # formulario enviado
        editar_cotizacion = CotizacionForm(request.POST, instance=id_cotizacion)

        if editar_cotizacion.is_valid():
            # formulario validado correctamente
            id_reg = editar_cotizacion.save()

            #prueba para actualizar un campo calculable
            reporter = Cotizacion.objects.filter(pk=id_reg.id)
            reporter.update(cantidad_ambientes=F('cantidad_ambientes')+1)

        if redirect_to:

            return HttpResponseRedirect(redirect_to)
        else:
            return HttpResponseRedirect(reverse('ucotizaciones:lista_cotizacion'))

    else:
        # formulario inicial
        editar_cotizacion = CotizacionForm(instance=id_cotizacion)
        mensaje = ""
    return render_to_response('cotizacion/cotizacion_edit.html',
                              {'editar_cotizacion': editar_cotizacion, 'id_cotizacion': pk, 'create': False, 'mensaje': mensaje},
                              context_instance=RequestContext(request))


def edit_vehiculo(request, pk):

    try:
        id_vehiculo = Vehiculo.objects.get(pk=pk)
    except ObjectDoesNotExist as ex:
        mensaje = "El vehiculo no existe"
    except Exception as ex:
        mensaje = "se ha producido un error"+str(ex)

    redirect_to = request.REQUEST.get('next', '')

    if request.method == 'POST':
        # formulario enviado
        editar_vehiculo = VehiculoForm(request.POST, instance=id_vehiculo)

        if editar_vehiculo.is_valid():
            # formulario validado correctamente
            editar_vehiculo.save()

            if redirect_to:
                return HttpResponseRedirect(redirect_to)
            else:
                return HttpResponseRedirect(reverse('ucotizaciones:lista_vehiculo'))

    else:
        # formulario inicial
        editar_vehiculo = VehiculoForm(instance=id_vehiculo)
        mensaje = ""
    return render_to_response('cotizacion/vehiculo_edit.html',
                              {'editar_vehiculo': editar_vehiculo, 'id_vehiculo': pk, 'create': False, 'mensaje': mensaje},
                              context_instance=RequestContext(request))


def edit_vehiculocotizacion(request, pk):

    try:
        id_vehiculocotizacion = Vehiculo_Cotizacion.objects.get(pk=pk)
    except ObjectDoesNotExist as ex:
        mensaje = "El registro no existe"
    except Exception as ex:
        mensaje = "se ha producido un error"+str(ex)

    if request.method == 'POST':
        # formulario enviado
        editar_vehiculocotizacion = VehiculoCotizacionForm(request.POST, instance=id_vehiculocotizacion)

        if editar_vehiculocotizacion.is_valid():
            # formulario validado correctamente
            editar_vehiculocotizacion.save()

            return HttpResponseRedirect(reverse('ucotizaciones:buscar_vehiculocotizacion', args=(id_vehiculocotizacion.cotizacion.id,)))

    else:
        # formulario inicial
        editar_vehiculocotizacion = VehiculoCotizacionForm(instance=id_vehiculocotizacion)
        mensaje = ""
    return render_to_response('cotizacion/vehiculocotizacion_edit.html',
                              {'editar_vehiculocotizacion': editar_vehiculocotizacion, 'id_vehiculocotizacion': pk, 'create': False, 'mensaje': mensaje},
                              context_instance=RequestContext(request))


def edit_cotizaciondireccion(request, pk):

    try:
        id_cotizaciondireccion = Cotizacion_direccion.objects.get(pk=pk)
    except ObjectDoesNotExist as ex:
        mensaje = "El registro no existe"
    except Exception as ex:
        mensaje = "se ha producido un error"+str(ex)

    if request.method == 'POST':
        # formulario enviado
        editar_cotizaciondireccion = CotizaciondireccionForm(request.POST, instance=id_cotizaciondireccion)

        if editar_cotizaciondireccion.is_valid():
            # formulario validado correctamente
            editar_cotizaciondireccion.save()

            return HttpResponseRedirect(reverse('ucotizaciones:buscar_direccioncotizacion', args=(id_cotizaciondireccion.cotizacion.id,)))

    else:
        # formulario inicial
        editar_cotizaciondireccion = CotizaciondireccionForm(instance=id_cotizaciondireccion)
        mensaje = ""
    return render_to_response('cotizacion/direccioncotizacion_edit.html',
                              {'editar_cotizaciondireccion': editar_cotizaciondireccion, 'id_cotizaciondireccion': pk, 'create': False, 'mensaje': mensaje},
                              context_instance=RequestContext(request))


def edit_cotizaciontrabajador(request, pk):

    try:
        id_cotizaciontrabajador = Cotizacion_trabajador.objects.get(pk=pk)
    except ObjectDoesNotExist as ex:
        mensaje = "El registro no existe"
    except Exception as ex:
        mensaje = "se ha producido un error"+str(ex)

    if request.method == 'POST':
        # formulario enviado
        editar_cotizaciontrabajador = CotizaciontrabajadorForm(request.POST, instance=id_cotizaciontrabajador)

        if editar_cotizaciontrabajador.is_valid():
            # formulario validado correctamente
            editar_cotizaciontrabajador.save()

            return HttpResponseRedirect(reverse('ucotizaciones:buscar_cotizaciontrabajador', args=(id_cotizaciontrabajador.cotizacion.id,)))

    else:
        # formulario inicial
        editar_cotizaciontrabajador = CotizaciontrabajadorForm(instance=id_cotizaciontrabajador)
        mensaje = ""
    return render_to_response('cotizacion/cotizaciontrabajador_edit.html',
                              {'editar_cotizaciontrabajador': editar_cotizaciontrabajador, 'id_cotizaciontrabajador': pk, 'create': False, 'mensaje': mensaje},
                              context_instance=RequestContext(request))


def edit_cotizacionambiente(request, pk):

    try:
        id_cotizacionambiente = Cotizacion_Ambiente.objects.get(pk=pk)
    except ObjectDoesNotExist as ex:
        mensaje = "El registro no existe"
    except Exception as ex:
        mensaje = "se ha producido un error"+str(ex)

    if request.method == 'POST':
        # formulario enviado
        editar_cotizacionambiente = CotizacionAmbienteForm(request.POST, instance=id_cotizacionambiente)

        if editar_cotizacionambiente.is_valid():
            # formulario validado correctamente
            editar_cotizacionambiente.save()

            return HttpResponseRedirect(reverse('ucotizaciones:buscar_cotizacionambiente', args=(id_cotizacionambiente.cotizacion.id,)))

    else:
        # formulario inicial
        editar_cotizacionambiente = CotizacionAmbienteForm(instance=id_cotizacionambiente)
        mensaje = ""
    return render_to_response('cotizacion/cotizacionambiente_edit.html',
                              {'editar_cotizacionambiente': editar_cotizacionambiente, 'id_cotizacionambiente': pk, 'create': False, 'mensaje': mensaje},
                              context_instance=RequestContext(request))


def edit_cotizacionmueble(request, pk):

    try:
        id_cotizacionmueble = Cotizacion_Mueble.objects.get(pk=pk)
    except ObjectDoesNotExist as ex:
        mensaje = "El registro no existe"
    except Exception as ex:
        mensaje = "se ha producido un error"+str(ex)

    if request.method == 'POST':
        # formulario enviado
        editar_cotizacionmueble = CotizacionMuebleForm(request.POST, instance=id_cotizacionmueble)

        if editar_cotizacionmueble.is_valid():
            # formulario validado correctamente
            editar_cotizacionmueble.save()

            return HttpResponseRedirect(reverse('ucotizaciones:buscar_cotizacionmueble', args=(id_cotizacionmueble.cotizacion_ambiente.id,)))

    else:
        # formulario inicial
        editar_cotizacionmueble = CotizacionMuebleForm(instance=id_cotizacionmueble)
        mensaje = ""
    return render_to_response('cotizacion/cotizacionmueble_edit.html',
                              {'editar_cotizacionmueble': editar_cotizacionmueble, 'id_cotizacionmueble': pk, 'create': False, 'mensaje': mensaje},
                              context_instance=RequestContext(request))


def edit_cotizacionservicio(request, pk):

    try:
        id_cotizacionservicio = Cotizacion_Servicio.objects.get(pk=pk)
    except ObjectDoesNotExist as ex:
        mensaje = "El registro no existe"
    except Exception as ex:
        mensaje = "se ha producido un error"+str(ex)

    if request.method == 'POST':
        # formulario enviado
        editar_cotizacionservicio = CotizacionServicioForm(request.POST, instance=id_cotizacionservicio)

        if editar_cotizacionservicio.is_valid():
            # formulario validado correctamente
            editar_cotizacionservicio.save()

            return HttpResponseRedirect(reverse('ucotizaciones:buscar_cotizacionservicio', args=(id_cotizacionservicio.cotizacion_mueble.id,)))

    else:
        # formulario inicial
        editar_cotizacionservicio = CotizacionServicioForm(instance=id_cotizacionservicio)
        mensaje = ""
    return render_to_response('cotizacion/cotizacionservicio_edit.html',
                              {'editar_cotizacionservicio': editar_cotizacionservicio, 'id_cotizacionservicio': pk, 'create': False, 'mensaje': mensaje},
                              context_instance=RequestContext(request))


def edit_cotizacionmaterial(request, pk):

    try:
        id_cotizacionmaterial = Cotizacion_Material.objects.get(pk=pk)
    except ObjectDoesNotExist as ex:
        mensaje = "El registro no existe"
    except Exception as ex:
        mensaje = "se ha producido un error"+str(ex)

    if request.method == 'POST':
        # formulario enviado
        editar_cotizacionmaterial = CotizacionMaterialForm(request.POST, instance=id_cotizacionmaterial)

        if editar_cotizacionmaterial.is_valid():
            # formulario validado correctamente
            editar_cotizacionmaterial.save()

            return HttpResponseRedirect(reverse('ucotizaciones:buscar_cotizacionmaterial', args=(id_cotizacionmaterial.cotizacion_servicio.id,)))

    else:
        # formulario inicial
        editar_cotizacionmaterial = CotizacionMaterialForm(instance=id_cotizacionmaterial)
        mensaje = ""
    return render_to_response('cotizacion/cotizacionmaterial_edit.html',
                              {'editar_cotizacionmaterial': editar_cotizacionmaterial, 'id_cotizacionmaterial': pk, 'create': False, 'mensaje': mensaje},
                              context_instance=RequestContext(request))


def edit_cotizacioncontenido(request, pk):

    try:
        id_cotizacioncontenido = Cotizacion_Contenido.objects.get(pk=pk)
    except ObjectDoesNotExist as ex:
        mensaje = "El registro no existe"
    except Exception as ex:
        mensaje = "se ha producido un error"+str(ex)

    if request.method == 'POST':
        # formulario enviado
        editar_cotizacioncontenido = CotizacionContenidoForm(request.POST, instance=id_cotizacioncontenido)

        if editar_cotizacioncontenido.is_valid():
            # formulario validado correctamente
            editar_cotizacioncontenido.save()

            return HttpResponseRedirect(reverse('ucotizaciones:buscar_cotizacioncontenido', args=(id_cotizacioncontenido.cotizacion_mueble.id,)))

    else:
        # formulario inicial
        editar_cotizacioncontenido = CotizacionContenidoForm(instance=id_cotizacioncontenido)
        mensaje = ""
    return render_to_response('cotizacion/cotizacioncontenido_edit.html',
                              {'editar_cotizacioncontenido': editar_cotizacioncontenido, 'id_cotizacioncontenido': pk, 'create': False, 'mensaje': mensaje},
                              context_instance=RequestContext(request))
