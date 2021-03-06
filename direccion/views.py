from django.shortcuts import render, render_to_response
from direccion.models import Pais, Provincia, Ciudad, \
    Zona, Tipo_direccion, Direccion, Tipo_Inmueble, \
    Complejidad_Inmueble, Inmueble
from direccion.forms import PaisForm, ProvinciaForm, \
    CiudadForm, ZonaForm, TipoDireccionForm, \
    DireccionForm, TipoInmuebleForm, \
    ComplejidadInmuebleForm, \
    InmuebleForm
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
import simplejson as json
import django.db
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from mtvmcotizacion.views import get_query
from premisas.models import PerzonalizacionVisual


# Create your views here.
# lista
def lista_pais(request):
    """docstring"""
    if request.user.id is not None:
        try:
            nropag = PerzonalizacionVisual.objects.values('valor').filter(usuario=
                                                                          request.user.id,
                                                                          tipo="paginacion")
        except PerzonalizacionVisual.DoesNotExist:
            nropag = PerzonalizacionVisual.objects.values('valor').filter(usuario__username="std",
                                                                          tipo="paginacion")
    else:
        nropag = PerzonalizacionVisual.objects.values('valor').filter(usuario__username="std",
                                                                      tipo="paginacion")
    order_by = request.GET.get('order_by')
    if order_by:
        lista_pais = Pais.objects.all().order_by(order_by)
    else:
        lista_pais = Pais.objects.all()

    paginator = Paginator(lista_pais, nropag[0]['valor'])
    # Show 25 contacts per page
    page = request.GET.get('page')
    if page == '0':
        paises = lista_pais
    else:
        try:
            paises = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            paises = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            paises = paginator.page(paginator.num_pages)

    context = {'lista_pais': lista_pais, 'paises': paises}
    #return render(request, 'pais_lista.html', context)
    return render_to_response('pais_lista.html',
                              context, context_instance=RequestContext(request))


def search_pais(request):
    if request.user.id is not None:
        try:
            nropag = PerzonalizacionVisual.objects.values('valor').filter(usuario=
                                                                          request.user.id,
                                                                          tipo="paginacion")
        except PerzonalizacionVisual.DoesNotExist:
            nropag = PerzonalizacionVisual.objects.values('valor').filter(usuario__username="std",
                                                                          tipo="paginacion")
    else:
        nropag = PerzonalizacionVisual.objects.values('valor').filter(usuario__username="std",
                                                                      tipo="paginacion")
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

        search_text = request.POST['search_text']
        if search_text is not None and search_text != u"":
            entry_query = get_query(search_text, ['pais', ])
            lista_pais = Pais.objects.filter(entry_query)
        else:
            lista_pais = Pais.objects.all()

    paginator = Paginator(lista_pais, nropag[0]['valor'])
    # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        paises = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        paises = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        paises = paginator.page(paginator.num_pages)

    return render_to_response('pais_lista_search.html',
                              {'lista_pais': lista_pais, 'paises': paises})


def lista_provincia(request):
    """docstring"""
    if request.user.id is not None:
        try:
            nropag = PerzonalizacionVisual.objects.values('valor').filter(usuario=
                                                                          request.user.id,
                                                                          tipo="paginacion")
        except PerzonalizacionVisual.DoesNotExist:
            nropag = PerzonalizacionVisual.objects.values('valor').filter(usuario__username="std",
                                                                          tipo="paginacion")
    else:
        nropag = PerzonalizacionVisual.objects.values('valor').filter(usuario__username="std",
                                                                      tipo="paginacion")
    order_by = request.GET.get('order_by')
    if order_by:
        lista_provincia = Provincia.objects.all().order_by(order_by)
    else:
        lista_provincia = Provincia.objects.all()

    paginator = Paginator(lista_provincia, nropag[0]['valor'])
    # Show 25 contacts per page
    page = request.GET.get('page')

    if page == '0':
        provincias = lista_provincia
    else:
        try:
            provincias = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            provincias = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            provincias = paginator.page(paginator.num_pages)
    context = {'lista_provincia': lista_provincia, 'provincias': provincias}
    return render(request, 'provincia_lista.html', context)


