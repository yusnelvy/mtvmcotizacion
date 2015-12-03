"""docstring"""

from django.shortcuts import render, render_to_response
from mueble.models import Tipo_Mueble, Ocupacion,\
    Forma_Mueble, Mueble, Tamano, Tamano_Mueble, \
    Mueble_Ambiente, Densidad
from mueble.forms import TipoMuebleForm, OcupacionForm,\
    FormaMuebleForm, MuebleForm, TamanoForm, \
    TamanoMuebleForm, MuebleAmbienteForm, DensidadForm
from ambiente.models import Ambiente
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
import simplejson as json
import django.db
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView, View
from django.views.generic.detail import DetailView
from django.db.models import Count
from mtvmcotizacion.views import get_query
from premisas.models import PerzonalizacionVisual
from django.forms.formsets import formset_factory
from django.contrib import messages


def lista_mueble(request):
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
                id_mueble = request.POST['item_id']
                p = Mueble.objects.get(pk=id_mueble)
                mensaje = {"status": "True", "item_id": p.id, "form": "del"}
                p.delete()

                 # Elinamos objeto de la base de datos
                messages.success(request, "Se elimino el registro.")
                return HttpResponse(json.dumps(mensaje), content_type='application/json')

            except django.db.IntegrityError:

                mensaje = {"status": "False",
                           "form": "del",
                           "msj": "No se puede eliminar porque tiene algun registro asociado"}
                messages.success(request, "No se puede eliminar porque tiene algun registro asociado")
                return HttpResponse(json.dumps(mensaje), content_type='application/json')

            except:
                mensaje = {"status": "False", "form": "del", "msj": "Error al eliminar"}
                messages.success(request, "Error al eliminar")

                return HttpResponse(json.dumps(mensaje), content_type='application/json')
    order_by = request.GET.get('order_by')
    if order_by:
        lista_mueble = Mueble.objects.all().order_by(order_by)
    else:
        lista_mueble = Mueble.objects.all()

    paginator = Paginator(lista_mueble, nropag[0]['valor'])
    # Show 25 contacts per page
    page = request.GET.get('page')
    if page == '0':
        muebles = lista_mueble
    else:
        try:
            muebles = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            muebles = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            muebles = paginator.page(paginator.num_pages)
    context = {'lista_mueble': lista_mueble, 'muebles': muebles}
    return render(request, 'mueble_lista.html', context)


def search_mueble(request):
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
                id_mueble = request.POST['item_id']
                p = Mueble.objects.get(pk=id_mueble)
                mensaje = {"status": "True", "item_id": p.id, "form": "del"}
                p.delete()

                 # Elinamos objeto de la base de datos
                messages.success(request, "Se elimino el registro.")
                return HttpResponse(json.dumps(mensaje), content_type='application/json')

            except django.db.IntegrityError:

                mensaje = {"status": "False", "form": "del",
                           "msj": "No se puede eliminar porque tiene algun registro asociado"}
                messages.success(request, "No se puede eliminar porque tiene algun registro asociado")
                return HttpResponse(json.dumps(mensaje), content_type='application/json')

            except:
                mensaje = {"status": "False", "form": "del", "msj": "Error al eliminar"}
                messages.success(request, "Error al eliminar")
                return HttpResponse(json.dumps(mensaje), content_type='application/json')

        search_text = request.POST['search_text']
        if search_text is not None and search_text != u"":
            entry_query = get_query(search_text, ['mueble',
                                                  'tipo_mueble__tipo_mueble',
                                                  'forma__forma'])
            lista_mueble = Mueble.objects.filter(entry_query)
        else:
            lista_mueble = Mueble.objects.all()

    paginator = Paginator(lista_mueble, nropag[0]['valor'])
    # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        muebles = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        muebles = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        muebles = paginator.page(paginator.num_pages)
    context = {'lista_mueble': lista_mueble, 'muebles': muebles}
    return render_to_response('mueble_lista_search.html', context)


def buscar_mueble(request, idtipomueble):
    """docstring"""

    tipomueble = Tipo_Mueble.objects.get(id=idtipomueble)

    buscar_muebleambiente = Mueble.objects.filter(tipo_mueble_id=tipomueble)
    context = {'buscar_muebleambiente': buscar_muebleambiente}
    return render(request, 'mueble_buscar.html', context)


def add_mueble(request):
    """docstring"""
    if request.method == 'POST':
        form_mueble = MuebleForm(request.POST)
        if form_mueble.is_valid():
            id_reg = form_mueble.save()
            if 'regEdit' in request.POST:
                messages.success(request, "Registro guardado.")
                return HttpResponseRedirect(reverse('umuebles:edit_mueble',
                                                    args=(id_reg.id,)))
            else:
                return HttpResponseRedirect(reverse('umuebles:lista_mueble'))
    else:
        form_mueble = MuebleForm()
    return render_to_response('mueble_add.html',
                              {'form_mueble': form_mueble, 'create': True},
                              context_instance=RequestContext(request))


