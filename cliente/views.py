""" docstring """

from django.shortcuts import render, render_to_response, get_object_or_404
from cliente.models import Cliente, Email, Sexo, Estado_civil,\
    TipoCliente
from telefono.models import Telefono
from direccion.models import Direccion
from cliente.forms import ClienteForm, EmailForm, SexoForm,\
    EstadoCivilForm, TipoClienteForm
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist
from cotizacion.models import Cotizacion
import simplejson as json
import django.db
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from mtvmcotizacion.views import get_query
from premisas.models import PerzonalizacionVisual
from django.contrib import messages


# Create your views here.
# lista
def lista_sexo(request):
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
                id_sexo = request.POST['item_id']
                try:
                    p = Sexo.objects.get(pk=id_sexo)
                except Sexo.DoesNotExist:
                    raise Http404
                mensaje = {"status": "True", "item_id": p.id, "form": "del"}
                p.delete()

                # Elinamos objeto de la base de datos
                messages.success(request, "Se elimino el registro.")
                return HttpResponse(json.dumps(mensaje), content_type='application/json')

            except django.db.IntegrityError:

                mensaje = {"status": "False",
                           "form": "del",
                           "msj": "No se puede eliminar porque tiene algun registro asociado"}
                messages.success(request, "No se puede eliminar porque tiene algun registro asociado.")
                return HttpResponse(json.dumps(mensaje), content_type='application/json')

            except:
                mensaje = {"status": "False", "form": "del", "msj": "Error al eliminar"}
                messages.success(request, "Error al eliminar.")
                return HttpResponse(json.dumps(mensaje), content_type='application/json')
    order_by = request.GET.get('order_by')
    if order_by:
        lista_sexo = Sexo.objects.all().order_by(order_by)
    else:
        lista_sexo = Sexo.objects.all()

    paginator = Paginator(lista_sexo, nropag[0]['valor'])
    # Show 25 contacts per page
    page = request.GET.get('page')
    if page == '0':
        sexos = lista_sexo
    else:
        try:
            sexos = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            sexos = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            sexos = paginator.page(paginator.num_pages)

    context = {'lista_sexo': lista_sexo, 'sexos': sexos}

    return render(request, 'sexo_lista.html', context)


def search_sexo(request):
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
                id_sexo = request.POST['item_id']
                try:
                    p = Sexo.objects.get(pk=id_sexo)
                except Sexo.DoesNotExist:
                    raise Http404
                mensaje = {"status": "True", "item_id": p.id, "form": "del"}
                p.delete()

                # Elinamos objeto de la base de datos
                messages.success(request, "Se elimino el registro.")
                return HttpResponse(json.dumps(mensaje), content_type='application/json')

            except django.db.IntegrityError:

                mensaje = {"status": "False",
                           "form": "del",
                           "msj": "No se puede eliminar porque tiene algun registro asociado"}
                messages.success(request, "No se puede eliminar porque tiene algun registro asociado.")
                return HttpResponse(json.dumps(mensaje), content_type='application/json')

            except:
                mensaje = {"status": "False", "form": "del", "msj": "Error al eliminar"}
                messages.success(request, "Error al eliminar.")
                return HttpResponse(json.dumps(mensaje), content_type='application/json')

        search_text = request.POST['search_text']
        if search_text is not None and search_text != u"":
            entry_query = get_query(search_text, ['sexo', ])
            lista_sexo = Sexo.objects.filter(entry_query)
        else:
            lista_sexo = Sexo.objects.all()

    paginator = Paginator(lista_sexo, nropag[0]['valor'])
    # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        sexos = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        sexos = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        sexos = paginator.page(paginator.num_pages)

    context = {'lista_sexo': lista_sexo, 'sexos': sexos}
    return render_to_response('sexo_lista_search.html', context)


