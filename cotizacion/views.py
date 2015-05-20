from django.shortcuts import render, render_to_response
from cotizacion.models import Estado_Cotizacion, \
    Piso, Tiempo_Carga, Cotizacion, Vehiculo, \
    Vehiculo_Cotizacion, Cotizacion_direccion, \
    Cotizacion_trabajador, Cotizacion_Ambiente, \
    Cotizacion_Mueble, Cotizacion_Servicio, \
    Cotizacion_Material, Cotizacion_Contenedor, \
    Cotizacion_Contenido
from cotizacion.forms import EstadoCotizacionForm, \
    PisoForm, TiempoCargaForm, CotizacionForm, VehiculoForm, \
    VehiculoCotizacionForm, CotizaciondireccionForm, \
    CotizaciontrabajadorForm, CotizacionAmbienteForm, \
    CotizacionMuebleForm, CotizacionServicioForm, \
    CotizacionMaterialForm, CotizacionContenedorForm, \
    CotizacionContenidoForm
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.core.urlresolvers import reverse
import django.db
import simplejson as json



# Create your views here.
# lista
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
    context = {'lista_estadocotizacion': lista_estadocotizacion}
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
    context = {'lista_tiempocarga': lista_tiempocarga}
    return render(request, 'cotizacion/tiempocarga_lista.html', context)


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
    context = {'lista_vehiculo': lista_vehiculo}
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


def buscar_cotizacionmaterial(request, idcotizacionmueble):
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

    id_cotizacionmueble = Cotizacion_Mueble.objects.get(id=idcotizacionmueble)
    buscar_cotizacionmaterial = Cotizacion_Material.objects.filter(cotizacion_mueble_id=id_cotizacionmueble)
    context = {'buscar_cotizacionmaterial': buscar_cotizacionmaterial}
    return render(request, 'cotizacion/cotizacionmaterial_lista.html', context)


def buscar_cotizacioncontenedor(request, idcotizacionmueble):
    """docstring"""

    if request.method == "POST":
        if "item_id" in request.POST:
            try:
                id_cotizacioncontenedor = request.POST['item_id']
                p = Cotizacion_Contenedor.objects.get(pk=id_cotizacioncontenedor)
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
    buscar_cotizacioncontenedor = Cotizacion_Contenedor.objects.filter(cotizacion_mueble_id=id_cotizacionmueble)
    context = {'buscar_cotizacioncontenedor': buscar_cotizacioncontenedor}
    return render(request, 'cotizacion/cotizacioncontenedor_lista.html', context)


def buscar_cotizacioncontenido(request, idcotizacioncontenedor):
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

    id_cotizacioncontenedor = Cotizacion_Contenedor.objects.get(id=idcotizacioncontenedor)
    buscar_cotizacioncontenido = Cotizacion_Contenido.objects.filter(cotizacion_contenedor_id=id_cotizacioncontenedor)
    context = {'buscar_cotizacioncontenido': buscar_cotizacioncontenido}
    return render(request, 'cotizacion/cotizacioncontenido_lista.html', context)


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
            form_vehiculocotizacion.save()
            return HttpResponseRedirect(reverse('ucotizaciones:buscar_vehiculocotizacion'))

    else:
        form_vehiculocotizacion = VehiculoCotizacionForm()
    return render_to_response('vehiculocotizacion/vehiculocotizacion_add.html',
                              {'form_vehiculocotizacion': form_vehiculocotizacion, 'create': True},
                              context_instance=RequestContext(request))


def add_cotizaciondireccion(request):
    """docstring"""

    if request.method == 'POST':
        form_cotizaciondireccion = CotizaciondireccionForm(request.POST)
        if form_cotizaciondireccion.is_valid():
            form_cotizaciondireccion.save()
            return HttpResponseRedirect(reverse('ucotizaciones:buscar_direccioncotizacion'))

    else:
        form_cotizaciondireccion = CotizaciondireccionForm()
    return render_to_response('cotizaciondireccion/direccioncotizacion_add.html',
                              {'form_cotizaciondireccion': form_cotizaciondireccion, 'create': True},
                              context_instance=RequestContext(request))


def add_cotizaciontrabajador(request):
    """docstring"""

    if request.method == 'POST':
        form_cotizaciontrabajador = CotizaciontrabajadorForm(request.POST)
        if form_cotizaciontrabajador.is_valid():
            form_cotizaciontrabajador.save()
            return HttpResponseRedirect(reverse('ucotizaciones:buscar_cotizaciontrabajador'))

    else:
        form_cotizaciontrabajador = CotizaciontrabajadorForm()
    return render_to_response('cotizaciontrabajador/direccioncotizacion_add.html',
                              {'form_cotizaciontrabajador': form_cotizaciontrabajador, 'create': True},
                              context_instance=RequestContext(request))
