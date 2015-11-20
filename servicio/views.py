from django.shortcuts import render, render_to_response
from servicio.models import Servicio, Material, \
    Servicio_Material, Complejidad, \
    Complejidad_Servicio, Unidad
from servicio.forms import ServicioForm, MaterialForm,\
    ServicioMaterialForm, ComplejidadForm, \
    ComplejidadServicioForm, UnidadForm
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.core.urlresolvers import reverse
import django.db
import simplejson as json
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count
from mtvmcotizacion.views import get_query
from premisas.models import PerzonalizacionVisual
from django.contrib import messages


# Create your views here.
# lista
def lista_servicio(request):
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

    order_by = request.GET.get('order_by')
    if order_by:
        lista_servicio = Servicio.objects.all().order_by(order_by)
    else:
        lista_servicio = Servicio.objects.all()

    paginator = Paginator(lista_servicio, nropag[0]['valor'])
    # Show 25 contacts per page
    page = request.GET.get('page')
    if page == '0':
        servicios = lista_servicio
    else:
        try:
            servicios = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            servicios = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            servicios = paginator.page(paginator.num_pages)

    context = {'lista_servicio': lista_servicio, 'servicios': servicios}
    return render(request, 'servicio_lista.html', context)


def search_servicio(request):
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

        search_text = request.POST['search_text']
        if search_text is not None and search_text != u"":
            entry_query = get_query(search_text, ['servicio', ])
            lista_servicio = Servicio.objects.filter(entry_query)
        else:
            lista_servicio = Servicio.objects.all()

    paginator = Paginator(lista_servicio, nropag[0]['valor'])
    # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        servicios = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        servicios = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        servicios = paginator.page(paginator.num_pages)

    context = {'lista_servicio': lista_servicio, 'servicios': servicios}
    return render_to_response('servicio_lista_search.html', context)


def lista_unidad(request):
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
                id_unidad = request.POST['item_id']
                p = Unidad.objects.get(pk=id_unidad)
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
    order_by = request.GET.get('order_by')
    if order_by:
        lista_unidad = Unidad.objects.all().order_by(order_by)
    else:
        lista_unidad = Unidad.objects.all()

    paginator = Paginator(lista_unidad, nropag[0]['valor'])
    # Show 25 contacts per page
    page = request.GET.get('page')
    if page == '0':
        unidades = lista_unidad
    else:
        try:
            unidades = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            unidades = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            unidades = paginator.page(paginator.num_pages)

    context = {'lista_unidad': lista_unidad, 'unidades': unidades}
    return render(request, 'unidad_lista.html', context)


def search_unidad(request):
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
                id_unidad = request.POST['item_id']
                p = Unidad.objects.get(pk=id_unidad)
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
            entry_query = get_query(search_text, ['unidad', ])
            lista_unidad = Unidad.objects.filter(entry_query)
        else:
            lista_unidad = Unidad.objects.all()

    paginator = Paginator(lista_unidad, nropag[0]['valor'])
    # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        unidades = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        unidades = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        unidades = paginator.page(paginator.num_pages)

    context = {'lista_unidad': lista_unidad, 'unidades': unidades}
    return render_to_response('unidad_lista_search.html', context)


def lista_material(request):
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
    order_by = request.GET.get('order_by')
    if order_by:
        lista_material = Material.objects.all().order_by(order_by)
    else:
        lista_material = Material.objects.all()

    paginator = Paginator(lista_material, nropag[0]['valor'])
    # Show 25 contacts per page
    page = request.GET.get('page')
    if page == '0':
        materiales = lista_material
    else:
        try:
            materiales = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            materiales = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            materiales = paginator.page(paginator.num_pages)

    context = {'lista_material': lista_material, 'materiales': materiales}
    return render(request, 'material_lista.html', context)