def lista_estadocivil(request):
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
                id_estadocivil = request.POST['item_id']
                try:
                    p = Estado_civil.objects.get(pk=id_estadocivil)
                except Estado_civil.DoesNotExist:
                    raise Http404
                mensaje = {"status": "True", "item_id": p.id, "form": "del"}
                p.delete()

                 # Elinamos objeto de la base de datos
                messages.success(request, "Se elimino el registro.")
                return HttpResponse(json.dumps(mensaje), content_type='application/json')

            except django.db.IntegrityError:

                mensaje = {"status": "False",
                           "form": "del",
                           "msj": "No se puede eliminar porque tiene algun registro asociado"}
                messages.success(request, "No se puede eliminar porque tiene algun registro asociado.")
                return HttpResponse(json.dumps(mensaje), content_type='application/json')

            except:  # ERROR requiere definir un tipo de error para la excepción
                mensaje = {"status": "False", "form": "del", "msj": "Error al eliminar"}
                messages.success(request, "Error al eliminar.")
                return HttpResponse(json.dumps(mensaje), content_type='application/json')

    order_by = request.GET.get('order_by')
    if order_by:
        lista_estadocivil = Estado_civil.objects.all().order_by(order_by)
    else:
        lista_estadocivil = Estado_civil.objects.all()

    paginator = Paginator(lista_estadocivil, nropag[0]['valor'])
    # Show 25 contacts per page
    page = request.GET.get('page')
    if page == '0':
        estadoscivil = lista_estadocivil
    else:
        try:
            estadoscivil = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            estadoscivil = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            estadoscivil = paginator.page(paginator.num_pages)

    context = {'lista_estadocivil': lista_estadocivil, 'estadoscivil': estadoscivil}

    return render(request, 'estadocivil_lista.html', context)


def search_estadocivil(request):
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
                id_estadocivil = request.POST['item_id']
                try:
                    p = Estado_civil.objects.get(pk=id_estadocivil)
                except Estado_civil.DoesNotExist:
                    raise Http404
                mensaje = {"status": "True", "item_id": p.id, "form": "del"}
                p.delete()

                 # Elinamos objeto de la base de datos
                messages.success(request, "Se elimino el registro.")
                return HttpResponse(json.dumps(mensaje), content_type='application/json')

            except django.db.IntegrityError:

                mensaje = {"status": "False",
                           "form": "del",
                           "msj": "No se puede eliminar porque tiene algun registro asociado"}
                messages.success(request, "No se puede eliminar porque tiene algun registro asociado.")
                return HttpResponse(json.dumps(mensaje), content_type='application/json')

            except:  # ERROR requiere definir un tipo de error para la excepción
                mensaje = {"status": "False", "form": "del", "msj": "Error al eliminar"}
                messages.success(request, "Error al eliminar.")
                return HttpResponse(json.dumps(mensaje), content_type='application/json')

        search_text = request.POST['search_text']
        if search_text is not None and search_text != u"":
            entry_query = get_query(search_text, ['estado_civil', ])
            lista_estadocivil = Estado_civil.objects.filter(entry_query)
        else:
            lista_estadocivil = Estado_civil.objects.all()

    paginator = Paginator(lista_estadocivil, nropag[0]['valor'])
    # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        estadoscivil = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        estadoscivil = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        estadoscivil = paginator.page(paginator.num_pages)

    context = {'lista_estadocivil': lista_estadocivil, 'estadoscivil': estadoscivil}
    return render_to_response('estadocivil_lista_search.html', context)


def lista_cliente(request):
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
                id_cliente = request.POST['item_id']
                try:
                    p = Cliente.objects.get(pk=id_cliente)
                except Cliente.DoesNotExist:
                    raise Http404
                mensaje = {"status": "True", "item_id": p.id, "form": "del"}
                p.delete()

                 # Elinamos objeto de la base de datos
                messages.success(request, "Se elimino el registro.")
                return HttpResponse(json.dumps(mensaje), content_type='application/json')

            except django.db.IntegrityError:

                mensaje = {"status": "False",
                           "form": "del",
                           "msj": "No se puede eliminar porque tiene algun registro asociado"}
                messages.success(request, "No se puede eliminar porque tiene algun registro asociado.")
                return HttpResponse(json.dumps(mensaje), content_type='application/json')

            except:
                mensaje = {"status": "False", "form": "del", "msj": "Error al eliminar."}
                messages.success(request, "Error al eliminar.")
                return HttpResponse(json.dumps(mensaje), content_type='application/json')
    order_by = request.GET.get('order_by')
    if order_by:
        lista_cliente = Cliente.objects.all().order_by(order_by)
    else:
        lista_cliente = Cliente.objects.all()

    paginator = Paginator(lista_cliente, nropag[0]['valor'])
    # Show 25 contacts per page
    page = request.GET.get('page')
    if page == '0':
        clientes = lista_cliente
    else:
        try:
            clientes = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            clientes = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            clientes = paginator.page(paginator.num_pages)

    context = {'lista_cliente': lista_cliente, 'clientes': clientes}
    return render(request, 'cliente_lista.html', context)