def edit_mueble(request, pk):
    """docstring"""
    mueble = Mueble.objects.get(pk=pk)

    redirect_to = request.REQUEST.get('next', '../../')

    if request.method == 'POST':
        # formulario enviado
        form_edit_mueble = MuebleForm(request.POST, instance=mueble)

        if form_edit_mueble.is_valid():
            # formulario validado correctamente
            form_edit_mueble.save()
            if 'regEdit' in request.POST:
                messages.success(request, "Registro guardado.")
                return HttpResponseRedirect(request.get_full_path())

            else:
                if redirect_to:
                    return HttpResponseRedirect(redirect_to)
                else:
                    return HttpResponseRedirect(reverse('umuebles:lista_mueble'))

    else:
        # formulario inicial
        form_edit_mueble = MuebleForm(instance=mueble)

    return render_to_response('mueble_edit.html',
                              {'form_edit_mueble': form_edit_mueble,
                               'mueble': mueble,
                               'create': False},
                              context_instance=RequestContext(request))


def lista_tipo_mueble(request):
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
                id_tipomueble = request.POST['item_id']
                p = Tipo_Mueble.objects.get(pk=id_tipomueble)
                mensaje = {"status": "True", "item_id": p.id, "form": "del"}
                p.delete()

                 # Elinamos objeto de la base de datos
                messages.success(request, "Se elimino el registro.")
                return HttpResponse(json.dumps(mensaje), content_type='application/json')

            except django.db.IntegrityError:

                mensaje = {"status": "False", "form": "del",
                           "msj": "No se puede eliminar porque tiene algun registro asociado"}
                messages.success(request, "No se puede eliminar porque tiene algun registro asociado")
                return HttpResponse(json.dumps(mensaje), content_type='application/json')

            except:
                mensaje = {"status": "False", "form": "del", "msj": "Error al eliminar"}
                messages.success(request, "Error al eliminar")
                return HttpResponse(json.dumps(mensaje), content_type='application/json')
    order_by = request.GET.get('order_by')
    if order_by:
        lista_tipomueble = Tipo_Mueble.objects.all().order_by(order_by)
    else:
        lista_tipomueble = Tipo_Mueble.objects.all()

    paginator = Paginator(lista_tipomueble, nropag[0]['valor'])
    # Show 25 contacts per page
    page = request.GET.get('page')
    if page == '0':
        tipomuebles = lista_tipomueble
    else:
        try:
            tipomuebles = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            tipomuebles = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            tipomuebles = paginator.page(paginator.num_pages)

    context = {'lista_tipomueble': lista_tipomueble, 'tipomuebles': tipomuebles}
    return render(request, 'tipomueble_lista.html', context)


def search_tipo_mueble(request):
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
                id_tipomueble = request.POST['item_id']
                p = Tipo_Mueble.objects.get(pk=id_tipomueble)
                mensaje = {"status": "True", "item_id": p.id, "form": "del"}
                p.delete()

                 # Elinamos objeto de la base de datos
                messages.success(request, "Se elimino el registro.")
                return HttpResponse(json.dumps(mensaje), content_type='application/json')

            except django.db.IntegrityError:

                mensaje = {"status": "False", "form": "del",
                           "msj": "No se puede eliminar porque tiene algun registro asociado"}
                messages.success(request, "No se puede eliminar porque tiene algun registro asociado")
                return HttpResponse(json.dumps(mensaje), content_type='application/json')

            except:
                mensaje = {"status": "False", "form": "del", "msj": "Error al eliminar"}
                messages.success(request, "Error al eliminar")
                return HttpResponse(json.dumps(mensaje), content_type='application/json')

        search_text = request.POST['search_text']
        if search_text is not None and search_text != u"":
            entry_query = get_query(search_text, ['tipo_mueble', ])
            lista_tipomueble = Tipo_Mueble.objects.filter(entry_query)
        else:
            lista_tipomueble = Tipo_Mueble.objects.all()

    paginator = Paginator(lista_tipomueble, nropag[0]['valor'])
    # Show 25 contacts per page
    page = request.GET.get('page')
    if page == '0':
        tipomuebles = lista_tipomueble
    else:
        try:
            tipomuebles = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            tipomuebles = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            tipomuebles = paginator.page(paginator.num_pages)

    context = {'lista_tipomueble': lista_tipomueble, 'tipomuebles': tipomuebles}
    return render_to_response('tipomueble_lista_search.html', context)


def lista_ocupacion(request):
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
                id_ocupacion = request.POST['item_id']
                p = Ocupacion.objects.get(pk=id_ocupacion)
                mensaje = {"status": "True", "item_id": p.id, "form": "del"}
                p.delete()

                 # Elinamos objeto de la base de datos
                messages.success(request, "Se elimino el registro.")
                return HttpResponse(json.dumps(mensaje), content_type='application/json')

            except django.db.IntegrityError:

                mensaje = {"status": "False", "form": "del",
                           "msj": "No se puede eliminar porque tiene algun registro asociado"}
                messages.success(request, "No se puede eliminar porque tiene algun registro asociado")
                return HttpResponse(json.dumps(mensaje), content_type='application/json')

            except:
                mensaje = {"status": "False", "form": "del", "msj": "Error al eliminar"}
                messages.success(request, "Error al eliminar")
                return HttpResponse(json.dumps(mensaje), content_type='application/json')
    order_by = request.GET.get('order_by')
    if order_by:
        lista_ocupacion = Ocupacion.objects.all().order_by(order_by)
    else:
        lista_ocupacion = Ocupacion.objects.all()

    paginator = Paginator(lista_ocupacion, nropag[0]['valor'])
    # Show 25 contacts per page
    page = request.GET.get('page')
    if page == '0':
        ocupaciones = lista_ocupacion
    else:
        try:
            ocupaciones = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            ocupaciones = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            ocupaciones = paginator.page(paginator.num_pages)
    context = {'lista_ocupacion': lista_ocupacion, 'ocupaciones': ocupaciones}
    return render(request, 'ocupacion_lista.html', context)