def search_provincia(request):

    if request.user.id is not None:
        try:
            nropag = PerzonalizacionVisual.objects.values('valor').filter(usuario=
                                                                          request.user.id,
                                                                          tipo="paginacion")
        except PerzonalizacionVisual.DoesNotExist:
            nropag = PerzonalizacionVisual.objects.values('valor').filter(usuario__username="std",
                                                                          tipo="paginacion")
    else:
        nropag = PerzonalizacionVisual.objects.values('valor').filter(usuario__username="std",
                                                                      tipo="paginacion")

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

        search_text = request.POST['search_text']
        if search_text is not None and search_text != u"":
            entry_query = get_query(search_text, ['provincia', 'pais__pais', ])
            lista_provincia = Provincia.objects.filter(entry_query)
        else:
            lista_provincia = Provincia.objects.all()

    paginator = Paginator(lista_provincia, nropag[0]['valor'])

    page = request.GET.get('page')
    try:
        provincias = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        provincias = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        provincias = paginator.page(paginator.num_pages)

    return render_to_response('provincia_lista_search.html', {'lista_provincia': lista_provincia, 'provincias': provincias})


def lista_ciudad(request):
    """docstring"""
    if request.user.id is not None:
        try:
            nropag = PerzonalizacionVisual.objects.values('valor').filter(usuario=
                                                                          request.user.id,
                                                                          tipo="paginacion")
        except PerzonalizacionVisual.DoesNotExist:
            nropag = PerzonalizacionVisual.objects.values('valor').filter(usuario__username="std",
                                                                          tipo="paginacion")
    else:
        nropag = PerzonalizacionVisual.objects.values('valor').filter(usuario__username="std",
                                                                      tipo="paginacion")
    order_by = request.GET.get('order_by')
    if order_by:
        lista_ciudad = Ciudad.objects.all().order_by(order_by)
    else:
        lista_ciudad = Ciudad.objects.all()

    paginator = Paginator(lista_ciudad, nropag[0]['valor'])
    # Show 25 contacts per page
    page = request.GET.get('page')
    if page == '0':
        ciudades = lista_ciudad
    else:
        try:
            ciudades = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            ciudades = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            ciudades = paginator.page(paginator.num_pages)
    context = {'lista_ciudad': lista_ciudad, 'ciudades': ciudades}
    return render(request, 'ciudad_lista.html', context)


def search_ciudad(request):
    """docstring"""
    if request.user.id is not None:
        try:
            nropag = PerzonalizacionVisual.objects.values('valor').filter(usuario=
                                                                          request.user.id,
                                                                          tipo="paginacion")
        except PerzonalizacionVisual.DoesNotExist:
            nropag = PerzonalizacionVisual.objects.values('valor').filter(usuario__username="std",
                                                                          tipo="paginacion")
    else:
        nropag = PerzonalizacionVisual.objects.values('valor').filter(usuario__username="std",
                                                                      tipo="paginacion")
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
        search_text = request.POST['search_text']
        if search_text is not None and search_text != u"":
            entry_query = get_query(search_text, ['ciudad', 'provincia__provincia', 'pais__pais', ])
            lista_ciudad = Ciudad.objects.filter(entry_query)
        else:
            order_by = request.GET.get('order_by')
            if order_by:
                lista_ciudad = Ciudad.objects.all().order_by(order_by)
            else:
                lista_ciudad = Ciudad.objects.all()

    paginator = Paginator(lista_ciudad, nropag[0]['valor'])
    # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        ciudades = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        ciudades = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        ciudades = paginator.page(paginator.num_pages)
    context = {'lista_ciudad': lista_ciudad, 'ciudades': ciudades}
    return render(request, 'ciudad_lista_search.html', context)