def search_material(request):
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

        search_text = request.POST['search_text']
        contenedor = request.POST['contenedor']
        if search_text is not None and search_text != u"":
            entry_query = get_query(search_text, ['material', ])
            if contenedor is not None and contenedor != u"":
                lista_material = Material.objects.filter(entry_query, contenedor=True)
            else:
                lista_material = Material.objects.filter(entry_query)

        else:
            if contenedor is not None and contenedor != u"":
                lista_material = Material.objects.filter(contenedor=True)
            else:
                lista_material = Material.objects.all()

    paginator = Paginator(lista_material, nropag[0]['valor'])
    # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        materiales = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        materiales = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        materiales = paginator.page(paginator.num_pages)

    context = {'lista_material': lista_material, 'materiales': materiales}
    return render_to_response('material_lista_search.html', context)


def lista_contenedor(request):
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

    order_by = request.GET.get('order_by')
    if order_by:
        lista_material = Material.objects.filter(contenedor=True).order_by(order_by)
    else:
        lista_material = Material.objects.filter(contenedor=True)

    paginator = Paginator(lista_material, nropag[0]['valor'])
    # Show 25 contacts per page
    page = request.GET.get('page')
    if page == '0':
        materiales = lista_material
    else:
        try:
            materiales = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            materiales = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            materiales = paginator.page(paginator.num_pages)

    context = {'lista_material': lista_material,
               'materiales': materiales,
               'contenedor': 'contenedor'}
    return render(request, 'material_lista.html', context)


def lista_complejidad(request):
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
    order_by = request.GET.get('order_by')
    if order_by:
        lista_complejidad = Complejidad.objects.all().order_by(order_by)
    else:
        lista_complejidad = Complejidad.objects.all()

    paginator = Paginator(lista_complejidad, nropag[0]['valor'])
    # Show 25 contacts per page
    page = request.GET.get('page')
    if page == '0':
        complejidades = lista_complejidad
    else:
        try:
            complejidades = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            complejidades = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            complejidades = paginator.page(paginator.num_pages)

    context = {'lista_complejidad': lista_complejidad,
               'complejidades': complejidades}
    return render(request, 'complejidad_lista.html', context)


def search_complejidad(request):
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

        search_text = request.POST['search_text']
        if search_text is not None and search_text != u"":
            entry_query = get_query(search_text, ['descripcion', ])
            lista_complejidad = Complejidad.objects.filter(entry_query)
        else:
            lista_complejidad = Complejidad.objects.all()

    paginator = Paginator(lista_complejidad, nropag[0]['valor'])
    # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        complejidades = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        complejidades = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        complejidades = paginator.page(paginator.num_pages)

    context = {'lista_complejidad': lista_complejidad,
               'complejidades': complejidades}
    return render_to_response('complejidad_lista_search.html', context)


def buscar_servicio_material(request, idserv=0, idmat=0):
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

    if int(idmat) != 0 | int(idserv) != 0:

        buscar_serviciomaterial = Servicio_Material.objects.filter(Q(material=idmat) | Q(servicio=idserv))
        lista_servicio = Servicio.objects.all()
    else:
        buscar_serviciomaterial = Servicio_Material.objects.all()
        lista_servicio = Servicio.objects.all()

    lista_servicio = Servicio.objects.all()
    paginator = Paginator(lista_servicio, nropag[0]['valor'])
    # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        servicios = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        servicios = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        servicios = paginator.page(paginator.num_pages)

    context = {'buscar_serviciomaterial': buscar_serviciomaterial,
               'servicios': servicios,
               'lista_servicio': lista_servicio}
    return render(request, 'serviciomaterial_lista.html', context)