def search_ocupacion(request):
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
                id_ocupacion = request.POST['item_id']
                p = Ocupacion.objects.get(pk=id_ocupacion)
                mensaje = {"status": "True", "item_id": p.id, "form": "del"}
                p.delete()

                 # Elinamos objeto de la base de datos
                messages.success(request, "Se elimino el registro.")
                return HttpResponse(json.dumps(mensaje), content_type='application/json')

            except django.db.IntegrityError:

                mensaje = {"status": "False", "form": "del",
                           "msj": "No se puede eliminar porque tiene algun registro asociado"}
                messages.success(request, "No se puede eliminar porque tiene algun registro asociado")
                return HttpResponse(json.dumps(mensaje), content_type='application/json')

            except:
                mensaje = {"status": "False", "form": "del", "msj": "Error al eliminar"}
                messages.success(request, "Error al eliminar")
                return HttpResponse(json.dumps(mensaje), content_type='application/json')

        search_text = request.POST['search_text']
        if search_text is not None and search_text != u"":
            entry_query = get_query(search_text, ['descripcion', ])
            lista_ocupacion = Ocupacion.objects.filter(entry_query)
        else:
            lista_ocupacion = Ocupacion.objects.all()

    paginator = Paginator(lista_ocupacion, nropag[0]['valor'])
    # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        ocupaciones = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        ocupaciones = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        ocupaciones = paginator.page(paginator.num_pages)

    context = {'lista_ocupacion': lista_ocupacion, 'ocupaciones': ocupaciones}
    return render_to_response('ocupacion_lista_search.html', context)


def lista_forma_mueble(request):
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
                id_formamueble = request.POST['item_id']
                p = Forma_Mueble.objects.get(pk=id_formamueble)
                mensaje = {"status": "True", "item_id": p.id, "form": "del"}
                p.delete()

                 # Elinamos objeto de la base de datos
                messages.success(request, "Se elimino el registro.")
                return HttpResponse(json.dumps(mensaje), content_type='application/json')

            except django.db.IntegrityError:

                mensaje = {"status": "False", "form": "del",
                           "msj": "No se puede eliminar porque tiene algun registro asociado"}
                messages.success(request, "No se puede eliminar porque tiene algun registro asociado")
                return HttpResponse(json.dumps(mensaje), content_type='application/json')

            except:
                mensaje = {"status": "False", "form": "del", "msj": "Error al eliminar"}
                messages.success(request, "Error al eliminar")
                return HttpResponse(json.dumps(mensaje), content_type='application/json')
    order_by = request.GET.get('order_by')
    if order_by:
        lista_formamueble = Forma_Mueble.objects.all().order_by(order_by)
    else:
        lista_formamueble = Forma_Mueble.objects.all()

    paginator = Paginator(lista_formamueble, nropag[0]['valor'])
    # Show 25 contacts per page
    page = request.GET.get('page')
    if page == '0':
        formamuebles = lista_formamueble
    else:
        try:
            formamuebles = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            formamuebles = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            formamuebles = paginator.page(paginator.num_pages)

    context = {'lista_formamueble': lista_formamueble, 'formamuebles': formamuebles}
    return render(request, 'formamueble_lista.html', context)


def search_forma_mueble(request):
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
                id_formamueble = request.POST['item_id']
                p = Forma_Mueble.objects.get(pk=id_formamueble)
                mensaje = {"status": "True", "item_id": p.id, "form": "del"}
                p.delete()

                 # Elinamos objeto de la base de datos
                messages.success(request, "Se elimino el registro.")
                return HttpResponse(json.dumps(mensaje), content_type='application/json')

            except django.db.IntegrityError:

                mensaje = {"status": "False", "form": "del",
                           "msj": "No se puede eliminar porque tiene algun registro asociado"}
                messages.success(request, "No se puede eliminar porque tiene algun registro asociado")
                return HttpResponse(json.dumps(mensaje), content_type='application/json')

            except:
                mensaje = {"status": "False", "form": "del", "msj": "Error al eliminar"}
                messages.success(request, "Error al eliminar")
                return HttpResponse(json.dumps(mensaje), content_type='application/json')

        search_text = request.POST['search_text']
        if search_text is not None and search_text != u"":
            entry_query = get_query(search_text, ['forma', ])
            lista_formamueble = Forma_Mueble.objects.filter(entry_query)
        else:
            lista_formamueble = Forma_Mueble.objects.all()

    paginator = Paginator(lista_formamueble, nropag[0]['valor'])
    # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        formamuebles = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        formamuebles = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        formamuebles = paginator.page(paginator.num_pages)

    context = {'lista_formamueble': lista_formamueble, 'formamuebles': formamuebles}

    return render_to_response('formamueble_lista_search.html', context)