def lista_zona(request):
    """docstring"""
    if request.user.id is not None:
        try:
            nropag = PerzonalizacionVisual.objects.values('valor').filter(usuario=
                                                                          request.user.id,
                                                                          tipo="paginacion")
        except PerzonalizacionVisual.DoesNotExist:
            nropag = PerzonalizacionVisual.objects.values('valor').filter(usuario__username="std",
                                                                          tipo="paginacion")
    else:
        nropag = PerzonalizacionVisual.objects.values('valor').filter(usuario__username="std",
                                                                      tipo="paginacion")
    order_by = request.GET.get('order_by')
    if order_by:
        lista_zona = Zona.objects.all().order_by(order_by)
    else:
        lista_zona = Zona.objects.all()

    paginator = Paginator(lista_zona, nropag[0]['valor'])
    # Show 25 contacts per page
    page = request.GET.get('page')

    if page == '0':
        zonas = lista_zona
    else:
        try:
            zonas = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            zonas = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            zonas = paginator.page(paginator.num_pages)
    context = {'lista_zona': lista_zona, 'zonas': zonas}
    return render(request, 'zona_lista.html', context)


def search_zona(request):
    """docstring"""
    if request.user.id is not None:
        try:
            nropag = PerzonalizacionVisual.objects.values('valor').filter(usuario=
                                                                          request.user.id,
                                                                          tipo="paginacion")
        except PerzonalizacionVisual.DoesNotExist:
            nropag = PerzonalizacionVisual.objects.values('valor').filter(usuario__username="std",
                                                                          tipo="paginacion")
    else:
        nropag = PerzonalizacionVisual.objects.values('valor').filter(usuario__username="std",
                                                                      tipo="paginacion")
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
        search_text = request.POST['search_text']
        if search_text is not None and search_text != u"":
            entry_query = get_query(search_text, ['zona', 'ciudad__ciudad', 'provincia__provincia', 'pais__pais', ])
            lista_zona = Zona.objects.filter(entry_query)
        else:
            lista_zona = Zona.objects.all()

    paginator = Paginator(lista_zona, nropag[0]['valor'])
    # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        zonas = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        zonas = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        zonas = paginator.page(paginator.num_pages)
    context = {'lista_zona': lista_zona, 'zonas': zonas}
    return render(request, 'zona_lista_search.html', context)


def lista_tipo_direccion(request):
    """docstring"""
    if request.user.id is not None:
        try:
            nropag = PerzonalizacionVisual.objects.values('valor').filter(usuario=
                                                                          request.user.id,
                                                                          tipo="paginacion")
        except PerzonalizacionVisual.DoesNotExist:
            nropag = PerzonalizacionVisual.objects.values('valor').filter(usuario__username="std",
                                                                          tipo="paginacion")
    else:
        nropag = PerzonalizacionVisual.objects.values('valor').filter(usuario__username="std",
                                                                      tipo="paginacion")
    order_by = request.GET.get('order_by')
    if order_by:
        lista_tipodireccion = Tipo_direccion.objects.all().order_by(order_by)
    else:
        lista_tipodireccion = Tipo_direccion.objects.all()

    paginator = Paginator(lista_tipodireccion, nropag[0]['valor'])
    # Show 25 contacts per page
    page = request.GET.get('page')
    if page == '0':
        tipodirecciones = lista_tipodireccion
    else:
        try:
            tipodirecciones = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            tipodirecciones = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            tipodirecciones = paginator.page(paginator.num_pages)

    context = {'lista_tipodireccion': lista_tipodireccion, 'tipodirecciones': tipodirecciones}
    return render(request, 'tipodireccion_lista.html', context)


