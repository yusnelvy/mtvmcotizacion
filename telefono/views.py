from django.shortcuts import render, render_to_response
from telefono.models import Tipo_telefono, Telefono
from telefono.forms import TipoTelefonoForm, TelefonoForm
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.core.urlresolvers import reverse
import django.db
import simplejson as json
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from mtvmcotizacion.views import get_query
from premisas.models import PerzonalizacionVisual


# Create your views here.
# lista
def lista_tipotelefono(request):
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
    order_by = request.GET.get('order_by')
    if order_by:
        lista_tipotelefono = Tipo_telefono.objects.all().order_by(order_by)
    else:
        lista_tipotelefono = Tipo_telefono.objects.all()

    paginator = Paginator(lista_tipotelefono, nropag[0]['valor'])
    # Show 25 contacts per page
    page = request.GET.get('page')
    if page == '0':
        tipostelefono = lista_tipotelefono
    else:
        try:
            tipostelefono = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            tipostelefono = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            tipostelefono = paginator.page(paginator.num_pages)

    context = {'lista_tipotelefono': lista_tipotelefono,
               'tipostelefono': tipostelefono}
    return render(request, 'tipotelefono_lista.html', context)


def search_tipotelefono(request):
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

        search_text = request.POST['search_text']
        if search_text is not None and search_text != u"":
            entry_query = get_query(search_text, ['tipo_telefono', ])
            lista_tipotelefono = Tipo_telefono.objects.filter(entry_query)
        else:
            lista_tipotelefono = Tipo_telefono.objects.all()

    paginator = Paginator(lista_tipotelefono, nropag[0]['valor'])
    # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        tipostelefono = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        tipostelefono = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        tipostelefono = paginator.page(paginator.num_pages)

    context = {'lista_tipotelefono': lista_tipotelefono, 'tipostelefono': tipostelefono}
    return render_to_response('tipotelefono_lista_search.html', context)


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
    return render(request, 'telefono_lista.html', context)


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
    return render_to_response('tipotelefono_add.html',
                              {'form_tipotelefono': form_tipotelefono, 'create': True},
                              context_instance=RequestContext(request))


def add_telefono(request, id_cli):
    """docstring"""
    redirect_to = request.REQUEST.get('next', '')

    if request.method == 'POST':
        form_telefono = TelefonoForm(request.POST)
        if form_telefono.is_valid():
            id_reg = form_telefono.save()
            id_cli = Telefono.objects.get(id=id_reg.id)
        if redirect_to:
            return HttpResponseRedirect(redirect_to)
        else:
            #return HttpResponseRedirect(reverse('utelefonos:lista_telefono'))return HttpResponseRedirect(reverse('uclientes:ficha_cliente', args=(id_cli.cliente.id,)))
            return HttpResponseRedirect(reverse('uclientes:ficha_cliente', args=(id_cli.cliente.id,)))
    else:
        form_telefono = TelefonoForm(initial={'cliente': id_cli})
    return render_to_response('telefono_add.html',
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

    return render_to_response('tipotelefono_edit.html',
                              {'form_edit_tipotelefono': form_edit_tipotelefono, 'create': False},
                              context_instance=RequestContext(request))


def edit_telefono(request, pk):
    """docstring"""

    id_telefono = Telefono.objects.get(pk=pk)

    redirect_to = request.REQUEST.get('next', '')

    if request.method == 'POST':
        # formulario enviado
        form_edit_telefono = TelefonoForm(request.POST, instance=id_telefono)

        if form_edit_telefono.is_valid():
            # formulario validado correctamente
            id_reg = form_edit_telefono.save()
            id_cli = Telefono.objects.get(id=id_reg.id)
        if redirect_to:
            return HttpResponseRedirect(redirect_to)
        else:

            #return HttpResponseRedirect(reverse('uclientes:lista_cliente'))
            #return HttpResponseRedirect('../../cliente/ficha_cliente/')
            return HttpResponseRedirect(reverse('uclientes:ficha_cliente', args=(id_cli.cliente.id,)))
    else:
        # formulario inicial
        form_edit_telefono = TelefonoForm(instance=id_telefono)

    return render_to_response('telefono_edit.html',
                              {'form_edit_telefono': form_edit_telefono, 'telefono': id_telefono, 'create': False},
                              context_instance=RequestContext(request))