def lista_tamano(request):
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
                id_tamano = request.POST['item_id']
                p = Tamano.objects.get(pk=id_tamano)
                mensaje = {"status": "True", "item_id": p.id, "form": "del"}
                p.delete()

                 # Elinamos objeto de la base de datos
                messages.success(request, "Se elimino el registro.")
                return HttpResponse(json.dumps(mensaje), content_type='application/json')

            except django.db.IntegrityError:

                mensaje = {"status": "False", "form": "del",
                           "msj": "No se puede eliminar porque tiene algun registro asociado"}
                messages.success(request, "No se puede eliminar porque tiene algun registro asociado")
                return HttpResponse(json.dumps(mensaje), content_type='application/json')

            except:
                mensaje = {"status": "False", "form": "del", "msj": "Error al eliminar"}
                messages.success(request, "Error al eliminar")
                return HttpResponse(json.dumps(mensaje), content_type='application/json')
    order_by = request.GET.get('order_by')
    if order_by:
        lista_tamano = Tamano.objects.all().order_by(order_by)
    else:
        lista_tamano = Tamano.objects.all()

    paginator = Paginator(lista_tamano, nropag[0]['valor'])
    # Show 25 contacts per page
    page = request.GET.get('page')
    if page == '0':
        tamanos = lista_tamano
    else:
        try:
            tamanos = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            tamanos = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            tamanos = paginator.page(paginator.num_pages)

    context = {'lista_tamano': lista_tamano, 'tamanos': tamanos}
    return render(request, 'tamano_lista.html', context)


def search_tamano(request):
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
                id_tamano = request.POST['item_id']
                p = Tamano.objects.get(pk=id_tamano)
                mensaje = {"status": "True", "item_id": p.id, "form": "del"}
                p.delete()

                 # Elinamos objeto de la base de datos
                messages.success(request, "Se elimino el registro.")
                return HttpResponse(json.dumps(mensaje), content_type='application/json')

            except django.db.IntegrityError:

                mensaje = {"status": "False", "form": "del",
                           "msj": "No se puede eliminar porque tiene algun registro asociado"}
                messages.success(request, "No se puede eliminar porque tiene algun registro asociado")
                return HttpResponse(json.dumps(mensaje), content_type='application/json')

            except:
                mensaje = {"status": "False", "form": "del", "msj": "Error al eliminar"}
                messages.success(request, "Error al eliminar")
                return HttpResponse(json.dumps(mensaje), content_type='application/json')

        search_text = request.POST['search_text']
        if search_text is not None and search_text != u"":
            entry_query = get_query(search_text, ['descripcion', ])
            lista_tamano = Tamano.objects.filter(entry_query)
        else:
            lista_tamano = Tamano.objects.all()

    paginator = Paginator(lista_tamano, nropag[0]['valor'])
    # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        tamanos = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        tamanos = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        tamanos = paginator.page(paginator.num_pages)

    context = {'lista_tamano': lista_tamano, 'tamanos': tamanos}

    return render_to_response('tamano_lista_search.html', context)


def lista_densidad(request):
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
                id_densidad = request.POST['item_id']
                p = Densidad.objects.get(pk=id_densidad)
                mensaje = {"status": "True", "item_id": p.id, "form": "del"}
                p.delete()

                 # Elinamos objeto de la base de datos
                messages.success(request, "Se elimino el registro.")
                return HttpResponse(json.dumps(mensaje), content_type='application/json')

            except django.db.IntegrityError:

                mensaje = {"status": "False", "form": "del",
                           "msj": "No se puede eliminar porque tiene algun registro asociado"}
                messages.success(request, "No se puede eliminar porque tiene algun registro asociado")
                return HttpResponse(json.dumps(mensaje), content_type='application/json')

            except:
                mensaje = {"status": "False", "form": "del", "msj": "Error al eliminar"}
                messages.success(request, "Error al eliminar")
                return HttpResponse(json.dumps(mensaje), content_type='application/json')
    order_by = request.GET.get('order_by')
    if order_by:
        lista_densidad = Densidad.objects.all().order_by(order_by)
    else:
        lista_densidad = Densidad.objects.all()

    paginator = Paginator(lista_densidad, nropag[0]['valor'])
    # Show 25 contacts per page
    page = request.GET.get('page')
    if page == '0':
        densidades = lista_densidad
    else:
        try:
            densidades = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            densidades = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            densidades = paginator.page(paginator.num_pages)

    context = {'lista_densidad': lista_densidad, 'densidades': densidades}
    return render(request, 'densidad_lista.html', context)


def search_densidad(request):
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
                id_densidad = request.POST['item_id']
                p = Densidad.objects.get(pk=id_densidad)
                mensaje = {"status": "True", "item_id": p.id, "form": "del"}
                p.delete()

                 # Elinamos objeto de la base de datos
                messages.success(request, "Se elimino el registro.")
                return HttpResponse(json.dumps(mensaje), content_type='application/json')

            except django.db.IntegrityError:

                mensaje = {"status": "False", "form": "del",
                           "msj": "No se puede eliminar porque tiene algun registro asociado"}
                messages.success(request, "No se puede eliminar porque tiene algun registro asociado")
                return HttpResponse(json.dumps(mensaje), content_type='application/json')

            except:
                mensaje = {"status": "False", "form": "del", "msj": "Error al eliminar"}
                messages.success(request, "Error al eliminar")
                return HttpResponse(json.dumps(mensaje), content_type='application/json')

        search_text = request.POST['search_text']
        if search_text is not None and search_text != u"":
            entry_query = get_query(search_text, ['descripcion', ])
            lista_densidad = Densidad.objects.filter(entry_query)
        else:
            lista_densidad = Densidad.objects.all()

    paginator = Paginator(lista_densidad, nropag[0]['valor'])
    # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        densidades = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        densidades = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        densidades = paginator.page(paginator.num_pages)

    context = {'lista_densidad': lista_densidad, 'densidades': densidades}

    return render_to_response('densidad_lista_search.html', context)