def search_tipo_direccion(request):
    """docstring"""
    if request.user.id is not None:
        try:
            nropag = PerzonalizacionVisual.objects.values('valor').filter(usuario=
                                                                          request.user.id,
                                                                          tipo="paginacion")
        except PerzonalizacionVisual.DoesNotExist:
            nropag = PerzonalizacionVisual.objects.values('valor').filter(usuario__username="std",
                                                                          tipo="paginacion")
    else:
        nropag = PerzonalizacionVisual.objects.values('valor').filter(usuario__username="std",
                                                                      tipo="paginacion")
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

        search_text = request.POST['search_text']
        if search_text is not None and search_text != u"":
            entry_query = get_query(search_text, ['tipo_direccion', ])
            lista_tipodireccion = Tipo_direccion.objects.filter(entry_query)
        else:
            lista_tipodireccion = Tipo_direccion.objects.all()

    paginator = Paginator(lista_tipodireccion, nropag[0]['valor'])
    # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        tipodirecciones = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        tipodirecciones = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        tipodirecciones = paginator.page(paginator.num_pages)
    context = {'lista_tipodireccion': lista_tipodireccion, 'tipodirecciones': tipodirecciones}
    return render(request, 'tipodireccion_lista_search.html', context)


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
    return render(request, 'direccion_lista.html', context)


def lista_tipo_inmueble(request):
    """docstring"""
    if request.user.id is not None:
        try:
            nropag = PerzonalizacionVisual.objects.values('valor').filter(usuario=
                                                                          request.user.id,
                                                                          tipo="paginacion")
        except PerzonalizacionVisual.DoesNotExist:
            nropag = PerzonalizacionVisual.objects.values('valor').filter(usuario__username="std",
                                                                          tipo="paginacion")
    else:
        nropag = PerzonalizacionVisual.objects.values('valor').filter(usuario__username="std",
                                                                      tipo="paginacion")
    order_by = request.GET.get('order_by')
    if order_by:
        lista_tipo_inmueble = Tipo_Inmueble.objects.all().order_by(order_by)
    else:
        lista_tipo_inmueble = Tipo_Inmueble.objects.all()

    paginator = Paginator(lista_tipo_inmueble, nropag[0]['valor'])
    # Show 25 contacts per page
    page = request.GET.get('page')
    if page == '0':
        tipoinmuebles = lista_tipo_inmueble
    else:
        try:
            tipoinmuebles = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            tipoinmuebles = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            tipoinmuebles = paginator.page(paginator.num_pages)

    context = {'lista_tipo_inmueble': lista_tipo_inmueble, 'tipoinmuebles': tipoinmuebles}
    return render(request, 'tipo_inmueble_lista.html', context)


def search_tipo_inmueble(request):
    """docstring"""
    if request.user.id is not None:
        try:
            nropag = PerzonalizacionVisual.objects.values('valor').filter(usuario=
                                                                          request.user.id,
                                                                          tipo="paginacion")
        except PerzonalizacionVisual.DoesNotExist:
            nropag = PerzonalizacionVisual.objects.values('valor').filter(usuario__username="std",
                                                                          tipo="paginacion")
    else:
        nropag = PerzonalizacionVisual.objects.values('valor').filter(usuario__username="std",
                                                                      tipo="paginacion")
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

        search_text = request.POST['search_text']
        if search_text is not None and search_text != u"":
            entry_query = get_query(search_text, ['tipo_inmueble', ])
            lista_tipo_inmueble = Tipo_Inmueble.objects.filter(entry_query)
        else:
            lista_tipo_inmueble = Tipo_Inmueble.objects.all()

    paginator = Paginator(lista_tipo_inmueble, nropag[0]['valor'])
    # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        tipoinmuebles = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        tipoinmuebles = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        tipoinmuebles = paginator.page(paginator.num_pages)

    return render_to_response('tipo_inmueble_lista_search.html',
                              {'lista_tipo_inmueble': lista_tipo_inmueble,
                               'tipoinmuebles': tipoinmuebles})


