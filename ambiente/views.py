"""
docstring está pendiente de elaboración

"""

from django.shortcuts import render, render_to_response
from ambiente.models import Ambiente, Ambiente_Tipo_inmueble
from ambiente.forms import AmbienteForm, AmbienteTipoInmuebleForm
from direccion.models import Tipo_Inmueble
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
import simplejson as json
import django.db
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from mtvmcotizacion.views import get_query
from premisas.models import PerzonalizacionVisual


def lista_ambiente(request):
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
                id_ambiente = request.POST['item_id']
                p = Ambiente.objects.get(pk=id_ambiente)
                mensaje = {"status": "True", "item_id": p.id, "form": "del",
                           "msj": "Se elimino el registro."}
                p.delete()

                 # Elinamos objeto de la base de datos
                return HttpResponse(json.dumps(mensaje), content_type='application/json')

            except django.db.IntegrityError:

                mensaje = {"status": "False", "form": "del", "msj": "No se puede eliminar porque \
                tiene algun registro asociado"}
                return HttpResponse(json.dumps(mensaje), content_type='application/json')

            except:
                mensaje = {"status": "False", "form": "del", "msj": "Error al eliminar "}
                return HttpResponse(json.dumps(mensaje), content_type='application/json')

    order_by = request.GET.get('order_by')
    if order_by:
        lista_ambiente = Ambiente.objects.all().order_by(order_by)
    else:
        lista_ambiente = Ambiente.objects.all()
    paginator = Paginator(lista_ambiente, nropag[0]['valor'])
    # Show 25 contacts per page
    page = request.GET.get('page')
    if page == '0':
        ambientes = lista_ambiente
    else:
        try:
            ambientes = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            ambientes = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            ambientes = paginator.page(paginator.num_pages)

    ambiente_links = zip(['Ambientes por tipo de inmueble', ],
                         ['uambientes:lista_ambiente_tipo_inmueble', ])

    context = {'lista_ambiente': lista_ambiente, 'ambientes': ambientes,
               'ambiente_links': ambiente_links}
    return render(request, 'ambiente_lista.html', context)


def search_ambiente(request):
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
                id_ambiente = request.POST['item_id']
                p = Ambiente.objects.get(pk=id_ambiente)
                mensaje = {"status": "True", "item_id": p.id, "form": "del",
                           "msj": "Se elimino el registro."}
                p.delete()

                 # Elinamos objeto de la base de datos
                return HttpResponse(json.dumps(mensaje), content_type='application/json')

            except django.db.IntegrityError:

                mensaje = {"status": "False", "form": "del", "msj": "No se puede eliminar porque \
                tiene algun registro asociado"}
                return HttpResponse(json.dumps(mensaje), content_type='application/json')

            except:
                mensaje = {"status": "False", "form": "del", "msj": "Error al eliminar "}
                return HttpResponse(json.dumps(mensaje), content_type='application/json')

        search_text = request.POST['search_text']
        if search_text is not None and search_text != u"":
            entry_query = get_query(search_text, ['ambiente', ])
            lista_ambiente = Ambiente.objects.filter(entry_query)
        else:
            lista_ambiente = Ambiente.objects.all()

    paginator = Paginator(lista_ambiente, nropag[0]['valor'])
    # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        ambientes = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        ambientes = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        ambientes = paginator.page(paginator.num_pages)

    ambiente_links = zip(['Ambientes por tipo de inmueble', ],
                         ['uambientes:lista_ambiente_tipo_inmueble', ])

    context = {'lista_ambiente': lista_ambiente, 'ambientes': ambientes,
               'ambiente_links': ambiente_links}
    return render_to_response('ambiente_lista_search.html', context)


def lista_ambiente_tipo_inmueble(request):
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
                id_ambtipoinmueble = request.POST['item_id']
                p = Ambiente_Tipo_inmueble.objects.get(pk=id_ambtipoinmueble)
                mensaje = {"status": "True", "item_id": p.id, "form": "del",
                           "msj": "Se elimino el registro."}
                p.delete()

                 # Elinamos objeto de la base de datos
                return HttpResponse(json.dumps(mensaje), content_type='application/json')

            except django.db.IntegrityError:

                mensaje = {"status": "False", "form": "del", "msj": "No se puede eliminar porque \
                tiene algun registro asociado"}
                return HttpResponse(json.dumps(mensaje), content_type='application/json')

            except:
                mensaje = {"status": "False", "form": "del", "msj": "Error al eliminar "}
                return HttpResponse(json.dumps(mensaje), content_type='application/json')

    lista_inmueble = Tipo_Inmueble.objects.filter()
    lista_ambtipoinmueble = Ambiente_Tipo_inmueble.objects.all()
    paginator = Paginator(lista_inmueble, nropag[0]['valor'])
    # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        listas_inmueble = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        listas_inmueble = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        listas_inmueble = paginator.page(paginator.num_pages)
    context = {'lista_ambtipoinmueble': lista_ambtipoinmueble,
               'lista_inmueble': lista_inmueble, 'listas_inmueble': listas_inmueble}
    return render(request, 'ambientetipoinmueble_lista.html', context)