def search_cliente(request):
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
                id_cliente = request.POST['item_id']
                try:
                    p = Cliente.objects.get(pk=id_cliente)
                except Cliente.DoesNotExist:
                    raise Http404
                mensaje = {"status": "True", "item_id": p.id, "form": "del"}
                p.delete()

                 # Elinamos objeto de la base de datos
                messages.success(request, "Se elimino el registro.")
                return HttpResponse(json.dumps(mensaje), content_type='application/json')

            except django.db.IntegrityError:

                mensaje = {"status": "False",
                           "form": "del",
                           "msj": "No se puede eliminar porque tiene algun registro asociado"}
                messages.success(request, "No se puede eliminar porque tiene algun registro asociado.")
                return HttpResponse(json.dumps(mensaje), content_type='application/json')

            except:
                mensaje = {"status": "False", "form": "del", "msj": "Error al eliminar."}
                messages.success(request, "Error al eliminar.")
                return HttpResponse(json.dumps(mensaje), content_type='application/json')

        search_text = request.POST['search_text']
        if search_text is not None and search_text != u"":
            entry_query = get_query(search_text, ['nombre_principal', 'dni', 'sexo__sexo', ])
            lista_cliente = Cliente.objects.filter(entry_query)
        else:
            lista_cliente = Cliente.objects.all()

    paginator = Paginator(lista_cliente, nropag[0]['valor'])
    # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        clientes = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        clientes = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        clientes = paginator.page(paginator.num_pages)

    context = {'lista_cliente': lista_cliente, 'clientes': clientes}
    return render_to_response('cliente_lista_search.html', context)


def lista_email(request, id_cli):
    """docstring"""
    if request.method == "POST":
        if "item_id" in request.POST:
            try:
                id_email = request.POST['item_id']
                try:
                    p = Email.objects.get(pk=id_email)
                except Email.DoesNotExist:
                    raise Http404
                mensaje = {"status": "True", "item_id": p.id, "form": "del"}
                p.delete()

                 # Elinamos objeto de la base de datos
                messages.success(request, "Se elimino el registro.")
                return HttpResponse(json.dumps(mensaje), content_type='application/json')

            except django.db.IntegrityError:

                mensaje = {"status": "False", "form": "del",
                           "msj": "No se puede eliminar porque tiene algun registro asociado"}
                messages.success(request, "No se puede eliminar porque tiene algun registro asociado.")
                return HttpResponse(json.dumps(mensaje), content_type='application/json')

            except:
                mensaje = {"status": "False", "form": "del", "msj": "Error al eliminar."}
                messages.success(request, "Error al eliminar.")
                return HttpResponse(json.dumps(mensaje), content_type='application/json')

    cliente = Cliente.objects.get(id=id_cli)

    lista_email = Email.objects.filter(cliente_id=cliente)
    context = {'lista_email': lista_email, 'id_cli': id_cli}
    return render(request, 'emailcliente_lista.html', context)


def lista_telefono_cliente(request, id_cli):
    """docstring"""
    if request.method == "POST":
        if "item_id" in request.POST:
            try:
                id_telefono = request.POST['item_id']
                try:
                    p = Telefono.objects.get(pk=id_telefono)
                except Telefono.DoesNotExist:
                    raise Http404
                mensaje = {"status": "True", "item_id": p.id, "form": "del"}
                p.delete()

                 # Elinamos objeto de la base de datos
                messages.success(request, "Se elimino el registro.")
                return HttpResponse(json.dumps(mensaje), content_type='application/json')

            except django.db.IntegrityError:

                mensaje = {"status": "False",
                           "form": "del",
                           "msj": "No se puede eliminar porque tiene algun registro asociado"}
                messages.success(request, "No se puede eliminar porque tiene algun registro asociado.")
                return HttpResponse(json.dumps(mensaje), content_type='application/json')

            except:
                mensaje = {"status": "False", "form": "del", "msj": "Error al eliminar."}
                messages.success(request, "Error al eliminar.")
                return HttpResponse(json.dumps(mensaje), content_type='application/json')

    cliente = Cliente.objects.get(id=id_cli)

    lista_telefono_cliente = Telefono.objects.select_related().filter(cliente=cliente)

    context = {'lista_telefono_cliente': lista_telefono_cliente, 'id_cli': id_cli}
    return render(request, 'telefonocliente_lista.html', context)