def buscar_complejidad_servicio(request, idserv=0, idcomp=0):
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

    if int(idcomp) != 0 | int(idserv) != 0:

        buscar_complejidadservicio = Complejidad_Servicio.objects.filter(Q(complejidad=idcomp) | Q(servicio=idserv))
        listar_servicios = Complejidad_Servicio.objects.filter(Q(complejidad=idcomp) | Q(servicio=idserv)).values('servicio', 'servicio__servicio').annotate(tcount=Count('servicio')).order_by('servicio')
    else:
        buscar_complejidadservicio = Complejidad_Servicio.objects.all()
        listar_servicios = Complejidad_Servicio.objects.values('servicio', 'servicio__servicio').annotate(tcount=Count('servicio')).order_by('servicio')

    paginator = Paginator(listar_servicios, nropag[0]['valor'])
    # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        servicios = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        servicios = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        servicios = paginator.page(paginator.num_pages)

    context = {'buscar_complejidadservicio': buscar_complejidadservicio,
               'servicios': servicios,
               'listar_servicios': listar_servicios,
               'idserv': idserv}
    return render(request, 'complejidadservicio_lista.html', context)


# agregar nuevo
def add_servicio(request):
    """docstring"""
    if request.method == 'POST':
        form_servicio = ServicioForm(request.POST)
        if form_servicio.is_valid():
            id_reg = form_servicio.save()
            if 'regEdit' in request.POST:
                messages.success(request, "Registro guardado.")
                return HttpResponseRedirect(reverse('uservicios:edit_servicio',
                                                    args=(id_reg.id,)))
            else:
                return HttpResponseRedirect(reverse('uservicios:lista_servicio'))
    else:
        form_servicio = ServicioForm()
    return render_to_response('servicio_add.html',
                              {'form_servicio': form_servicio, 'create': True},
                              context_instance=RequestContext(request))


def add_unidad(request):
    """docstring"""
    if request.method == 'POST':
        form_unidad = UnidadForm(request.POST)
        if form_unidad.is_valid():
            id_reg = form_unidad.save()
            if 'regEdit' in request.POST:
                messages.success(request, "Registro guardado.")
                return HttpResponseRedirect(reverse('uservicios:edit_unidad',
                                                    args=(id_reg.id,)))
            else:
                return HttpResponseRedirect(reverse('uservicios:lista_unidad'))
    else:
        form_unidad = UnidadForm()
    return render_to_response('unidad_add.html',
                              {'form_unidad': form_unidad, 'create': True},
                              context_instance=RequestContext(request))


def add_material(request):
    """docstring"""
    if request.method == 'POST':
        form_material = MaterialForm(request.POST)
        if form_material.is_valid():
            id_reg = form_material.save()
            if 'regEdit' in request.POST:
                messages.success(request, "Registro guardado.")
                return HttpResponseRedirect(reverse('uservicios:edit_material',
                                                    args=(id_reg.id,)))
            else:
                return HttpResponseRedirect(reverse('uservicios:lista_material'))
    else:
        form_material = MaterialForm()
    return render_to_response('material_add.html',
                              {'form_material': form_material, 'create': True},
                              context_instance=RequestContext(request))


def add_complejidad(request):
    """docstring"""
    if request.method == 'POST':
        form_complejidad = ComplejidadForm(request.POST)
        if form_complejidad.is_valid():
            id_reg = form_complejidad.save()
            if 'regEdit' in request.POST:
                messages.success(request, "Registro guardado.")
                return HttpResponseRedirect(reverse('uservicios:edit_complejidad',
                                                    args=(id_reg.id,)))
            else:
                return HttpResponseRedirect(reverse('uservicios:lista_complejidad'))
    else:
        form_complejidad = ComplejidadForm()
    return render_to_response('complejidad_add.html',
                              {'form_complejidad': form_complejidad, 'create': True},
                              context_instance=RequestContext(request))