def lista_complejidad_inmueble(request):
    """docstring"""
    if request.user.id is not None:
        try:
            nropag = PerzonalizacionVisual.objects.values('valor').filter(usuario=
                                                                          request.user.id,
                                                                          tipo="paginacion")
        except PerzonalizacionVisual.DoesNotExist:
            nropag = PerzonalizacionVisual.objects.values('valor').filter(usuario__username="std",
                                                                          tipo="paginacion")
    else:
        nropag = PerzonalizacionVisual.objects.values('valor').filter(usuario__username="std",
                                                                      tipo="paginacion")
    order_by = request.GET.get('order_by')
    if order_by:
        lista_complejidad_inmueble = Complejidad_Inmueble.objects.all().order_by(order_by)
    else:
        lista_complejidad_inmueble = Complejidad_Inmueble.objects.all()

    paginator = Paginator(lista_complejidad_inmueble, nropag[0]['valor'])
    # Show 25 contacts per page
    page = request.GET.get('page')
    if page == '0':
        complejidadinmuebles = lista_complejidad_inmueble
    else:
        try:
            complejidadinmuebles = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            complejidadinmuebles = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            complejidadinmuebles = paginator.page(paginator.num_pages)

    context = {'lista_complejidad_inmueble': lista_complejidad_inmueble, 'complejidadinmuebles': complejidadinmuebles}
    return render(request, 'complejidad_inmueble_lista.html', context)


def search_complejidad_inmueble(request):
    """docstring"""
    if request.user.id is not None:
        try:
            nropag = PerzonalizacionVisual.objects.values('valor').filter(usuario=
                                                                          request.user.id,
                                                                          tipo="paginacion")
        except PerzonalizacionVisual.DoesNotExist:
            nropag = PerzonalizacionVisual.objects.values('valor').filter(usuario__username="std",
                                                                          tipo="paginacion")
    else:
        nropag = PerzonalizacionVisual.objects.values('valor').filter(usuario__username="std",
                                                                      tipo="paginacion")
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

        search_text = request.POST['search_text']
        if search_text is not None and search_text != u"":
            entry_query = get_query(search_text, ['complejidad', ])
            lista_complejidad_inmueble = Complejidad_Inmueble.objects.filter(entry_query)
        else:
            lista_complejidad_inmueble = Complejidad_Inmueble.objects.all()

    paginator = Paginator(lista_complejidad_inmueble, nropag[0]['valor'])
    # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        complejidadinmuebles = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        complejidadinmuebles = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        complejidadinmuebles = paginator.page(paginator.num_pages)

    context = {'lista_complejidad_inmueble': lista_complejidad_inmueble,
               'complejidadinmuebles': complejidadinmuebles
               }
    return render_to_response('complejidad_inmueble_lista_search.html', context)


def lista_inmueble(request, iddireccion):
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

    id_direccion = Direccion.objects.get(id=iddireccion)
    lista_inmueble = Inmueble.objects.filter(direccion_id=id_direccion)

    context = {'lista_inmueble': lista_inmueble}
    return render(request, 'inmueble_lista.html', context)


# agregar nuevo
def add_pais(request):
    """docstring"""
    if request.method == 'POST':
        form_pais = PaisForm(request.POST)
        if form_pais.is_valid():
            form_pais.save()
            return HttpResponseRedirect(reverse('udirecciones:lista_pais'))
    else:
        form_pais = PaisForm()
    return render_to_response('pais_add.html',
                              {'form_pais': form_pais, 'create': True},
                              context_instance=RequestContext(request))


def add_provincia(request):
    """docstring"""
    if request.method == 'POST':
        form_provincia = ProvinciaForm(request.POST)
        if form_provincia.is_valid():
            form_provincia.save()
            return HttpResponseRedirect(reverse('udirecciones:lista_provincia'))
    else:
        form_provincia = ProvinciaForm()
    return render_to_response('provincia_add.html',
                              {'form_provincia': form_provincia, 'create': True},
                              context_instance=RequestContext(request))