def buscar_tamano_mueble(request, idmueble=0):
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
                id_tamanomueble = request.POST['item_id']
                p = Tamano_Mueble.objects.get(pk=id_tamanomueble)
                mensaje = {"status": "True", "item_id": p.id, "form": "del"}
                p.delete()

                 # Elinamos objeto de la base de datos
                messages.success(request, "Se elimino el registro.")
                return HttpResponse(json.dumps(mensaje), content_type='application/json')

            except django.db.IntegrityError:

                mensaje = {"status": "False", "form": "del",
                           "msj": "No se puede eliminar porque tiene algun registro asociado"}
                messages.success(request, "No se puede eliminar porque tiene algun registro asociado")
                return HttpResponse(json.dumps(mensaje), content_type='application/json')

            except:
                mensaje = {"status": "False", "form": "del", "msj": "Error al eliminar"}
                messages.success(request, "Error al eliminar")
                return HttpResponse(json.dumps(mensaje), content_type='application/json')

    if idmueble != '0':
        try:
            buscar_tamanomueble = Tamano_Mueble.objects.filter(mueble=idmueble)
            listar_tamano = Tamano_Mueble.objects.filter(mueble=idmueble).values('tamano',
                                                                                 'tamano__descripcion',
                                                                                 'mueble').annotate(tcount=Count('tamano')).order_by('tamano')
            lista_mueble = Mueble.objects.filter(id=idmueble)
            mensaje = ""

        except ObjectDoesNotExist as ex:
            buscar_tamanomueble = ""
            mensaje = "registro no existe"

        except Exception as ex:
            buscar_tamanomueble = ""
            mensaje = "se ha producido un error"+str(ex)

    else:
        buscar_tamanomueble = Tamano_Mueble.objects.all()
        lista_mueble = Mueble.objects.all()
        listar_tamano = Tamano_Mueble.objects.values('tamano',
                                                     'tamano__descripcion',
                                                     'mueble').annotate(tcount=Count('tamano')).order_by('tamano')

        mensaje = ""

    paginator = Paginator(lista_mueble, nropag[0]['valor'])
    # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        lista_muebles = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        lista_muebles = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        lista_muebles = paginator.page(paginator.num_pages)

    context = {'buscar_tamanomueble': buscar_tamanomueble,
               'lista_muebles': lista_muebles,
               'lista_mueble': lista_mueble,
               'listar_tamano': listar_tamano,
               'mensaje': mensaje}

    return render(request, 'tamanomueble_lista.html', context)


def buscar_mueble_ambiente(request, idambiente=0):
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
                id_muebleambiente = request.POST['item_id']
                p = Mueble_Ambiente.objects.get(pk=id_muebleambiente)
                mensaje = {"status": "True", "item_id": p.id, "form": "del"}
                p.delete()

                 # Elinamos objeto de la base de datos
                messages.success(request, "Se elimino el registro.")
                return HttpResponse(json.dumps(mensaje), content_type='application/json')

            except django.db.IntegrityError:

                mensaje = {"status": "False", "form": "del",
                           "msj": "No se puede eliminar porque tiene algun registro asociado"}
                messages.success(request, "No se puede eliminar porque tiene algun registro asociado")
                return HttpResponse(json.dumps(mensaje), content_type='application/json')

            except:
                mensaje = {"status": "False", "form": "del", "msj": "Error al eliminar"}
                messages.success(request, "Error al eliminar")
                return HttpResponse(json.dumps(mensaje), content_type='application/json')

    if idambiente != '0':
        try:
            buscar_muebleambiente = Mueble_Ambiente.objects.filter(ambiente=idambiente)
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

    lista_ambiente = Ambiente.objects.all()
    paginator = Paginator(lista_ambiente, nropag[0]['valor'])
    # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        muebleambientes = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        muebleambientes = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        muebleambientes = paginator.page(paginator.num_pages)

    context = {'buscar_muebleambiente': buscar_muebleambiente,
               'muebleambientes': muebleambientes, 'ambiente': idambiente,
               'mensaje': mensaje, 'lista_ambiente': lista_ambiente}
    return render(request, 'muebleambiente_lista.html', context)


# agregar nuevo
def add_tipo_mueble(request):
    """docstring"""
    if request.method == 'POST':
        form_tipomueble = TipoMuebleForm(request.POST)
        if form_tipomueble.is_valid():
            id_reg = form_tipomueble.save()
            if 'regEdit' in request.POST:
                messages.success(request, "Registro guardado.")
                return HttpResponseRedirect(reverse('umuebles:edit_tipo_mueble',
                                                    args=(id_reg.id,)))
            else:
                return HttpResponseRedirect(reverse('umuebles:lista_tipo_mueble'))
    else:
        form_tipomueble = TipoMuebleForm()
    return render_to_response('tipomueble_add.html',
                              {'form_tipomueble': form_tipomueble, 'create': True},
                              context_instance=RequestContext(request))


