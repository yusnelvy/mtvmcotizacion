from django.shortcuts import render, render_to_response
from contenido.models import Contenedor, \
    Contenido, Contenido_Tipico
from contenido.forms import ContenedorForm, \
    ContenidoForm, ContenidoTipicoForm
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
import simplejson as json
import django.db
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
# lista
def lista_contenedor(request):
    """docstring"""

    if request.method == "POST":
        if "item_id" in request.POST:
            try:
                id_contenedor = request.POST['item_id']
                p = Contenedor.objects.get(pk=id_contenedor)
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

    lista_contenedor = Contenedor.objects.all()
    context = {'lista_contenedor': lista_contenedor}
    return render(request, 'contenido/contenedor_lista.html', context)


def lista_contenido(request):
    """docstring"""

    if request.method == "POST":
        if "item_id" in request.POST:
            try:
                id_contenido = request.POST['item_id']
                p = Contenido.objects.get(pk=id_contenido)
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

    lista_contenido = Contenido.objects.all()
    context = {'lista_contenido': lista_contenido}
    return render(request, 'contenido/contenido_lista.html', context)


def buscar_contenidotipico(request, idmueble=0):
    """docstring"""

    if request.method == "POST":
        if "item_id" in request.POST:
            try:
                id_contenidotipico = request.POST['item_id']
                p = Contenido_Tipico.objects.get(pk=id_contenidotipico)
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

    if idmueble != '0':
        try:
            buscar_contenidotipico = Contenido_Tipico.objects.filter(mueble=idmueble)
            mensaje = ""
        except ObjectDoesNotExist as ex:
            buscar_contenidotipico = ""
            mensaje = "registro no existe"

        except Exception as ex:
            buscar_contenidotipico = ""
            mensaje = "se ha producido un error"+str(ex)
    else:
        buscar_contenidotipico = Contenido_Tipico.objects.all()
        mensaje = ""
    context = {'buscar_contenidotipico': buscar_contenidotipico}
    return render(request, 'contenido/contenidotipico_lista.html', context)


# agregar nuevo
def add_contenedor(request):
    """docstring"""
    if request.method == 'POST':
        form_contenedor = ContenedorForm(request.POST)
        if form_contenedor.is_valid():
            form_contenedor.save()
            return HttpResponseRedirect(reverse('ucontenidos:lista_contenedor'))
    else:
        form_contenedor = ContenedorForm()
    return render_to_response('contenido/contenedor_add.html',
                              {'form_contenedor': form_contenedor, 'create': True},
                              context_instance=RequestContext(request))


def add_contenido(request):
    """docstring"""
    if request.method == 'POST':
        form_contenido = ContenidoForm(request.POST)
        if form_contenido.is_valid():
            form_contenido.save()
            return HttpResponseRedirect(reverse('ucontenidos:lista_contenido'))
    else:
        form_contenido = ContenidoForm()
    return render_to_response('contenido/contenido_add.html',
                              {'form_contenido': form_contenido, 'create': True},
                              context_instance=RequestContext(request))


def add_contenidotipico(request):
    """docstring"""
    if request.method == 'POST':
        form_contenidotipico = ContenidoTipicoForm(request.POST)
        if form_contenidotipico.is_valid():
            form_contenidotipico.save()
            return HttpResponseRedirect(reverse('ucontenidos:buscar_contenidotipico', args=('0')))
    else:
        form_contenidotipico = ContenidoTipicoForm()
    return render_to_response('contenido/contenidotipico_add.html',
                              {'form_contenidotipico': form_contenidotipico, 'create': True},
                              context_instance=RequestContext(request))


# editar registro
def edit_contenido(request, pk):
    """docstring"""
    contenido = Contenido.objects.get(pk=pk)

    if request.method == 'POST':
        # formulario enviado
        form_edit_contenido = ContenidoForm(request.POST, instance=contenido)

        if form_edit_contenido.is_valid():
            # formulario validado correctamente
            form_edit_contenido.save()

            return HttpResponseRedirect(reverse('ucontenidos:lista_contenido'))

    else:
        # formulario inicial
        form_edit_contenido = ContenidoForm(instance=contenido)

    return render_to_response('contenido/contenido_edit.html',
                              {'form_edit_contenido': form_edit_contenido, 'create': False},
                              context_instance=RequestContext(request))


def edit_contenedor(request, pk):
    """docstring"""
    contenedor = Contenedor.objects.get(pk=pk)

    if request.method == 'POST':
        # formulario enviado
        form_edit_contenedor = ContenedorForm(request.POST, instance=contenedor)

        if form_edit_contenedor.is_valid():
            # formulario validado correctamente
            form_edit_contenedor.save()

            return HttpResponseRedirect(reverse('ucontenidos:lista_contenedor'))

    else:
        # formulario inicial
        form_edit_contenedor = ContenedorForm(instance=contenedor)

    return render_to_response('contenido/contenedor_edit.html',
                              {'form_edit_contenedor': form_edit_contenedor, 'create': False},
                              context_instance=RequestContext(request))


def edit_contenidotipico(request, pk):
    """docstring"""
    contenidotipico = Contenido_Tipico.objects.get(pk=pk)

    if request.method == 'POST':
        # formulario enviado
        form_edit_contenidotipico = ContenidoTipicoForm(request.POST, instance=contenidotipico)

        if form_edit_contenidotipico.is_valid():
            # formulario validado correctamente
            form_edit_contenidotipico.save()

            return HttpResponseRedirect(reverse('ucontenidos:buscar_contenidotipico', args=(contenidotipico.contenido.id,)))

    else:
        # formulario inicial
        form_edit_contenidotipico = ContenidoTipicoForm(instance=contenidotipico)

    return render_to_response('contenido/contenidotipico_edit.html',
                              {'form_edit_contenidotipico': form_edit_contenidotipico, 'create': False},
                              context_instance=RequestContext(request))