def add_ciudad(request):
    """docstring"""
    if request.method == 'POST':
        form_ciudad = CiudadForm(request.POST)
        if form_ciudad.is_valid():
            form_ciudad.save()
            return HttpResponseRedirect(reverse('udirecciones:lista_ciudad'))
    else:
        form_ciudad = CiudadForm()
    return render_to_response('ciudad_add.html',
                              {'form_ciudad': form_ciudad, 'create': True},
                              context_instance=RequestContext(request))


def add_zona(request):
    """docstring"""
    if request.method == 'POST':
        form_zona = ZonaForm(request.POST, request.FILES)
        if form_zona.is_valid():
            form_zona.save()
            return HttpResponseRedirect(reverse('udirecciones:lista_zona'))
    else:
        form_zona = ZonaForm()
    return render_to_response('zona_add.html',
                              {'form_zona': form_zona, 'create': True},
                              context_instance=RequestContext(request))


def add_tipo_direccion(request):
    """docstring"""
    if request.method == 'POST':
        form_tipodireccion = TipoDireccionForm(request.POST)
        if form_tipodireccion.is_valid():
            form_tipodireccion.save()
            return HttpResponseRedirect(reverse('udirecciones:lista_tipo_direccion'))
    else:
        form_tipodireccion = TipoDireccionForm()

    return render_to_response('tipodireccion_add.html',
                              {'form_tipodireccion': form_tipodireccion, 'create': True},
                              context_instance=RequestContext(request))


def add_direccion(request, id_cli):
    """docstring"""

    if request.method == 'POST':
        form_direccion = DireccionForm(request.POST)
        if form_direccion.is_valid():
            id_reg = form_direccion.save()
            id_cli = Direccion.objects.get(id=id_reg.id)
            return HttpResponseRedirect(reverse('uclientes:ficha_cliente', args=(id_cli.cliente.id,)))
    else:
        form_direccion = DireccionForm(initial={'cliente': id_cli})

    return render_to_response('direccion_add.html',
                              {'form_direccion': form_direccion, 'create': True},
                              context_instance=RequestContext(request))


def add_tipo_inmueble(request):
    """docstring"""
    if request.method == 'POST':
        form_tipo_inmueble = TipoInmuebleForm(request.POST)
        if form_tipo_inmueble.is_valid():
            form_tipo_inmueble.save()
            return HttpResponseRedirect(reverse('udirecciones:lista_tipo_inmueble'))
    else:
        form_tipo_inmueble = TipoInmuebleForm()

    return render_to_response('tipo_inmueble_add.html',
                              {'form_tipo_inmueble': form_tipo_inmueble, 'create': True},
                              context_instance=RequestContext(request))


def add_complejidad_inmueble(request):
    """docstring"""
    if request.method == 'POST':
        form_complejidad = ComplejidadInmuebleForm(request.POST)
        if form_complejidad.is_valid():
            form_complejidad.save()
            return HttpResponseRedirect(reverse('udirecciones:lista_complejidad_inmueble'))
    else:
        form_complejidad = ComplejidadInmuebleForm()

    return render_to_response('complejidad_inmueble_add.html',
                              {'form_complejidad': form_complejidad, 'create': True},
                              context_instance=RequestContext(request))


def add_inmueble(request):
    """docstring"""
    if request.method == 'POST':
        form_inmueble = InmuebleForm(request.POST)
        if form_inmueble.is_valid():
            id_reg = form_inmueble.save()
            id_di = Inmueble.objects.get(id=id_reg.id)
            return HttpResponseRedirect(reverse('udirecciones:lista_inmueble', args=(id_di.direccion.id,)))
    else:
        form_inmueble = InmuebleForm()

    return render_to_response('inmueble_add.html',
                              {'form_inmueble': form_inmueble, 'create': True},
                              context_instance=RequestContext(request))