def add_ocupacion(request):
    """docstring"""
    if request.method == 'POST':
        form_ocupacion = OcupacionForm(request.POST)
        if form_ocupacion.is_valid():
            id_reg = form_ocupacion.save()
            if 'regEdit' in request.POST:
                messages.success(request, "Registro guardado.")
                return HttpResponseRedirect(reverse('umuebles:edit_ocupacion',
                                                    args=(id_reg.id,)))
            else:
                return HttpResponseRedirect(reverse('umuebles:lista_ocupacion'))
    else:
        form_ocupacion = OcupacionForm()
    return render_to_response('ocupacion_add.html',
                              {'form_ocupacion': form_ocupacion, 'create': True},
                              context_instance=RequestContext(request))


def add_formamueble(request):
    """docstring"""
    if request.method == 'POST':
        form_formamueble = FormaMuebleForm(request.POST)
        if form_formamueble.is_valid():
            id_reg = form_formamueble.save()
            if 'regEdit' in request.POST:
                messages.success(request, "Registro guardado.")
                return HttpResponseRedirect(reverse('umuebles:edit_forma_mueble',
                                                    args=(id_reg.id,)))
            else:
                return HttpResponseRedirect(reverse('umuebles:lista_forma_mueble'))
    else:
        form_formamueble = FormaMuebleForm()
    return render_to_response('formamueble_add.html',
                              {'form_formamueble': form_formamueble, 'create': True},
                              context_instance=RequestContext(request))


def add_tamano(request):
    """docstring"""
    if request.method == 'POST':
        form_tamano = TamanoForm(request.POST)
        if form_tamano.is_valid():
            id_reg = form_tamano.save()
            if 'regEdit' in request.POST:
                messages.success(request, "Registro guardado.")
                return HttpResponseRedirect(reverse('umuebles:edit_tamano',
                                                    args=(id_reg.id,)))
            else:
                return HttpResponseRedirect(reverse('umuebles:lista_tamano'))
    else:
        form_tamano = TamanoForm()
    return render_to_response('tamano_add.html',
                              {'form_tamano': form_tamano, 'create': True},
                              context_instance=RequestContext(request))


def add_densidad(request):
    """docstring"""
    if request.method == 'POST':
        form_densidad = DensidadForm(request.POST)
        if form_densidad.is_valid():
            id_reg = form_densidad.save()
            if 'regEdit' in request.POST:
                messages.success(request, "Registro guardado.")
                return HttpResponseRedirect(reverse('umuebles:edit_densidad',
                                                    args=(id_reg.id,)))
            else:
                return HttpResponseRedirect(reverse('umuebles:lista_densidad'))
    else:
        form_densidad = DensidadForm()
    return render_to_response('densidad_add.html',
                              {'form_densidad': form_densidad, 'create': True},
                              context_instance=RequestContext(request))


def add_tamanomueble(request, id_m):
    """docstring"""
    if request.method == 'POST':
        form_tamanomueble = TamanoMuebleForm(request.POST)
        if form_tamanomueble.is_valid():
            id_reg = form_tamanomueble.save()
            id_tm = Tamano_Mueble.objects.get(id=id_reg.id)

            if 'regEdit' in request.POST:
                messages.success(self.request, "Registro guardado.")
                return HttpResponseRedirect(reverse('umuebles:TamanoMuebleView') + "?%s" % 'item=' + id_tm.mueble.id)
            else:
                return HttpResponseRedirect(reverse('umuebles:buscar_tamano_mueble',
                                                    args=(id_tm.mueble.id,)))

    else:
        form_tamanomueble = TamanoMuebleForm(initial={'mueble': id_m})
    return render_to_response('tamanomueble_add.html',
                              {'form_tamanomueble': form_tamanomueble, 'create': True},
                              context_instance=RequestContext(request))


class TamanoMuebleView(View):
    form_class_formset = formset_factory(TamanoMuebleForm,
                                         extra=Tamano.objects.count(),
                                         max_num=Tamano.objects.count())
    template_name = 'tamanomueble_add2.html'

    def get(self, request, *args, **kwargs):
        """docstring"""
        if self.request.is_ajax():
            mueble_id = self.request.GET.get('id_lista_mueble')
            tamano_id = self.request.GET.get('id_tamano')

            tamanomueble = Tamano_Mueble.objects.filter(tamano_id=tamano_id,
                                                        mueble_id=mueble_id)
            if tamanomueble:
                tamanomueble = [{
                    'ancho': tamanomueble[0].ancho,
                    'largo': tamanomueble[0].largo,
                    'alto': tamanomueble[0].alto,
                    'predefinido': tamanomueble[0].predefinido
                    }]
            else:
                tamanomueble = [{
                    'ancho': 0,
                    'largo': 0,
                    'alto': 0,
                    'predefinido': False
                    }]

            return JsonResponse(tamanomueble, safe=False)

        mueble = Mueble.objects.all()
        tamano = Tamano.objects.all()
        if self.request.GET.get('item'):
            tamanomueble = Tamano_Mueble.objects.filter(mueble_id=self.request.GET.get('item'))
            data = []
            for item in tamanomueble:
                data.append({'tamano': item.tamano,
                             'mueble': item.mueble,
                             'ancho': item.ancho,
                             'largo': item.largo,
                             'alto': item.alto,
                             'predefinido': item.predefinido
                             })

            formset = self.form_class_formset(initial=data)
        else:
            formset = self.form_class_formset()

        return render(request, self.template_name, {'formset': formset,
                                                    'tamano': tamano,
                                                    'mueble': mueble})

    def post(self, request, *args, **kwargs):
        formset = self.form_class_formset(request.POST)
        item = request.POST.get('listamueble')

        if formset.is_valid():
            for form in formset:
                #params = urllib.urlencode({'mueble': 'form.cleaned_data["mueble"]'})
                form.save()

            # <process form cleaned data>
            messages.success(self.request, "Registro guardado.")
            return HttpResponseRedirect(reverse('umuebles:TamanoMuebleView') + "?%s" % 'item=' + item)
        else:
            for form in formset:
                tamanomueble = Tamano_Mueble.objects.filter(tamano_id=form.cleaned_data['tamano'],
                                                            mueble_id=form.cleaned_data['mueble'])

                if tamanomueble:
                    tamanomueble.update(ancho=form.cleaned_data['ancho'],
                                        largo=form.cleaned_data['largo'],
                                        alto=form.cleaned_data['alto'],
                                        predefinido=form.cleaned_data['predefinido'])
                else:
                    form.save()

            messages.success(self.request, "Registro guardado.")
            return HttpResponseRedirect(reverse('umuebles:TamanoMuebleView') + "?%s" % 'item=' + item)
        return render(request, self.template_name, {'formset': formset})