def buscar_ambiente(request, id_tipoinmueble):
    """docstring"""
    tipo_inmueble = Ambiente_Tipo_inmueble.objects.get(id=id_tipoinmueble)

    lista_ambiente = Ambiente.objects.filter(pk=tipo_inmueble.ambiente_id)
    context = {'lista_ambiente': lista_ambiente}
    return render(request, 'ambiente_lista.html', context)


def add_ambiente(request):
    """docstring"""
    if request.method == 'POST':
        form_ambiente = AmbienteForm(request.POST)
        if form_ambiente.is_valid():
            form_ambiente.save()
            return HttpResponseRedirect(reverse('uambientes:lista_ambiente'))
    else:
        form_ambiente = AmbienteForm()
    return render_to_response('ambiente_add.html',
                              {'form_ambiente': form_ambiente, 'create': True},
                              context_instance=RequestContext(request))


def add_ambiente_tipoinmueble(request, id_ti, origen):
    """docstring"""
    redirect_to = request.REQUEST.get('next', '')
    if origen == '1':
        # Aplica cuando se llama desde el tipo de inmueble
        data = {'tipo_inmueble': id_ti}
        clase_filtro = 'filtra-tipoinmueble'
        nombre = Tipo_Inmueble.objects.filter(id=id_ti)
        titulo = 'Asociar un ambiente al tipo de inmueble: ' + nombre[0].tipo_inmueble
    else:
        # Aplica cuando se llama desde el ambiente
        data = {'ambiente': id_ti}
        clase_filtro = 'filtra-ambiente'
        nombre = Ambiente.objects.filter(id=id_ti)
        titulo = 'Asociar un tipo de inmueble al ambiente: ' + nombre[0].ambiente

    if request.method == 'POST':
        form_ambtipoinmueble = AmbienteTipoInmuebleForm(request.POST)
        if form_ambtipoinmueble.is_valid():
            form_ambtipoinmueble.save()

            if redirect_to:
                return HttpResponseRedirect(redirect_to)
            else:
                return HttpResponseRedirect(reverse('uambientes:lista_ambiente_tipo_inmueble'))

    else:
        form_ambtipoinmueble = AmbienteTipoInmuebleForm(initial=data)

    return render_to_response('ambientetipoinmueble_add.html',
                              {'form_ambtipoinmueble': form_ambtipoinmueble,
                               'create': True,
                               'clase_filtro': clase_filtro,
                               'titulo': titulo,
                               'id_ti': id_ti},
                              context_instance=RequestContext(request))


# editar un registro
def edit_ambiente(request, pk):
    """docstring"""

    id_ambiente = Ambiente.objects.get(pk=pk)

    redirect_to = request.REQUEST.get('next', '')

    if request.method == 'POST':
        # formulario enviado
        form_edit_ambiente = AmbienteForm(request.POST, instance=id_ambiente)

        if form_edit_ambiente.is_valid():
            # formulario validado correctamente
            form_edit_ambiente.save()

            if redirect_to:
                return HttpResponseRedirect(redirect_to)
            else:
                return HttpResponseRedirect(reverse('uambientes:lista_ambiente'))

    else:
        # formulario inicial
        form_edit_ambiente = AmbienteForm(instance=id_ambiente)

    return render_to_response('ambiente_edit.html',
                              {'form_edit_ambiente': form_edit_ambiente,
                               'ambiente': id_ambiente, 'create': False},
                              context_instance=RequestContext(request))


def edit_ambiente_tipoinmueble(request, pk):
    """docstring"""
    ambtipoinmueble = Ambiente_Tipo_inmueble.objects.get(pk=pk)

    redirect_to = request.REQUEST.get('next', '')

    if request.method == 'POST':
        # formulario enviado
        form_edit_ambtipoinmueble = AmbienteTipoInmuebleForm(request.POST, instance=ambtipoinmueble)

        if form_edit_ambtipoinmueble.is_valid():
            # formulario validado correctamente
            form_edit_ambtipoinmueble.save()

            if redirect_to:
                return HttpResponseRedirect(redirect_to)
            else:
                return HttpResponseRedirect(reverse('uambientes:lista_ambiente_tipo_inmueble'))

    else:
        # formulario inicial
        form_edit_ambtipoinmueble = AmbienteTipoInmuebleForm(instance=ambtipoinmueble)

    return render_to_response('ambientetipoinmueble_edit.html',
                              {'form_edit_ambtipoinmueble': form_edit_ambtipoinmueble,
                               'create': False},
                              context_instance=RequestContext(request))