def lista_direccioncliente(request, id_cli):
    """docstring"""
    if request.method == "POST":
        if "item_id" in request.POST:
            try:
                id_direccion = request.POST['item_id']
                try:
                    p = Direccion.objects.get(pk=id_direccion)
                except Direccion.DoesNotExist:
                    raise Http404
                mensaje = {"status": "True", "item_id": p.id, "form": "del"}
                p.delete()

                 # Elinamos objeto de la base de datos
                messages.success(request, "Se elimino el registro.")
                return HttpResponse(json.dumps(mensaje), content_type='application/json')

            except django.db.IntegrityError:

                mensaje = {"status": "False",
                           "form": "del",
                           "msj": "No se puede eliminar porque tiene algun registro asociado"}
                messages.success(request, "Error al eliminar.")
                return HttpResponse(json.dumps(mensaje), content_type='application/json')

            except:
                mensaje = {"status": "False", "form": "del", "msj": "Error al eliminar."}
                messages.success(request, "Error al eliminar.")
                return HttpResponse(json.dumps(mensaje), content_type='application/json')

    cliente = Cliente.objects.get(id=id_cli)

    direccioncliente_lista = Direccion.objects.filter(cliente=cliente)

    context = {'direccioncliente_lista': direccioncliente_lista, 'id_cli': id_cli}
    return render(request, 'direccioncliente_lista.html', context)


def lista_tipo_cliente(request):
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
                id_tipocliente = request.POST['item_id']
                try:
                    p = TipoCliente.objects.get(pk=id_tipocliente)
                except TipoCliente.DoesNotExist:
                    raise Http404
                mensaje = {"status": "True", "item_id": p.id, "form": "del"}
                p.delete()

                 # Elinamos objeto de la base de datos
                messages.success(request, "Se elimino el registro.")
                return HttpResponse(json.dumps(mensaje), content_type='application/json')

            except django.db.IntegrityError:

                mensaje = {"status": "False",
                           "form": "del",
                           "msj": "No se puede eliminar porque tiene algun registro asociado"}
                messages.success(request, "No se puede eliminar porque tiene algun registro asociado.")
                return HttpResponse(json.dumps(mensaje), content_type='application/json')

            except:
                mensaje = {"status": "False", "form": "del", "msj": "Error al eliminar."}
                messages.success(request, "Error al eliminar.")
                return HttpResponse(json.dumps(mensaje), content_type='application/json')
    order_by = request.GET.get('order_by')
    if order_by:
        lista_tipo_cliente = TipoCliente.objects.all().order_by(order_by)
    else:
        lista_tipo_cliente = TipoCliente.objects.all()

    paginator = Paginator(lista_tipo_cliente, nropag[0]['valor'])
    # Show 25 contacts per page
    page = request.GET.get('page')
    if page == '0':
        tipo_clientes = lista_tipo_cliente
    else:
        try:
            tipo_clientes = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            tipo_clientes = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            tipo_clientes = paginator.page(paginator.num_pages)

    context = {'lista_tipo_cliente': lista_tipo_cliente, 'tipo_clientes': tipo_clientes}
    return render(request, 'tipocliente_lista.html', context)