def add_muebleambiente(request, id_ti, origen):
    """docstring"""
    redirect_to = request.REQUEST.get('next', '')
    if origen == '1':
        # Aplica cuando se llama desde el mueble
        data = {'mueble': id_ti}
        clase_filtro = 'filtra-mueble'
        nombre = Mueble.objects.filter(id=id_ti)
        titulo = 'Asociar un ambiente al mueble: ' + nombre[0].mueble
    else:
        # Aplica cuando se llama desde el ambiente
        data = {'ambiente': id_ti}
        clase_filtro = 'filtra-ambiente'
        nombre = Ambiente.objects.filter(id=id_ti)
        titulo = 'Asociar un mueble al ambiente: ' + nombre[0].ambiente

    if request.method == 'POST':
        form_muebleambiente = MuebleAmbienteForm(request.POST)
        if form_muebleambiente.is_valid():
            id_reg = form_muebleambiente.save()
            id_am = Mueble_Ambiente.objects.get(id=id_reg.id)

            if 'regEdit' in request.POST:
                messages.success(request, "Registro guardado.")
                return HttpResponseRedirect(reverse('umuebles:edit_muebleambiente',
                                                    args=(id_reg.id,)))
            else:

                if redirect_to:
                    return HttpResponseRedirect(redirect_to)
                else:
                    return HttpResponseRedirect(reverse('umuebles:buscar_mueble_ambiente',
                                                        args=(id_am.ambiente.id,)))
    else:
        form_muebleambiente = MuebleAmbienteForm(initial=data)

    return render_to_response('muebleambiente_add.html',
                              {'form_muebleambiente': form_muebleambiente,
                               'create': True,
                               'clase_filtro': clase_filtro,
                               'titulo': titulo,
                               'id_ti': id_ti},
                              context_instance=RequestContext(request))


# editar registro
def edit_tipo_mueble(request, pk):
    """docstring"""
    tipomueble = Tipo_Mueble.objects.all().get(pk=pk)

    redirect_to = request.REQUEST.get('next', '')

    if request.method == 'POST':
        # formulario enviado
        form_edit_tipomueble = TipoMuebleForm(request.POST, instance=tipomueble)

        if form_edit_tipomueble.is_valid():
            # formulario validado correctamente
            form_edit_tipomueble.save()
            if 'regEdit' in request.POST:

                messages.success(request, "Registro guardado.")
                return HttpResponseRedirect(request.get_full_path())

            else:
                if redirect_to:
                    return HttpResponseRedirect(redirect_to)
                else:
                    return HttpResponseRedirect(reverse('umuebles:lista_tipo_mueble'))

    else:
        # formulario inicial
        form_edit_tipomueble = TipoMuebleForm(instance=tipomueble)

    return render_to_response('tipomueble_edit.html',
                              {'form_edit_tipomueble': form_edit_tipomueble,
                               'tipomueble': tipomueble, 'create': False},
                              context_instance=RequestContext(request))


def edit_ocupacion(request, pk):
    """docstring"""
    ocupacion = Ocupacion.objects.get(pk=pk)

    redirect_to = request.REQUEST.get('next', '')

    if request.method == 'POST':
        # formulario enviado
        form_edit_ocupacion = OcupacionForm(request.POST, instance=ocupacion)

        if form_edit_ocupacion.is_valid():
            # formulario validado correctamente
            form_edit_ocupacion.save()
            if 'regEdit' in request.POST:

                messages.success(request, "Registro guardado.")
                return HttpResponseRedirect(request.get_full_path())

            else:
                if redirect_to:
                    return HttpResponseRedirect(redirect_to)
                else:
                    return HttpResponseRedirect(reverse('umuebles:lista_ocupacion'))

    else:
        # formulario inicial
        form_edit_ocupacion = OcupacionForm(instance=ocupacion)

    return render_to_response('ocupacion_edit.html',
                              {'form_edit_ocupacion': form_edit_ocupacion,
                               'ocupacion': ocupacion, 'create': False},
                              context_instance=RequestContext(request))