# editar registro
def edit_pais(request, pk):
    """docstring"""
    pais = Pais.objects.get(pk=pk)

    redirect_to = request.REQUEST.get('next', '')

    if request.method == 'POST':
        # formulario enviado
        form_edit_pais = PaisForm(request.POST, instance=pais)

        if form_edit_pais.is_valid():
            # formulario validado correctamente
            form_edit_pais.save()

            if redirect_to:
                return HttpResponseRedirect(redirect_to)
            else:
                return HttpResponseRedirect(reverse('udirecciones:lista_pais'))
    else:
        # formulario inicial
        form_edit_pais = PaisForm(instance=pais)

    return render_to_response('pais_edit.html',
                              {'form_edit_pais': form_edit_pais, 'create': False},
                              context_instance=RequestContext(request))


def edit_provincia(request, pk):
    """docstring"""
    provincia = Provincia.objects.get(pk=pk)

    redirect_to = request.REQUEST.get('next', '')

    if request.method == 'POST':
        # formulario enviado
        form_edit_provincia = ProvinciaForm(request.POST, instance=provincia)

        if form_edit_provincia.is_valid():
            # formulario validado correctamente
            form_edit_provincia.save()

            if redirect_to:
                return HttpResponseRedirect(redirect_to)
            else:
                return HttpResponseRedirect(reverse('udirecciones:lista_provincia'))

    else:
        # formulario inicial
        form_edit_provincia = ProvinciaForm(instance=provincia)

    return render_to_response('provincia_edit.html',
                              {'form_edit_provincia': form_edit_provincia, 'create': False},
                              context_instance=RequestContext(request))


def edit_ciudad(request, pk):
    """docstring"""
    ciudad = Ciudad.objects.get(pk=pk)

    redirect_to = request.REQUEST.get('next', '')

    if request.method == 'POST':
        # formulario enviado
        form_edit_ciudad = CiudadForm(request.POST, instance=ciudad)

        if form_edit_ciudad.is_valid():
            # formulario validado correctamente
            form_edit_ciudad.save()

            if redirect_to:
                return HttpResponseRedirect(redirect_to)
            else:

                return HttpResponseRedirect(reverse('udirecciones:lista_ciudad'))

    else:
        # formulario inicial
        form_edit_ciudad = CiudadForm(instance=ciudad)

    return render_to_response('ciudad_edit.html',
                              {'form_edit_ciudad': form_edit_ciudad, 'create': False},
                              context_instance=RequestContext(request))


def edit_zona(request, pk):
    """docstring"""
    zona = Zona.objects.get(pk=pk)

    redirect_to = request.REQUEST.get('next', '')

    if request.method == 'POST':
        # formulario enviado
        form_edit_zona = ZonaForm(request.POST, instance=zona)

        if form_edit_zona.is_valid():
            # formulario validado correctamente
            form_edit_zona.save()

            if redirect_to:
                return HttpResponseRedirect(redirect_to)
            else:
                return HttpResponseRedirect(reverse('udirecciones:lista_zona'))

    else:
        # formulario inicial
        form_edit_zona = ZonaForm(instance=zona)

    return render_to_response('zona_edit.html',
                              {'form_edit_zona': form_edit_zona, 'create': False},
                              context_instance=RequestContext(request))


def edit_tipo_direccion(request, pk):
    """docstring"""
    tipodireccion = Tipo_direccion.objects.get(pk=pk)

    redirect_to = request.REQUEST.get('next', '')

    if request.method == 'POST':
        # formform_tipodireccionulario enviado
        form_edit_tipodireccion = TipoDireccionForm(request.POST, instance=tipodireccion)

        if form_edit_tipodireccion.is_valid():
            # formulario validado correctamente
            form_edit_tipodireccion.save()

            if redirect_to:
                return HttpResponseRedirect(redirect_to)
            else:
                return HttpResponseRedirect(reverse('udirecciones:lista_tipo_direccion'))

    else:
        # formulario inicial
        form_edit_tipodireccion = TipoDireccionForm(instance=tipodireccion)

    return render_to_response('tipodireccion_edit.html',
                              {'form_edit_tipodireccion': form_edit_tipodireccion, 'create': False},
                              context_instance=RequestContext(request))