def search_tipo_cliente(request):
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
                id_tipocliente = request.POST['item_id']
                try:
                    p = TipoCliente.objects.get(pk=id_tipocliente)
                except TipoCliente.DoesNotExist:
                    raise Http404
                mensaje = {"status": "True", "item_id": p.id, "form": "del"}
                p.delete()

                 # Elinamos objeto de la base de datos
                messages.success(request, "Se elimino el registro.")
                return HttpResponse(json.dumps(mensaje), content_type='application/json')

            except django.db.IntegrityError:

                mensaje = {"status": "False",
                           "form": "del",
                           "msj": "No se puede eliminar porque tiene algun registro asociado"}
                messages.success(request, "No se puede eliminar porque tiene algun registro asociado.")
                return HttpResponse(json.dumps(mensaje), content_type='application/json')

            except:
                mensaje = {"status": "False", "form": "del", "msj": "Error al eliminar."}
                messages.success(request, "Error al eliminar.")
                return HttpResponse(json.dumps(mensaje), content_type='application/json')

        search_text = request.POST['search_text']
        if search_text is not None and search_text != u"":
            entry_query = get_query(search_text, ['nombre_principal', 'dni', 'sexo__sexo', ])
            lista_tipo_cliente = TipoCliente.objects.filter(entry_query)
        else:
            lista_tipo_cliente = TipoCliente.objects.all()

    paginator = Paginator(lista_tipo_cliente, nropag[0]['valor'])
    # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        tipo_clientes = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        tipo_clientes = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        tipo_clientes = paginator.page(paginator.num_pages)

    context = {'lista_tipo_cliente': lista_tipo_cliente, 'tipo_clientes': tipo_clientes}
    return render_to_response('tipocliente_lista_search.html', context)


# agregar nuevo
def add_cliente(request):
    mensaje = ''
    if request.method == 'POST':
        try:
            cliente_form = ClienteForm(request.POST)

            if cliente_form.is_valid():
                id_reg = cliente_form.save()

                if 'regEdit' in request.POST:
                    messages.success(request, "Registro guardado.")
                    return HttpResponseRedirect(reverse('uclientes:edit_cliente',
                                                        args=(id_reg.id,)))
                else:
                    mensaje = 'Se ha guardado la información del cliente'
                    return HttpResponseRedirect(reverse('uclientes:lista_cliente'))

        except Exception as ex:
            cliente_form = ClienteForm()
            mensaje = "se ha producido un error"+str(ex)

    else:
        cliente_form = ClienteForm()

    return render_to_response('cliente_add.html',
                              {'cliente_form': cliente_form, 'create': True, 'mensaje': mensaje},
                              context_instance=RequestContext(request))


def add_sexo(request):

    if request.method == 'POST':
        try:
            sexo_form = SexoForm(request.POST)

            if sexo_form.is_valid():
                id_reg = sexo_form.save()

                if 'regEdit' in request.POST:
                    messages.success(request, "Registro guardado.")
                    return HttpResponseRedirect(reverse('uclientes:edit_sexo',
                                                        args=(id_reg.id,)))
                else:
                    return HttpResponseRedirect(reverse('uclientes:lista_sexo'))

        except Exception as ex:
            sexo_form = SexoForm()
            mensaje = "se ha producido un error"+str(ex)

    else:
        sexo_form = SexoForm()
        mensaje = ''

    return render_to_response('sexo_add.html',
                              {'sexo_form': sexo_form, 'create': True, 'mensaje': mensaje},
                              context_instance=RequestContext(request))


def add_estadocivil(request):

    if request.method == 'POST':
        try:
            estadocivil_form = EstadoCivilForm(request.POST)

            if estadocivil_form.is_valid():
                id_reg = estadocivil_form.save()

                if 'regEdit' in request.POST:
                    messages.success(request, "Registro guardado.")
                    return HttpResponseRedirect(reverse('uclientes:edit_estado_civil',
                                                        args=(id_reg.id,)))
                else:
                    return HttpResponseRedirect(reverse('uclientes:lista_estadocivil'))

        except Exception as ex:
            estadocivil_form = EstadoCivilForm()
            mensaje = "se ha producido un error"+str(ex)

    else:
        estadocivil_form = EstadoCivilForm()
        mensaje = ''

    return render_to_response('estadocivil_add.html',
                              {'estadocivil_form': estadocivil_form, 'create': True, 'mensaje': mensaje},
                              context_instance=RequestContext(request))


def add_email(request, id_cli):

    if request.method == 'POST':
        try:
            email_form = EmailForm(request.POST)
            if email_form.is_valid():
                id_reg = email_form.save()
                id_cli = Email.objects.get(id=id_reg.id)

                if 'regEdit' in request.POST:
                    messages.success(request, "Registro guardado.")
                    return HttpResponseRedirect(reverse('uclientes:edit_email',
                                                        args=(id_reg.id,)))
                else:
                    return HttpResponseRedirect(reverse('uclientes:ficha_cliente', args=(id_cli.cliente.id,)))

        except Exception as ex:
            mensaje = "se ha producido un error"+str(ex)
            email_form = EmailForm()

    else:
        email_form = EmailForm(initial={'cliente': id_cli})
        mensaje = ''

    return render_to_response('Emailcliente_add.html',
                              {'email_form': email_form, 'create': True, 'mensaje': mensaje},
                              context_instance=RequestContext(request))


