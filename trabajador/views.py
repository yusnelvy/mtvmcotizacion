""" docstring """

from django.shortcuts import render, render_to_response
from trabajador.models import Cargo_trabajador
from trabajador.forms import CargotrabajadorForm
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
def lista_cargotrabajador(request):
    """docstring"""
    try:
        nropag = PerzonalizacionVisual.objects.values('valor').filter(usuario=
                                                                      request.user.id,
                                                                      tipo="paginacion")
    except PerzonalizacionVisual.DoesNotExist:
        nropag = PerzonalizacionVisual.objects.values('valor').filter(usuario="std",
                                                                      tipo="paginacion")
    order_by = request.GET.get('order_by')
    if order_by:
        lista_cargo = Cargo_trabajador.objects.all().order_by(order_by)
    else:
        lista_cargo = Cargo_trabajador.objects.all()

    paginator = Paginator(lista_cargo, nropag[0]['valor'])
    # Show 25 contacts per page
    page = request.GET.get('page')
    if page == '0':
        cargos = lista_cargo
    else:
        try:
            cargos = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            cargos = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            cargos = paginator.page(paginator.num_pages)

    context = {'lista_cargo': lista_cargo, 'cargos': cargos}
    return render(request, 'cargotrabajador_lista.html', context)


def search_cargotrabajador(request):
    """docstring"""
    try:
        nropag = PerzonalizacionVisual.objects.values('valor').filter(usuario=
                                                                      request.user.id,
                                                                      tipo="paginacion")
    except PerzonalizacionVisual.DoesNotExist:
        nropag = PerzonalizacionVisual.objects.values('valor').filter(usuario="std",
                                                                      tipo="paginacion")
    if request.method == "POST":
        if "item_id" in request.POST:
            try:
                id_cargotrabajador = request.POST['item_id']
                p = Cargo_trabajador.objects.get(pk=id_cargotrabajador)
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
            entry_query = get_query(search_text, ['cargo', ])
            lista_cargo = Cargo_trabajador.objects.filter(entry_query)
        else:
            lista_cargo = Cargo_trabajador.objects.all()

    paginator = Paginator(lista_cargo, nropag[0]['valor'])
    # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        cargos = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        cargos = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        cargos = paginator.page(paginator.num_pages)

    context = {'lista_cargo': lista_cargo, 'cargos': cargos}
    return render_to_response('cargotrabajador_lista_search.html', context)


# agregar nuevo
def add_cargotrabajador(request):
    """docstring"""

    if request.method == 'POST':
        form_cargotrabajador = CargotrabajadorForm(request.POST)
        if form_cargotrabajador.is_valid():
            form_cargotrabajador.save()
            return HttpResponseRedirect(reverse('utrabajadores:lista_cargotrabajador'))

    else:
        form_cargotrabajador = CargotrabajadorForm()
    return render_to_response('cargotrabajador_add.html',
                              {'form_cargotrabajador': form_cargotrabajador, 'create': True},
                              context_instance=RequestContext(request))


# editar
def edit_cargotrabajador(request, pk):
    """docstring"""

    id_cargo = Cargo_trabajador.objects.get(pk=pk)

    redirect_to = request.REQUEST.get('next', '')

    if request.method == 'POST':
        # formulario enviado
        form_edit_cargotrabajador = CargotrabajadorForm(request.POST, instance=id_cargo)

        if form_edit_cargotrabajador.is_valid():
            # formulario validado correctamente
            form_edit_cargotrabajador.save()

            if redirect_to:
                return HttpResponseRedirect(redirect_to)
            else:
                return HttpResponseRedirect(reverse('utrabajadores:lista_cargotrabajador'))
    else:
        # formulario inicial
        form_edit_cargotrabajador = CargotrabajadorForm(instance=id_cargo)

    return render_to_response('cargotrabajador_edit.html',
                              {'form_edit_cargotrabajador': form_edit_cargotrabajador, 'create': False},
                              context_instance=RequestContext(request))