def edit_direccion(request, pk):
    """docstring"""
    direccion = Direccion.objects.get(pk=pk)

    redirect_to = request.REQUEST.get('next', '')

    if request.method == 'POST':
        # formform_direccionulario enviado
        form_edit_direccion = DireccionForm(request.POST, instance=direccion)

        if form_edit_direccion.is_valid():
            # formulario validado correctamente
            id_reg = form_edit_direccion.save()
            id_cli = Direccion.objects.get(id=id_reg.id)
        if redirect_to:
            return HttpResponseRedirect(redirect_to)
        else:

            #return HttpResponseRedirect(reverse('udirecciones:lista_direccion'))
            return HttpResponseRedirect(reverse('uclientes:ficha_cliente', args=(id_cli.cliente.id,)))

    else:
        # formulario inicial
        form_edit_direccion = DireccionForm(instance=direccion)

    return render_to_response('direccion_edit.html',
                              {'form_edit_direccion': form_edit_direccion, 'create': False},
                              context_instance=RequestContext(request))


def edit_tipo_inmueble(request, pk):
    """docstring"""
    tipo_inmueble = Tipo_Inmueble.objects.get(pk=pk)

    redirect_to = request.REQUEST.get('next', '')

    if request.method == 'POST':
        form_edit_tipo_inmueble = TipoInmuebleForm(request.POST, instance=tipo_inmueble)

        if form_edit_tipo_inmueble.is_valid():
            form_edit_tipo_inmueble.save()

            if redirect_to:
                return HttpResponseRedirect(redirect_to)
            else:
                return HttpResponseRedirect(reverse('udirecciones:lista_tipo_inmueble'))
    else:
        form_edit_tipo_inmueble = TipoInmuebleForm(instance=tipo_inmueble)

    return render_to_response('tipo_inmueble_edit.html',
                              {'form_edit_tipo_inmueble': form_edit_tipo_inmueble, 'tipo_inmueble': tipo_inmueble,
                               'create': True}, context_instance=RequestContext(request))


def edit_complejidad_inmueble(request, pk):
    """docstring"""

    complejidad_inmueble = Complejidad_Inmueble.objects.get(pk=pk)

    if request.method == 'POST':
        form_edit_complejidad_inmueble = ComplejidadInmuebleForm(request.POST, instance=complejidad_inmueble)
        if form_edit_complejidad_inmueble.is_valid():
            form_edit_complejidad_inmueble.save()
            return HttpResponseRedirect(reverse('udirecciones:lista_complejidad_inmueble'))
    else:
        form_edit_complejidad_inmueble = ComplejidadInmuebleForm(instance=complejidad_inmueble)

    return render_to_response('complejidad_inmueble_edit.html',
                              {'form_edit_complejidad_inmueble': form_edit_complejidad_inmueble,
                               'complejidad_inmueble': complejidad_inmueble, 'create': True}, context_instance=RequestContext(request))


def edit_inmueble(request, pk):
    """docstring"""
    inmueble = Inmueble.objects.get(pk=pk)

    redirect_to = request.REQUEST.get('next', '')

    if request.method == 'POST':
        form_edit_inmueble = InmuebleForm(request.POST, instance=inmueble)
        if form_edit_inmueble.is_valid():
            form_edit_inmueble.save()

            if redirect_to:
                return HttpResponseRedirect(redirect_to)
            else:
                return HttpResponseRedirect(reverse('udirecciones:lista_inmueble', args=(inmueble.direccion.id,)))
    else:
        form_edit_inmueble = InmuebleForm(instance=inmueble)

    return render_to_response('inmueble_edit.html',
                              {'form_edit_inmueble': form_edit_inmueble, 'create': True},
                              context_instance=RequestContext(request))
