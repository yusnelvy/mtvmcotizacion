from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, JsonResponse
from django.core.urlresolvers import reverse
from gestiondocumento.models import Estado, EstadoDocumento
from gestiondocumento.forms import EstadoForm, EstadoDocumentoForm
from premisas.models import PerzonalizacionVisual
from mtvmcotizacion.views import get_query
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView, DetailView, View, UpdateView, DeleteView
from django.contrib import messages
from django.db import transaction
import sys
import traceback


# Create your views here.
class EstadoList(ListView):
    model = Estado
    paginate_by = 10
    context_object_name = 'estados'
    template_name = 'estado_lista.html'

    def get_paginate_by(self, queryset):
        if self.request.user.id is not None:
            try:
                nropag = PerzonalizacionVisual.objects.values('valor').filter(usuario=
                                                                              self.request.user.id,
                                                                              tipo="paginacion")
            except PerzonalizacionVisual.DoesNotExist:
                nropag = PerzonalizacionVisual.objects.values('valor').filter(usuario="std",
                                                                              tipo="paginacion")
        else:
            nropag = PerzonalizacionVisual.objects.values('valor').filter(usuario="std",
                                                                          tipo="paginacion")

        page = self.request.GET.get('page')
        if page == '0':
            return None
        else:
            return self.request.GET.get('paginate_by', nropag[0]['valor'])

    def get_queryset(self):

        order_by = self.request.GET.get('order_by')
        if order_by:
            queryset = Estado.objects.all().order_by(order_by)
        else:
            queryset = Estado.objects.all()

        return queryset


def search_estado(request):
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

        search_text = request.POST['search_text']
        if search_text is not None and search_text != u"":
            entry_query = get_query(search_text, ['estado', ])
            estados = Estado.objects.filter(entry_query)
        else:
            estados = Estado.objects.all()

    paginator = Paginator(estados, nropag[0]['valor'])
    # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        page_obj = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        page_obj = paginator.page(paginator.num_pages)

    context = {'estados': estados, 'page_obj': page_obj}
    return render_to_response('estado_lista_search.html', context)


class EstadoDocumentoList(ListView):
    model = EstadoDocumento
    paginate_by = 10
    context_object_name = 'estadodocumentos'
    template_name = 'estadodocumento_lista.html'

    def get_paginate_by(self, queryset):
        if self.request.user.id is not None:
            try:
                nropag = PerzonalizacionVisual.objects.values('valor').filter(usuario=
                                                                              self.request.user.id,
                                                                              tipo="paginacion")
            except PerzonalizacionVisual.DoesNotExist:
                nropag = PerzonalizacionVisual.objects.values('valor').filter(usuario="std",
                                                                              tipo="paginacion")
        else:
            nropag = PerzonalizacionVisual.objects.values('valor').filter(usuario="std",
                                                                          tipo="paginacion")

        page = self.request.GET.get('page')
        if page == '0':
            return None
        else:
            return self.request.GET.get('paginate_by', nropag[0]['valor'])

    def get_queryset(self):

        order_by = self.request.GET.get('order_by')
        if order_by:
            queryset = EstadoDocumento.objects.all().order_by(order_by)
        else:
            queryset = EstadoDocumento.objects.all()

        return queryset


def search_estadodocumento(request):
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

        search_text = request.POST['search_text']
        if search_text is not None and search_text != u"":
            entry_query = get_query(search_text, ['estado', 'documento', ])
            estadodocumentos = EstadoDocumento.objects.filter(entry_query)
        else:
            estadodocumentos = EstadoDocumento.objects.all()

    paginator = Paginator(estadodocumentos, nropag[0]['valor'])
    # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        page_obj = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        page_obj = paginator.page(paginator.num_pages)

    context = {'estadodocumentos': estadodocumentos, 'page_obj': page_obj}
    return render_to_response('estadodocumento_lista_search.html', context)


class EstadoView(View):
    form_class = EstadoForm
    template_name = 'estado_add.html'

    def get(self, request, *args, **kwargs):
        """docstring"""
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            # <process form cleaned data>
            messages.success(self.request, "Estado registrado.")
            return HttpResponseRedirect(reverse('ugestiondocumentos:EstadoList'))

        return render(request, self.template_name, {'form': form})


class EstadoDocumentoView(View):
    form_class = EstadoDocumentoForm
    template_name = 'estadodocumento_add.html'

    def get(self, request, *args, **kwargs):
        """docstring"""
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            # <process form cleaned data>
            messages.success(self.request, "Estado de documento registrado.")
            return HttpResponseRedirect(reverse('ugestiondocumentos:EstadoDocumentoList'))

        return render(request, self.template_name, {'form': form})


class EstadoUpdate(UpdateView):
    template_name = 'estado_edit.html'
    form_class = EstadoForm
    model = Estado

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()

        redirect_to = self.request.GET['next']
        if redirect_to:
            return HttpResponseRedirect(redirect_to)
        else:
            return render_to_response(self.template_name, self.get_context_data())


class EstadoDocumentoUpdate(UpdateView):
    template_name = 'estadodocumento_edit.html'
    form_class = EstadoDocumentoForm
    model = EstadoDocumento

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()

        redirect_to = self.request.GET['next']
        if redirect_to:
            return HttpResponseRedirect(redirect_to)
        else:
            return render_to_response(self.template_name, self.get_context_data())


class EstadoDelete(DeleteView):
    model = Estado
    form_class = EstadoForm
    template_name = 'server_confirm_delete.html'

    @transaction.atomic
    def delete(self, request, *args, **kwargs):
        sql = transaction.savepoint()
        try:
            self.obj = self.get_object()
            #self.obj.activo = 'Anulado'
            self.obj.delete()

            transaction.savepoint_commit(sql)
            mensaje = {'estatus': 'ok', 'msj': 'Registro eliminado'}
            return JsonResponse(mensaje, safe=False)
        except:
            transaction.savepoint_rollback(sql)

            tb = sys.exc_info()[2]
            tbinfo = traceback.format_tb(tb)[0]
            mensaje = {'estatus': 'error', 'msj': 'Ocurrio un error : ' + str(tb) + ' ' + str(tbinfo)}
            return JsonResponse(mensaje, safe=False)


class EstadoDocumentoDelete(DeleteView):
    model = EstadoDocumento
    form_class = EstadoDocumentoForm
    template_name = 'server_confirm_delete.html'

    @transaction.atomic
    def delete(self, request, *args, **kwargs):
        sql = transaction.savepoint()
        try:
            self.obj = self.get_object()
            #self.obj.activo = 'Anulado'
            self.obj.delete()

            transaction.savepoint_commit(sql)
            mensaje = {'estatus': 'ok', 'msj': 'Registro eliminado'}
            return JsonResponse(mensaje, safe=False)
        except:
            transaction.savepoint_rollback(sql)

            tb = sys.exc_info()[2]
            tbinfo = traceback.format_tb(tb)[0]
            mensaje = {'estatus': 'error',
                       'msj': 'Ocurrio un error : ' + str(tb) + ' ' + str(tbinfo)}
            return JsonResponse(mensaje, safe=False)