def add_serviciomaterial(request, id_ser):
    """docstring"""
    if request.method == 'POST':
        form_serviciomaterial = ServicioMaterialForm(request.POST)
        if form_serviciomaterial.is_valid():
            id_reg = form_serviciomaterial.save()
            if 'regEdit' in request.POST:
                messages.success(request, "Registro guardado.")
                return HttpResponseRedirect(reverse('uservicios:servicio_material',
                                                    args=(id_reg.id,)))
            else:
                return HttpResponseRedirect(reverse('uservicios:buscar_servicio_material',
                                                    args=('0', '0')))
    else:
        form_serviciomaterial = ServicioMaterialForm(initial={'servicio': id_ser})
    return render_to_response('serviciomaterial_add.html',
                              {'form_serviciomaterial': form_serviciomaterial,
                               'create': True},
                              context_instance=RequestContext(request))


def add_complejidadservicio(request, id_ser):
    """docstring"""
    if request.method == 'POST':
        form_complejidadservicio = ComplejidadServicioForm(request.POST)
        if form_complejidadservicio.is_valid():
            id_reg = form_complejidadservicio.save()
            if 'regEdit' in request.POST:
                messages.success(request, "Registro guardado.")
                return HttpResponseRedirect(reverse('uservicios:edit_complejidadservicio',
                                                    args=(id_reg.id,)))
            else:
                return HttpResponseRedirect(reverse('uservicios:buscar_complejidad_servicio',
                                                    args=(id_ser, '0')))
    else:
        form_complejidadservicio = ComplejidadServicioForm(initial={'servicio': id_ser})
    return render_to_response('complejidadservicio_add.html',
                              {'form_complejidadservicio': form_complejidadservicio,
                               'create': True},
                              context_instance=RequestContext(request))


# editar registro
def edit_servicio(request, pk):
    """docstring"""
    servicio = Servicio.objects.get(pk=pk)

    redirect_to = request.REQUEST.get('next', '')

    if request.method == 'POST':
        # formulario enviado
        form_edit_servicio = ServicioForm(request.POST, instance=servicio)

        if form_edit_servicio.is_valid():
            # formulario validado correctamente
            form_edit_servicio.save()
            if 'regEdit' in request.POST:
                messages.success(request, "Registro guardado.")
                return HttpResponseRedirect(request.get_full_path())

            else:
                if redirect_to:
                    return HttpResponseRedirect(redirect_to)
                else:
                    return HttpResponseRedirect(reverse('uservicios:lista_servicio'))

    else:
        # formulario inicial
        form_edit_servicio = ServicioForm(instance=servicio)

    return render_to_response('servicio_edit.html',
                              {'form_edit_servicio': form_edit_servicio,
                               'servicio': servicio, 'create': False},
                              context_instance=RequestContext(request))


def edit_unidad(request, pk):
    """docstring"""
    unidad = Unidad.objects.get(pk=pk)

    redirect_to = request.REQUEST.get('next', '')

    if request.method == 'POST':
        # formulario enviado
        form_edit_unidad = UnidadForm(request.POST, instance=unidad)

        if form_edit_unidad.is_valid():
            # formulario validado correctamente
            form_edit_unidad.save()
            if 'regEdit' in request.POST:
                messages.success(request, "Registro guardado.")
                return HttpResponseRedirect(request.get_full_path())

            else:
                if redirect_to:
                    return HttpResponseRedirect(redirect_to)
                else:
                    return HttpResponseRedirect(reverse('uservicios:lista_unidad'))

    else:
        # formulario inicial
        form_edit_unidad = UnidadForm(instance=unidad)

    return render_to_response('unidad_edit.html',
                              {'form_edit_unidad': form_edit_unidad,
                               'unidad': unidad, 'create': False},
                              context_instance=RequestContext(request))


def edit_material(request, pk):
    """docstring"""
    material = Material.objects.get(pk=pk)

    redirect_to = request.REQUEST.get('next', '')

    if request.method == 'POST':
        # formulario enviado
        form_edit_material = MaterialForm(request.POST, instance=material)

        if form_edit_material.is_valid():
            # formulario validado correctamente
            form_edit_material.save()
            if 'regEdit' in request.POST:
                messages.success(request, "Registro guardado.")
                return HttpResponseRedirect(request.get_full_path())

            else:
                if redirect_to:
                    return HttpResponseRedirect(redirect_to)
                else:
                    return HttpResponseRedirect(reverse('uservicios:lista_material'))

    else:
        # formulario inicial
        form_edit_material = MaterialForm(instance=material)

    return render_to_response('material_edit.html',
                              {'form_edit_material': form_edit_material,
                               'material': material, 'create': False},
                              context_instance=RequestContext(request))