def add_tipocliente(request):
    mensaje = ''
    if request.method == 'POST':
        try:
            tipocliente_form = TipoClienteForm(request.POST)

            if tipocliente_form.is_valid():
                id_reg = tipocliente_form.save()

                if 'regEdit' in request.POST:
                    messages.success(request, "Registro guardado.")
                    return HttpResponseRedirect(reverse('uclientes:edit_tipocliente',
                                                        args=(id_reg.id,)))
                else:
                    mensaje = 'Se ha guardado la información del tipo de cliente'
                    return HttpResponseRedirect(reverse('uclientes:lista_tipo_cliente'))

        except Exception as ex:
            tipocliente_form = TipoClienteForm()
            mensaje = "se ha producido un error"+str(ex)

    else:
        tipocliente_form = TipoClienteForm()

    return render_to_response('tipocliente_add.html',
                              {'tipocliente_form': tipocliente_form, 'create': True, 'mensaje': mensaje},
                              context_instance=RequestContext(request))


# editar un registro
def edit_cliente(request, pk):

    redirect_to = request.REQUEST.get('next', '')

    try:
        id_clie = Cliente.objects.get(pk=pk)
    except ObjectDoesNotExist as ex:
        mensaje = "El cliente no existe"
    except Exception as ex:
        mensaje = "se ha producido un error"+str(ex)

    if request.method == 'POST':
        mensaje = ""
        # formulario enviado
        editar_clie = ClienteForm(request.POST, instance=id_clie)

        if editar_clie.is_valid():
            # formulario validado correctamente
            editar_clie.save()

            if 'regEdit' in request.POST:
                messages.success(request, "Registro guardado.")
                return HttpResponseRedirect(request.get_full_path())
            else:
                if redirect_to:
                    return HttpResponseRedirect(redirect_to)
                else:
                    return HttpResponseRedirect(reverse('uclientes:ficha_cliente',
                                                        args=(id_clie.id,)))
    else:
        # formulario inicial
        editar_clie = ClienteForm(instance=id_clie)
        mensaje = ""
    return render_to_response('cliente_edit.html',
                              {'editar_clie': editar_clie, 'id_cli': pk, 'create': False, 'mensaje': mensaje},
                              context_instance=RequestContext(request))


def edit_email(request, id_cli, pk):

    id_email = Email.objects.get(pk=pk)

    if request.method == 'POST':
        # formulario enviado
        form_edit_email = EmailForm(request.POST, instance=id_email)

        if form_edit_email.is_valid():
            # formulario validado correctamente
            form_edit_email.save()
            if 'regEdit' in request.POST:
                messages.success(request, "Registro guardado.")
                return HttpResponseRedirect(request.get_full_path())
            else:
                return HttpResponseRedirect('../../../')
    else:
        # formulario inicial
        form_edit_email = EmailForm(instance=id_email)

    return render_to_response('emailcliente_edit.html',
                              {'form_edit_email': form_edit_email, 'create': False},
                              context_instance=RequestContext(request))


def edit_sexo(request, pk):
    """docstring"""
    sexo = Sexo.objects.get(pk=pk)

    if request.method == 'POST':
        # formulario enviado
        form_edit_sexo = SexoForm(request.POST, instance=sexo)

        if form_edit_sexo.is_valid():
            # formulario validado correctamente
            form_edit_sexo.save()
            if 'regEdit' in request.POST:
                messages.success(request, "Registro guardado.")
                return HttpResponseRedirect(request.get_full_path())
            else:
                return HttpResponseRedirect(reverse('uclientes:lista_sexo'))

    else:
        # formulario inicial
        form_edit_sexo = SexoForm(instance=sexo)

    return render_to_response('sexo_edit.html',
                              {'form_edit_sexo': form_edit_sexo, 'create': False},
                              context_instance=RequestContext(request))


