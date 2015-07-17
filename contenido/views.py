from django.shortcuts import render, render_to_response
from contenido.models import Contenido, \
    Contenido_Tipico, Contenido_Servicio
from mueble.models import Mueble
from contenido.forms import ContenidoForm, \
    ContenidoTipicoForm, ContenidoServicioForm
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
import simplejson as json
import django.db
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
# lista
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
    paginator = Paginator(lista_contenido, 25)
    # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        contenidos = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contenidos = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contenidos = paginator.page(paginator.num_pages)

    context = {'lista_contenido': lista_contenido, 'contenidos': contenidos}
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

    lista_mueble = Mueble.objects.all()
    paginator = Paginator(lista_mueble, 25)
    # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        contenidotipicos = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contenidotipicos = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contenidotipicos = paginator.page(paginator.num_pages)

    context = {'buscar_contenidotipico': buscar_contenidotipico, 'contenidotipicos': contenidotipicos, 'lista_mueble': lista_mueble}
    return render(request, 'contenido/contenidotipico_lista.html', context)


def buscar_contenidoservicio(request, idservicio=0):
    """docstring"""

    if request.method == "POST":
        if "item_id" in request.POST:
            try:
                id_contenidoservicio = request.POST['item_id']
                p = Contenido_Servicio.objects.get(pk=id_contenidoservicio)
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

    if idservicio != '0':
        try:
            buscar_contenidoservicio = Contenido_Servicio.objects.filter(servicio=idservicio)
            mensaje = ""
        except ObjectDoesNotExist as ex:
            buscar_contenidoservicio = ""
            mensaje = "registro no existe"

        except Exception as ex:
            buscar_contenidoservicio = ""
            mensaje = "se ha producido un error"+str(ex)
    else:
        buscar_contenidoservicio = Contenido_Servicio.objects.all()
        mensaje = ""

    lista_contenido = Contenido.objects.all()
    paginator = Paginator(lista_contenido, 25)
    # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        contenidos = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contenidos = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contenidos = paginator.page(paginator.num_pages)
    context = {'buscar_contenidoservicio': buscar_contenidoservicio, 'contenidos': contenidos, 'lista_contenido': lista_contenido}
    return render(request, 'contenido/contenidoservicio_lista.html', context)


# agregar nuevo
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


def add_contenidotipico(request, id_m):
    """docstring"""
    if request.method == 'POST':
        form_contenidotipico = ContenidoTipicoForm(request.POST)
        if form_contenidotipico.is_valid():
            form_contenidotipico.save()
            return HttpResponseRedirect(reverse('ucontenidos:buscar_contenidotipico', args=('0')))
    else:
        form_contenidotipico = ContenidoTipicoForm(initial={'mueble': id_m})
    return render_to_response('contenido/contenidotipico_add.html',
                              {'form_contenidotipico': form_contenidotipico, 'create': True},
                              context_instance=RequestContext(request))


def add_contenidoservicio(request, id_c):
    """docstring"""
    if request.method == 'POST':
        form_contenidoservicio = ContenidoServicioForm(request.POST)
        if form_contenidoservicio.is_valid():
            form_contenidoservicio.save()
            return HttpResponseRedirect(reverse('ucontenidos:buscar_contenidoservicio', args=('0')))
    else:
        form_contenidoservicio = ContenidoServicioForm(initial={'contenido': id_c})
    return render_to_response('contenido/contenidoservicio_add.html',
                              {'form_contenidoservicio': form_contenidoservicio, 'create': True},
                              context_instance=RequestContext(request))


# editar registro
def edit_contenido(request, pk):
    """docstring"""
    contenido = Contenido.objects.get(pk=pk)

    redirect_to = request.REQUEST.get('next', '')

    if request.method == 'POST':
        # formulario enviado
        form_edit_contenido = ContenidoForm(request.POST, instance=contenido)

        if form_edit_contenido.is_valid():
            # formulario validado correctamente
            form_edit_contenido.save()
        if redirect_to:
            return HttpResponseRedirect(redirect_to)
        else:
            return HttpResponseRedirect(reverse('ucontenidos:lista_contenido'))

    else:
        # formulario inicial
        form_edit_contenido = ContenidoForm(instance=contenido)

    return render_to_response('contenido/contenido_edit.html',
                              {'form_edit_contenido': form_edit_contenido, 'create': False},
                              context_instance=RequestContext(request))


def edit_contenidotipico(request, pk):
    """docstring"""
    contenidotipico = Contenido_Tipico.objects.get(pk=pk)
    redirect_to = request.REQUEST.get('next', '')

    if request.method == 'POST':
        # formulario enviado
        form_edit_contenidotipico = ContenidoTipicoForm(request.POST, instance=contenidotipico)

        if form_edit_contenidotipico.is_valid():
            # formulario validado correctamente
            form_edit_contenidotipico.save()

            if redirect_to:
                return HttpResponseRedirect(redirect_to)
            else:
                return HttpResponseRedirect(reverse('ucontenidos:buscar_contenidotipico', args=(contenidotipico.mueble.id,)))

    else:
        # formulario inicial
        form_edit_contenidotipico = ContenidoTipicoForm(instance=contenidotipico)

    return render_to_response('contenido/contenidotipico_edit.html',
                              {'form_edit_contenidotipico': form_edit_contenidotipico, 'create': False},
                              context_instance=RequestContext(request))


def edit_contenidoservicio(request, pk):
    """docstring"""
    contenidoservicio = Contenido_Servicio.objects.get(pk=pk)

    if request.method == 'POST':
        # formulario enviado
        form_edit_contenidoservicio = ContenidoServicioForm(request.POST, instance=contenidoservicio)

        if form_edit_contenidoservicio.is_valid():
            # formulario validado correctamente
            form_edit_contenidoservicio.save()

            return HttpResponseRedirect(reverse('ucontenidos:buscar_contenidoservicio', args=(contenidoservicio.servicio.id,)))

    else:
        # formulario inicial
        form_edit_contenidoservicio = ContenidoServicioForm(instance=contenidoservicio)

    return render_to_response('contenido/contenidoservicio_edit.html',
                              {'form_edit_contenidoservicio': form_edit_contenidoservicio, 'create': False},
                              context_instance=RequestContext(request))