def edit_complejidad(request, pk):
    """docstring"""
    complejidad = Complejidad.objects.get(pk=pk)

    redirect_to = request.REQUEST.get('next', '')

    if request.method == 'POST':
        # formulario enviado
        form_edit_complejidad = ComplejidadForm(request.POST, instance=complejidad)

        if form_edit_complejidad.is_valid():
            # formulario validado correctamente
            form_edit_complejidad.save()
            if 'regEdit' in request.POST:
                messages.success(request, "Registro guardado.")
                return HttpResponseRedirect(request.get_full_path())

            else:
                if redirect_to:
                    return HttpResponseRedirect(redirect_to)
                else:
                    return HttpResponseRedirect(reverse('uservicios:lista_complejidad'))

    else:
        # formulario inicial
        form_edit_complejidad = ComplejidadForm(instance=complejidad)

    return render_to_response('complejidad_edit.html',
                              {'form_edit_complejidad': form_edit_complejidad,
                               'complejidad': complejidad, 'create': False},
                              context_instance=RequestContext(request))


def edit_complejidadservicio(request, pk):
    """docstring"""
    complejidadservicio = Complejidad_Servicio.objects.get(pk=pk)

    redirect_to = request.REQUEST.get('next', '')

    if request.method == 'POST':
        # formulario enviado
        form_edit_complejidadservicio = ComplejidadServicioForm(request.POST,
                                                                instance=complejidadservicio)

        if form_edit_complejidadservicio.is_valid():
            # formulario validado correctamente
            form_edit_complejidadservicio.save()

            if 'regEdit' in request.POST:
                messages.success(request, "Registro guardado.")
                return HttpResponseRedirect(request.get_full_path())

            else:
                if redirect_to:
                    return HttpResponseRedirect(redirect_to)
                else:
                    return HttpResponseRedirect(reverse('uservicios:buscar_complejidad_servicio',
                                                        args=(complejidadservicio.servicio.id, 0,)))

    else:
        # formulario inicial
        form_edit_complejidadservicio = ComplejidadServicioForm(instance=complejidadservicio)

    return render_to_response('complejidadservicio_edit.html',
                              {'form_edit_complejidadservicio': form_edit_complejidadservicio,
                               'create': False},
                              context_instance=RequestContext(request))


def edit_serviciomaterial(request, pk):
    """docstring"""
    serviciomaterial = Servicio_Material.objects.get(pk=pk)

    redirect_to = request.REQUEST.get('next', '')

    if request.method == 'POST':
        # formulario enviado
        form_edit_serviciomaterial = ServicioMaterialForm(request.POST,
                                                          instance=serviciomaterial)

        if form_edit_serviciomaterial.is_valid():
            # formulario validado correctamente
            form_edit_serviciomaterial.save()
            if 'regEdit' in request.POST:
                messages.success(request, "Registro guardado.")
                return HttpResponseRedirect(request.get_full_path())
            else:
                if redirect_to:
                    return HttpResponseRedirect(redirect_to)
                else:
                    return HttpResponseRedirect(reverse('uservicios:buscar_servicio_material',
                                                        args=(serviciomaterial.servicio.id, 0,)))

    else:
        # formulario inicial
        form_edit_serviciomaterial = ServicioMaterialForm(instance=serviciomaterial)

    return render_to_response('serviciomaterial_edit.html',
                              {'form_edit_serviciomaterial': form_edit_serviciomaterial,
                               'create': False},
                              context_instance=RequestContext(request))