def edit_estado_civil(request, pk):
    """docstring"""
    estado_civil = Estado_civil.objects.get(pk=pk)

    if request.method == 'POST':
        # formulario enviado
        form_edit_estadocivil = EstadoCivilForm(request.POST, instance=estado_civil)

        if form_edit_estadocivil.is_valid():
            # formulario validado correctamente
            form_edit_estadocivil.save()
            if 'regEdit' in request.POST:
                messages.success(request, "Registro guardado.")
                return HttpResponseRedirect(request.get_full_path())
            else:
                return HttpResponseRedirect(reverse('uclientes:lista_estadocivil'))

    else:
        # formulario inicial
        form_edit_estadocivil = EstadoCivilForm(instance=estado_civil)

    return render_to_response('estadocivil_edit.html',
                              {'form_edit_estadocivil': form_edit_estadocivil, 'create': False},
                              context_instance=RequestContext(request))


def edit_tipocliente(request, pk):

    redirect_to = request.REQUEST.get('next', '')

    try:
        id_tipocliente = TipoCliente.objects.get(pk=pk)
    except ObjectDoesNotExist as ex:
        mensaje = "El tipo de cliente no existe"
    except Exception as ex:
        mensaje = "se ha producido un error"+str(ex)

    if request.method == 'POST':
        # formulario enviado
        editar_tipocliente = TipoClienteForm(request.POST, instance=id_tipocliente)

        if editar_tipocliente.is_valid():
            # formulario validado correctamente
            editar_tipocliente.save()
            if 'regEdit' in request.POST:
                messages.success(request, "Registro guardado.")
                return HttpResponseRedirect(request.get_full_path())
            else:
                if redirect_to:
                    return HttpResponseRedirect(redirect_to)
                else:
                    return HttpResponseRedirect(reverse('uclientes:lista_tipo_cliente'))
    else:
        # formulario inicial
        editar_tipocliente = TipoClienteForm(instance=id_tipocliente)
        mensaje = ""
    return render_to_response('tipocliente_edit.html',
                              {'editar_tipocliente': editar_tipocliente, 'id_tipocli': pk, 'create': False, 'mensaje': mensaje},
                              context_instance=RequestContext(request))


def ficha_cliente(request, pk):

    lista_cliente = Cliente.objects.filter(pk=pk)
    lista_email = Email.objects.filter(cliente_id=pk)
    lista_telefono_cliente = Telefono.objects.filter(cliente=pk)
    direccioncliente_lista = Direccion.objects.filter(cliente=pk)
    lista_cotizacion = Cotizacion.objects.all()

    context = {
        'lista_cliente': lista_cliente,
        'lista_email': lista_email,
        'lista_telefono_cliente': lista_telefono_cliente,
        'direccioncliente_lista': direccioncliente_lista,
        'lista_cotizacion': lista_cotizacion
        }
    return render(request, 'cliente_ficha.html', context)


# eliminar un registro
def delete_email2(request, id_cli, pk, template_name='tipo_clienteserver_confirm_delete.html'):
    email = get_object_or_404(Email, pk=pk)
    if request.method == 'POST':
        email.delete()
        return HttpResponseRedirect(reverse('uclientes:ficha_cliente', args=(id_cli,)))
    return render(request, template_name, {'object': email})


def delete_telefono(request, id_cli):
    cod = request.GET.get('codigo', '')

    if cod:
        try:
            p = Telefono.objects.get(id=cod)
        except Telefono.DoesNotExist:
            raise Http404
        p.delete()
        messages.success(request, "Se elimino el registro.")
        return render_to_response('cliente_ficha.html', {"cod": cod, "exito": True})
    return render_to_response('cliente_ficha.html')


def delete_direccion(request, id_cli):
    cod = request.GET.get('codigo', '')

    if cod:
        try:
            p = Direccion.objects.get(id=cod)
        except Direccion.DoesNotExist:
            raise Http404
        p.delete()
        messages.success(request, "Se elimino el registro.")
        return render_to_response('cliente_ficha.html', {"cod": cod, "exito": True})
    return render_to_response('cliente_ficha.html')


def delete_email(request, id_cli):
    cod = request.GET.get('codigo', '')
    if cod:
        try:
            p = Email.objects.get(id=cod)
        except Email.DoesNotExist:
            raise Http404
        p.delete()
        messages.success(request, "Se elimino el registro.")
        return render_to_response('cliente_ficha.html', {"cod": cod, "exito": True})
    return render_to_response('cliente_ficha.html')
