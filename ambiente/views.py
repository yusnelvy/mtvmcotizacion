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


# Create your views here.
# lista

def lista_ambiente(request):
    """docstring"""

    if request.method == "POST":
        if "item_id" in request.POST:
            try:
                id_ambiente = request.POST['item_id']
                p = Ambiente.objects.get(pk=id_ambiente)
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

    lista_ambiente = Ambiente.objects.all()
    paginator = Paginator(lista_ambiente, 25)
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
    context = {'lista_ambiente': lista_ambiente, 'ambientes': ambientes}
    return render(request, 'ambiente/ambiente_lista.html', context)


def lista_ambiente_tipo_inmueble(request):
    """docstring"""
    if request.method == "POST":
        if "item_id" in request.POST:
            try:
                id_ambtipoinmueble = request.POST['item_id']
                p = Ambiente_Tipo_inmueble.objects.get(pk=id_ambtipoinmueble)
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
    lista_inmueble = Tipo_Inmueble.objects.filter()
    lista_ambtipoinmueble = Ambiente_Tipo_inmueble.objects.all()
    paginator = Paginator(lista_inmueble, 25)
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
    context = {'lista_ambtipoinmueble': lista_ambtipoinmueble, 'lista_inmueble': lista_inmueble, 'listas_inmueble': listas_inmueble}
    return render(request, 'ambiente/ambientetipoinmueble_lista.html', context)


def buscar_ambiente(request, id_tipoinmueble):
    """docstring"""
    tipo_inmueble = Ambiente_Tipo_inmueble.objects.get(id=id_tipoinmueble)

    lista_ambiente = Ambiente.objects.filter(pk=tipo_inmueble.ambiente_id)
    context = {'lista_ambiente': lista_ambiente}
    return render(request, 'ambiente/ambiente_lista.html', context)


# agregar nuevo
def add_ambiente(request):
    """docstring"""
    if request.method == 'POST':
        form_ambiente = AmbienteForm(request.POST)
        if form_ambiente.is_valid():
            form_ambiente.save()
            return HttpResponseRedirect(reverse('uambientes:lista_ambiente'))
    else:
        form_ambiente = AmbienteForm()
    return render_to_response('ambiente/ambiente_add.html',
                              {'form_ambiente': form_ambiente, 'create': True},
                              context_instance=RequestContext(request))


def add_ambiente_tipoinmueble(request, id_ti):
    """docstring"""
    if request.method == 'POST':
        form_ambtipoinmueble = AmbienteTipoInmuebleForm(request.POST)
        if form_ambtipoinmueble.is_valid():
            form_ambtipoinmueble.save()
            return HttpResponseRedirect(reverse('uambientes:lista_ambiente_tipo_inmueble'))
    else:
        form_ambtipoinmueble = AmbienteTipoInmuebleForm(initial={'tipo_inmueble': id_ti})
    return render_to_response('ambiente/ambientetipoinmueble_add.html',
                              {'form_ambtipoinmueble': form_ambtipoinmueble, 'create': True},
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

    return render_to_response('ambiente/ambiente_edit.html',
                              {'form_edit_ambiente': form_edit_ambiente, 'ambiente': id_ambiente, 'create': False},
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

    return render_to_response('ambiente/ambientetipoinmueble_edit.html',
                              {'form_edit_ambtipoinmueble': form_edit_ambtipoinmueble, 'create': False},
                              context_instance=RequestContext(request))