def edit_forma_mueble(request, pk):
    """docstring"""
    formamueble = Forma_Mueble.objects.get(pk=pk)

    redirect_to = request.REQUEST.get('next', '')

    if request.method == 'POST':
        # formulario enviado
        form_edit_formamueble = FormaMuebleForm(request.POST, instance=formamueble)

        if form_edit_formamueble.is_valid():
            # formulario validado correctamente
            form_edit_formamueble.save()
            if 'regEdit' in request.POST:

                messages.success(request, "Registro guardado.")
                return HttpResponseRedirect(request.get_full_path())

            else:
                if redirect_to:
                    return HttpResponseRedirect(redirect_to)
                else:
                    return HttpResponseRedirect(reverse('umuebles:lista_forma_mueble'))

    else:
        # formulario inicial
        form_edit_formamueble = FormaMuebleForm(instance=formamueble)

    return render_to_response('formamueble_edit.html',
                              {'form_edit_formamueble': form_edit_formamueble,
                               'formamueble': formamueble, 'create': False},
                              context_instance=RequestContext(request))


def edit_tamano(request, pk):
    """docstring"""
    tamano = Tamano.objects.get(pk=pk)

    redirect_to = request.REQUEST.get('next', '')

    if request.method == 'POST':
        # formulario enviado
        form_edit_tamano = TamanoForm(request.POST, instance=tamano)

        if form_edit_tamano.is_valid():
            # formulario validado correctamente
            form_edit_tamano.save()
            if 'regEdit' in request.POST:

                messages.success(request, "Registro guardado.")
                return HttpResponseRedirect(request.get_full_path())

            else:
                if redirect_to:
                    return HttpResponseRedirect(redirect_to)
                else:
                    return HttpResponseRedirect(reverse('umuebles:lista_tamano'))

    else:
        # formulario inicial
        form_edit_tamano = TamanoForm(instance=tamano)

    return render_to_response('tamano_edit.html',
                              {'form_edit_tamano': form_edit_tamano,
                               'tamano': tamano, 'create': False},
                              context_instance=RequestContext(request))


def edit_densidad(request, pk):
    """docstring"""
    densidad = Densidad.objects.get(pk=pk)

    redirect_to = request.REQUEST.get('next', '')

    if request.method == 'POST':
        # formulario enviado
        form_edit_densidad = DensidadForm(request.POST, instance=densidad)

        if form_edit_densidad.is_valid():
            # formulario validado correctamente
            form_edit_densidad.save()
            if 'regEdit' in request.POST:

                messages.success(request, "Registro guardado.")
                return HttpResponseRedirect(request.get_full_path())

            else:
                if redirect_to:
                    return HttpResponseRedirect(redirect_to)
                else:
                    return HttpResponseRedirect(reverse('umuebles:lista_densidad'))

    else:
        # formulario inicial
        form_edit_densidad = DensidadForm(instance=densidad)

    return render_to_response('densidad_edit.html',
                              {'form_edit_densidad': form_edit_densidad,
                               'densidad': densidad, 'create': False},
                              context_instance=RequestContext(request))


def edit_tamanomueble(request, pk):
    """docstring"""
    tamanomueble = Tamano_Mueble.objects.get(pk=pk)

    redirect_to = request.REQUEST.get('next', '')

    if request.method == 'POST':
        # formulario enviado
        form_edit_tamanomueble = TamanoMuebleForm(request.POST, instance=tamanomueble)

        if form_edit_tamanomueble.is_valid():
            # formulario validado correctamente
            form_edit_tamanomueble.save()
            if 'regEdit' in request.POST:

                messages.success(request, "Registro guardado.")
                return HttpResponseRedirect(request.get_full_path())

            else:
                if redirect_to:
                    return HttpResponseRedirect(redirect_to)
                else:
                    return HttpResponseRedirect(reverse('umuebles:buscar_tamano_mueble',
                                                        args=(tamanomueble.mueble.id,)))

    else:
        # formulario inicial
        form_edit_tamanomueble = TamanoMuebleForm(instance=tamanomueble)

    return render_to_response('tamanomueble_edit.html',
                              {'form_edit_tamanomueble': form_edit_tamanomueble,
                               'create': False},
                              context_instance=RequestContext(request))


def edit_muebleambiente(request, pk):
    """docstring"""
    muebleambiente = Mueble_Ambiente.objects.get(pk=pk)

    redirect_to = request.REQUEST.get('next', '')

    if request.method == 'POST':
        # formulario enviado
        form_edit_muebleambiente = MuebleAmbienteForm(request.POST, instance=muebleambiente)

        if form_edit_muebleambiente.is_valid():
            # formulario validado correctamente
            form_edit_muebleambiente.save()
            if 'regEdit' in request.POST:

                messages.success(request, "Registro guardado.")
                return HttpResponseRedirect(request.get_full_path())

            else:
                if redirect_to:
                    return HttpResponseRedirect(redirect_to)

                return HttpResponseRedirect(reverse('umuebles:buscar_mueble_ambiente',
                                                    args=(muebleambiente.ambiente.id,)))

    else:
        # formulario inicial
        form_edit_muebleambiente = MuebleAmbienteForm(instance=muebleambiente)

    return render_to_response('muebleambiente_edit.html',
                              {'form_edit_muebleambiente': form_edit_muebleambiente, 'create': False},
                              context_instance=RequestContext(request))


class FichaMueble(DetailView):
    """docstring for ficha_mueble"""
    model = Mueble
    context_object_name = "mueble"
    template_name = 'mueble_ficha.html'

    def get_context_data(self, **kwargs):
        context = super(FichaMueble, self).get_context_data(**kwargs)
        return context
