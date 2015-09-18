"""Doctsring"""
from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
from django.views.generic import ListView, DetailView, View, UpdateView, DeleteView
from presupuesto.models import Presupuesto, Presupuesto_Detalle, \
    Presupuesto_direccion, Presupuesto_servicio, DatosPrecargado
from presupuesto.forms import PresupuestoForm, \
    PresupuestoDireccionForm, PresupuestoDetalleForm, \
    PresupuestoServicioForm, DatosPrecargadoForm, PresupuestoRevisarForm
from django.core.urlresolvers import reverse
from django.utils import timezone
from direccion.models import Complejidad_Inmueble, Tipo_Inmueble
from mueble.models import Ocupacion, Mueble, Tamano_Mueble, Tamano
from ambiente.models import Ambiente
from servicio.models import Servicio, Complejidad_Servicio, Material, Servicio_Material
from contenido.models import Contenido_Tipico, Contenido_Servicio
from cotizacion.models import Vehiculo
from trabajador.models import Cargo_trabajador
from premisas.models import Empresa
from inicio.email import Email

from formtools.wizard.views import SessionWizardView
from django.forms.formsets import formset_factory

from django.db.models import Count, Sum
from decimal import Decimal

from io import BytesIO

from django.http import HttpResponse
from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table


class ContactWizard(SessionWizardView):
    def get_form(self, step=None, data=None, files=None):
        form = super(ContactWizard, self).get_form(step, data, files)

        # determine the step if not given
        if step is None:
            step = self.steps.current

        if step == '2':
            form.lista_tamano = self.form_list
        return form

    def done(self, form_list, **kwargs):
        return render_to_response('presupuestodetalle_add.html', {
            'form_data': [form.cleaned_data for form in form_list],
        })


# Create your views here.
class PresupuestoList(ListView):
    model = Presupuesto
    paginate_by = 10
    context_object_name = 'presupuestos'
    template_name = 'presupuesto_lista.html'

    def get_queryset(self):
        queryset = super(PresupuestoList, self).get_queryset()
        return queryset.filter()


class PresupuestoDetail(DetailView):

    model = Presupuesto
    context_object_name = "presupuesto"
    template_name = 'presupuesto_ficha.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(PresupuestoDetail, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['detalle_list'] = Presupuesto_Detalle.objects.filter(
            presupuesto=self.object.pk)
        context['lista_ambiente'] = Presupuesto_Detalle.objects.filter(
            presupuesto=self.object.pk).values('ambiente').annotate(
            tcount=Count('ambiente')).order_by('ambiente')
        context['direccion_origen'] = Presupuesto_direccion.objects.filter(
            presupuesto=self.object.pk, tipo_direccion="Origen")
        context['direccion_destino'] = Presupuesto_direccion.objects.filter(
            presupuesto=self.object.pk, tipo_direccion="Destino")
        context['now'] = timezone.now()
        context['servicio'] = Presupuesto_servicio.objects.filter(
            detalle_presupuesto__presupuesto=self.object.pk).values(
            'servicio', 'detalle_presupuesto', 'monto_servicio').annotate(
            tcount=Count('servicio')).order_by('servicio')
        return context


class PresupuestoDireccionOrigenDetail(DetailView):

    model = Presupuesto
    context_object_name = "presupuesto"
    template_name = 'presupuestodireccion_origen.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(PresupuestoDireccionOrigenDetail, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['direccion_origen'] = Presupuesto_direccion.objects.filter(presupuesto=self.object.pk, tipo_direccion="Origen")
        return context


class PresupuestoDatosPersonales(DetailView):

    model = Presupuesto
    context_object_name = "presupuesto"
    template_name = 'presupuesto_det.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(PresupuestoDatosPersonales, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        return context


class PresupuestoDireccionDestinoDetail(DetailView):

    model = Presupuesto
    context_object_name = "presupuesto"
    template_name = 'presupuestodireccion_destino.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(PresupuestoDireccionDestinoDetail, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['direccion_destino'] = Presupuesto_direccion.objects.filter(presupuesto=self.object.pk, tipo_direccion="Destino")
        return context


class PresupuestoDetalleDetail2(DetailView):

    model = Presupuesto
    context_object_name = "presupuesto"
    template_name = 'presupuestodetalle_det.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(PresupuestoDetalleDetail2, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        #context['listar_ambiente'] = Presupuesto_Detalle.objects.values('ambiente', 'ambiente__ambiente', 'mueble').annotate(tcount=Count('ambiente')).order_by('ambiente')
        context['detalle_list'] = Presupuesto_Detalle.objects.filter(presupuesto=self.object.pk)
        context['lista_ambiente'] = Presupuesto_Detalle.objects.filter(presupuesto=self.object.pk).values('ambiente').annotate(tcount=Count('ambiente')).order_by('ambiente')
        context['servicio'] = Presupuesto_servicio.objects.filter(detalle_presupuesto__presupuesto=self.object.pk).values('servicio', 'detalle_presupuesto', 'monto_servicio').annotate(tcount=Count('servicio')).order_by('servicio')
        return context


class PresupuestoDetalleList(ListView):
    model = Presupuesto_Detalle
    paginate_by = 25
    template_name = 'presupuestodetalle_lista.html'

    def get_queryset(self):
        queryset = super(PresupuestoDetalleList, self).get_queryset()
        return queryset.filter()


class PresupuestoDetalleDetail(DetailView):

    model = Presupuesto_Detalle
    template_name = 'presupuestodetalle_ficha.html'
    context_object_name = "detallepresupuesto"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(PresupuestoDetalleDetail, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['servicio_list'] = Presupuesto_servicio.objects.filter(detalle_presupuesto=self.object.pk)
        context['servicio'] = Presupuesto_servicio.objects.filter(detalle_presupuesto=self.object.pk).values('servicio', 'detalle_presupuesto', 'detalle_presupuesto__mueble', 'monto_servicio').annotate(tcount=Count('servicio')).order_by('servicio')
        return context


class PresupuestoDetalleServicioDetail(DetailView):

    model = Presupuesto_Detalle
    template_name = 'presupuestoservivio_det.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(PresupuestoDetalleServicioDetail, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['servicio_list'] = Presupuesto_servicio.objects.filter(detalle_presupuesto=self.object.pk)
        context['servicio'] = Presupuesto_servicio.objects.filter(detalle_presupuesto=self.object.pk).values('servicio', 'detalle_presupuesto', 'detalle_presupuesto__mueble', 'monto_servicio').annotate(tcount=Count('servicio')).order_by('servicio')
        return context


class PresupuestoDireccionList(ListView):
    model = Presupuesto_direccion
    paginate_by = 25
    template_name = 'presupuestodireccion_lista.html'

    def get_queryset(self):
        queryset = super(PresupuestoDireccionList, self).get_queryset()
        return queryset.filter(presupuesto_id=self.kwargs['presupuesto_id'])


class PresupuestoServicioList(ListView):

    template_name = 'presupuestoservicio_lista.html'
    context_object_name = 'servicio'

    def get_queryset(self):
        self.detalle_presupuesto = get_object_or_404(Presupuesto_Detalle, pk=self.args[0])
        return Presupuesto_servicio.objects.filter(detalle_presupuesto=self.detallepresupuesto).values('servicio', 'detalle_presupuesto', 'monto_servicio').annotate(tcount=Count('servicio')).order_by('servicio')


class PresupuestoView(View):
    form_class = PresupuestoForm
    template_name = 'presupuesto_add.html'

    def get(self, request, *args, **kwargs):

        data = {
            'cotizador': self.request.user
        }

        form = self.form_class(initial=data)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            id_reg = form.save()

            # <process form cleaned data>
            return HttpResponseRedirect(reverse('upresupuestos:PresupuestoDetail', args=(id_reg.id,)))

        return render(request, self.template_name, {'form': form})


class PresupuestoDireccionView(View):
    form_class = PresupuestoDireccionForm
    template_name = 'presupuestodireccion_add.html'

    def get(self, request, *args, **kwargs):

        if self.request.is_ajax():
            ocupacion_id = self.request.GET.get('id_ocupacion')
            tipoinmueble_id = self.request.GET.get('id_tipoinmueble')

            if tipoinmueble_id:
                tipoinmueble = Tipo_Inmueble.objects.get(id=tipoinmueble_id)
                if tipoinmueble:
                    tipoinmueble = [{
                        'tipoinmueble': tipoinmueble.tipo_inmueble,
                    }]

                return JsonResponse(tipoinmueble, safe=False)

            if ocupacion_id:
                ocupacion = Ocupacion.objects.get(id=ocupacion_id)
                if ocupacion:
                    ocupacion = [{
                        'ocupacion': ocupacion.descripcion,
                        'valorocupacion': ocupacion.valor
                    }]

                return JsonResponse(ocupacion, safe=False)

        precargado = DatosPrecargado.objects.all()
        if precargado:
            complejidad = precargado[0].complejidadinmueble
            factor_complejidad = precargado[0].factorcomplejidadinmueble
            valor_ambiente_complejidad = precargado[0].valorambcompleinmueble
            valor_metrocubico_complejiadad = precargado[0].valorm3compleinmueble
            ocupacidad_inmueble = precargado[0].ocupacioninmueble
            valor_ocupacidad = precargado[0].valorocupacioninmueble
            lista_ocupacion = 0

        complejidadinmueble = Complejidad_Inmueble.objects.get(complejidad='Media')
        if complejidadinmueble:
            complejidad = complejidadinmueble.complejidad
            factor_complejidad = complejidadinmueble.factor
            valor_ambiente_complejidad = complejidadinmueble.valor_ambiente
            valor_metrocubico_complejiadad = complejidadinmueble.valor_metrocubico

        ocupacion = Ocupacion.objects.get(descripcion='Medio Lleno')
        if ocupacion:
            lista_ocupacion = ocupacion.id
            ocupacidad_inmueble = ocupacion.descripcion
            valor_ocupacidad = ocupacion.valor

        tipoinmueble = Tipo_Inmueble.objects.order_by('tipo_inmueble').first()

        data = {
            'presupuesto': self.request.GET['pre'],
            'tipo_direccion': request.GET['tipo'],
            'complejidad': complejidad,
            'factor_complejidad': factor_complejidad,
            'valor_ambiente_complejidad': valor_ambiente_complejidad,
            'valor_metrocubico_complejiadad': valor_metrocubico_complejiadad,
            'lista_ocupacion': lista_ocupacion,
            'ocupacidad_inmueble': ocupacidad_inmueble,
            'valor_ocupacidad': valor_ocupacidad,
            'tipo_inmueble': tipoinmueble
        }
        form = self.form_class(initial=data)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        tipo_inmueble = Tipo_Inmueble.objects.get(id=request.POST['lista_tipoinmueble'])
        ocupacidad_inmueble = Ocupacion.objects.get(id=request.POST['lista_ocupacion'])

        if form.is_valid():
            formResult = form.save(commit=False)
            formResult.tipo_inmueble = tipo_inmueble.tipo_inmueble
            formResult.ocupacidad_inmueble = ocupacidad_inmueble.descripcion
            formResult.valor_ocupacidad = ocupacidad_inmueble.valor
            formResult.save()

            cantOrig = Presupuesto_direccion.objects.filter(presupuesto=request.POST['presupuesto'], tipo_direccion='Origen').count()
            cantDest = Presupuesto_direccion.objects.filter(presupuesto=request.POST['presupuesto'], tipo_direccion='Destino').count()

            if cantOrig > 0 and cantDest > 0:
                updatepresu = Presupuesto.objects.filter(pk=request.POST['presupuesto'])
                updatepresu.update(estado='Preparado')

            # <process form cleaned data>
            # redirect_to = request.GET['next']

            # if redirect_to:
            #     return HttpResponseRedirect(redirect_to)
            # else:
            #     return HttpResponseRedirect(reverse('upresupuesto:PresupuestoList'))
            mensaje = {'estatus': 'ok', 'msj': 'Registro guardado'}
            return JsonResponse(mensaje, safe=False)

        return render(request, self.template_name, {'form': form})


class PresupuestoDetalleView(View):
    form_class = PresupuestoDetalleForm
    template_name = 'presupuestodetalle_add.html'

    def get(self, request, *args, **kwargs):

        precargado = DatosPrecargado.objects.all()
        if precargado:
            densidadcontenido = precargado[0].densidadcontenidomueble
            vol_contenedor = precargado[0].volcontenedormueble
            peso_contenedor = precargado[0].peso_contenedormueble
            capacidadvolcontenedor = precargado[0].capvolcontenedormueble
            capacidadpesocontenedor = precargado[0].cappesocontenedormueble
            descripcioncontenedor = 'No definido'
            tamano = precargado[0].tamanomueble
            densidad = precargado[0].densidadmueble
            ancho = precargado[0].anchomueble
            largo = precargado[0].largomueble
            alto = precargado[0].altomueble
            peso = precargado[0].pesomueble
            valor_densidad = precargado[0].valordensidadmueble
            volumen_mueble = precargado[0].volumenmueble

        if self.request.is_ajax():
            ambiente_id = self.request.GET.get('id_lista_ambiente')
            mueble_id = self.request.GET.get('id_lista_mueble')
            tamano_id = self.request.GET.get('id_lista_tamano')
            ocupacion_id = self.request.GET.get('id_ocupacion')

            if (mueble_id and tamano_id is None):
                mueble = Mueble.objects.get(id=mueble_id)
                contenido = Contenido_Tipico.objects.filter(mueble=mueble_id, predefinido=True)[:1]

                if contenido:
                    densidadcontenido = contenido[0].contenido.densidad_media
                    contenidoservicio = Contenido_Servicio.objects.filter(contenido=contenido[0].contenido_id, predefinido=True)
                    if contenidoservicio:
                        contenedor = Material.objects.filter(servicio_material__servicio_id=contenidoservicio[0].servicio_id, contenedor=True)[:1]

                        vol_contenedor = contenedor[0].volumen
                        peso_contenedor = contenedor[0].peso
                        capacidadvolcontenedor = contenedor[0].capacidadvolm3
                        capacidadpesocontenedor = contenedor[0].capacidad_peso
                        descripcioncontenedor = contenedor[0].material

                if mueble:
                    mueble = [{
                        'mueble': mueble.mueble,
                        'trasladable': mueble.trasladable,
                        'ocupacion': mueble.ocupacion.id,
                        'descripocupacion': mueble.ocupacion.descripcion,
                        'valorocupacion': mueble.ocupacion.valor,
                        'capacidadmueble': mueble.capacidad,
                        'densidadcontenido': densidadcontenido,
                        'vol_contenedor': round(vol_contenedor, 3),
                        'peso_contenedor': round(peso_contenedor, 3),
                        'capacidadvolcontenedor': capacidadvolcontenedor,
                        'capacidadpesocontenedor': capacidadpesocontenedor,
                        'descripcioncontenedor': descripcioncontenedor
                    }]

                return JsonResponse(mueble, safe=False)

            if ambiente_id:
                ambiente = Ambiente.objects.get(id=ambiente_id)
                if ambiente:
                    ambiente = [{
                        'ambiente': ambiente.ambiente,
                    }]
                return JsonResponse(ambiente, safe=False)

            if tamano_id:
                tamanomueble = Tamano_Mueble.objects.filter(tamano_id=tamano_id, mueble_id=mueble_id)[:1]
                if tamanomueble:
                    tamano = tamanomueble[0].tamano.descripcion
                    densidad = tamanomueble[0].densidad.descripcion
                    ancho = tamanomueble[0].ancho
                    largo = tamanomueble[0].largo
                    alto = tamanomueble[0].alto
                    peso = tamanomueble[0].peso
                    valor_densidad = tamanomueble[0].densidad_valor
                    volumen_mueble = tamanomueble[0].volumenmueble

                tamano = [{
                    'tamano': tamano,
                    'densidad': densidad,
                    'ancho': ancho,
                    'largo': largo,
                    'alto': alto,
                    'peso': peso,
                    'valor_densidad': round(valor_densidad, 2),
                    'volumen_mueble': round(volumen_mueble, 3),
                }]
                return JsonResponse(tamano, safe=False)

            if ocupacion_id:
                ocupacion = Ocupacion.objects.get(id=ocupacion_id)
                if ocupacion:
                    ocupacion = [{
                        'ocupacion': ocupacion.descripcion,
                        'valorocupacion': ocupacion.valor
                    }]

                return JsonResponse(ocupacion, safe=False)

        if self.request.GET.get('amb'):
            lista_ambiente = Ambiente.objects.get(ambiente=self.request.GET.get('amb'))

            data = {
                'presupuesto': self.request.GET.get('pre'),
                'ambiente': self.request.GET.get('amb'),
                'lista_ambiente': lista_ambiente.id
                }
        else:
            data = {
                'presupuesto': self.request.GET.get('pre')
                }

        form = self.form_class(initial=data)

        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()

            #actualizar estatus en presupuesto
            updatepresu = Presupuesto.objects.filter(pk=self.request.POST.get('presupuesto'))
            cant_item = Presupuesto_servicio.objects.filter(detalle_presupuesto__presupuesto=self.request.POST.get('presupuesto')).count()
            if cant_item <= 0:
                updatepresu.update(estado='Muebles cargados')

            # <process form cleaned data>
            # redirect_to = request.GET['next']

            # if redirect_to:
            #     return HttpResponseRedirect(redirect_to)
            # else:
            #     return HttpResponseRedirect(reverse('upresupuesto:PresupuestoList'))
            mensaje = {'estatus': 'ok', 'msj': 'Registro guardado'}
            return JsonResponse(mensaje, safe=False)

        return render(request, self.template_name, {'form': form})


class PresupuestoServicioView(View):
    form_class = PresupuestoServicioForm
    template_name = 'presupuestoservicio_add.html'

    def get(self, request, *args, **kwargs):

        try:
            servicios = Servicio.objects.filter(servicio__in=Presupuesto_servicio.objects.values('servicio').filter(detalle_presupuesto=self.request.GET.get('pre')))

            data = {
                'detalle_presupuesto': self.request.GET.get('pre'),
                'lista_servicio': [p.id for p in servicios]
            }
        except Presupuesto_servicio.DoesNotExist:

            data = {
                'detalle_presupuesto': self.request.GET.get('pre'),
            }

        form = self.form_class(initial=data)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):

        precargado = DatosPrecargado.objects.all()
        if precargado:
            tarifa = precargado[0].tarifacomplejidadservicio
            factor_tiempo = precargado[0].factortiempocompservicio
            materialservicio = precargado[0].materialservicio
            cantidadmaterial = precargado[0].cantidadmaterial
            preciomaterial = precargado[0].preciomaterial
            montomaterial = precargado[0].montomaterial
            volmaterial = precargado[0].volmaterial
            pesomaterial = precargado[0].pesomaterial

        form = self.form_class(request.POST)

        servicios = request.POST.getlist('lista_servicio')

        try:

            try:
                existeservicio = Presupuesto_servicio.objects.filter(detalle_presupuesto=self.request.POST.get('detalle_presupuesto'))
            except Presupuesto_servicio.DoesNotExist:
                existeservicio = None

            if existeservicio:
                Presupuesto_servicio.objects.filter(detalle_presupuesto=self.request.POST.get('detalle_presupuesto')).delete()

            for i in servicios:
                idservicio = i

                servicio = Servicio.objects.get(id=idservicio)

                complejidad = Complejidad_Servicio.objects.filter(servicio=idservicio, complejidad__descripcion='Media')
                if complejidad:
                    tarifa = complejidad[0].tarifa
                    factor_tiempo = complejidad[0].factor_tiempo

                mueble = Presupuesto_Detalle.objects.get(id=self.request.POST.get('detalle_presupuesto'))
                materiales = Servicio_Material.objects.filter(servicio=idservicio)
                if materiales:
                    for material in materiales:

                        cantidadmaterial = CalculoCantMaterial(mueble.ancho, mueble.largo, mueble.alto, material.material.ancho, material.calculo, material.cantidad)
                        if material.calculo == '3':
                            montomaterial = Decimal(round((cantidadmaterial * material.material.precio), 2))
                            volmaterial = Decimal(round((cantidadmaterial * material.material.volumen), 3))
                            pesomaterial = Decimal(round((cantidadmaterial * material.material.peso), 3))
                        else:
                            montomaterial = Decimal(round((cantidadmaterial/(material.material.largo/100)) * material.material.precio, 2))
                            volmaterial = Decimal(round((cantidadmaterial * (material.material.volumen/(material.material.largo/100))), 3))
                            pesomaterial = Decimal(round((cantidadmaterial * (material.material.peso/(material.material.largo/100))), 3))

                        tiempoaplicado = 0
                        if material.material.contenedor is True:
                            tiempoaplicado = Decimal(round(factor_tiempo, 2))
                        else:
                            tiempoaplicado = Decimal(round((factor_tiempo * mueble.volumen_mueble), 2))

                        agregar = Presupuesto_servicio.objects.create(servicio=servicio.servicio,
                                                                      monto_servicio=tarifa,
                                                                      material=material.material.material,
                                                                      cantidad_material=cantidadmaterial,
                                                                      precio_material=material.material.precio,
                                                                      monto_material=montomaterial,
                                                                      volumen_material=volmaterial,
                                                                      peso_material=pesomaterial,
                                                                      detalle_presupuesto_id=self.request.POST.get('detalle_presupuesto'),
                                                                      tiempo_aplicado=tiempoaplicado)
                        agregar.save()
                else:
                    agregar = Presupuesto_servicio.objects.create(servicio=servicio.servicio,
                                                                  monto_servicio=tarifa,
                                                                  material=materialservicio,
                                                                  cantidad_material=cantidadmaterial,
                                                                  precio_material=preciomaterial,
                                                                  monto_material=montomaterial,
                                                                  volumen_material=volmaterial,
                                                                  peso_material=pesomaterial,
                                                                  detalle_presupuesto_id=self.request.POST.get('detalle_presupuesto'),
                                                                  tiempo_aplicado=factor_tiempo)
                    agregar.save()

                updatepresu = Presupuesto.objects.filter(presupuesto_detalle__id=request.POST['detalle_presupuesto'])
                updatepresu.update(estado='Servicios cargados')

                # # <process form cleaned data>
                # redirect_to = request.GET['next']

                # if redirect_to:
                #     return HttpResponseRedirect(redirect_to)
                # else:
                #     return HttpResponseRedirect(reverse('upresupuesto:PresupuestoList'))
                #
            mensaje = {'estatus': 'ok', 'msj': 'Registro guardado'}
            return JsonResponse(mensaje, safe=False)

        except:
            mensaje = {'estatus': 'error', 'msj': 'Ocurrio un error'}
            return JsonResponse(mensaje, safe=False)

        return render(request, self.template_name, {'form': form})


class PresupuestoServicioViewFomset(View):
    form_class_formset = formset_factory(PresupuestoServicioForm, extra=5)
    template_name = 'presupuestoservicio_add.html'

    def get(self, request, *args, **kwargs):

        data = {
            'detalle_presupuesto': self.request.GET.get('pre'),
            }

        formset = self.form_class_formset(initial=[data])
        return render(request, self.template_name, {'formset': formset})

    def post(self, request, *args, **kwargs):
        formset = self.form_class_formset(request.POST)
        if formset.is_valid():
            for form in formset:
                formset.save()
            # <process formset cleaned data>
            return HttpResponseRedirect('/')

        return render(request, self.template_name, {'formset': formset})


class DatosPrecargadoUpdate(UpdateView):
    template_name = 'datosprecargados_edit.html'
    form_class = DatosPrecargadoForm
    model = DatosPrecargado

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()

        redirect_to = self.request.GET['next']
        if redirect_to:
            return HttpResponseRedirect(redirect_to)
        else:
            return render_to_response(self.template_name, self.get_context_data())


class PresupuestoUpdate(UpdateView):
    template_name = 'presupuesto_edit.html'
    form_class = PresupuestoForm
    model = Presupuesto

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()

        mensaje = {'estatus': 'ok', 'msj': 'Registro guardado'}
        return JsonResponse(mensaje, safe=False)


class PresupuestoDireccionUpdate(UpdateView):
    template_name = 'presupuestodireccion_edit.html'
    form_class = PresupuestoDireccionForm
    model = Presupuesto_direccion

    def get_initial(self):
        super(PresupuestoDireccionUpdate, self).get_initial()
        lista_ocupacion = Ocupacion.objects.get(descripcion=self.object.ocupacidad_inmueble)
        lista_tipoinmueble = Tipo_Inmueble.objects.get(tipo_inmueble=self.object.tipo_inmueble)
        self.initial = {"lista_ocupacion": lista_ocupacion.id, 'lista_tipoinmueble': lista_tipoinmueble.id}
        return self.initial

    def form_valid(self, form):
        tipo_inmueble = Tipo_Inmueble.objects.get(id=self.request.POST['lista_tipoinmueble'])
        ocupacidad_inmueble = Ocupacion.objects.get(id=self.request.POST['lista_ocupacion'])

        self.object = form.save(commit=False)
        self.object.tipo_inmueble = tipo_inmueble.tipo_inmueble
        self.object.ocupacidad_inmueble = ocupacidad_inmueble.descripcion
        self.object.valor_ocupacidad = ocupacidad_inmueble.valor

        self.object.save()

        # redirect_to = self.request.GET['next']
        # if redirect_to:
        #     return HttpResponseRedirect(redirect_to)            mensaje = {'estatus': 'ok', 'msj': 'Registro guardado'}
        # else:
         #     return render_to_response(self.template_name, self.get_context_data())
        mensaje = {'estatus': 'ok', 'msj': 'Registro guardado'}
        return JsonResponse(mensaje, safe=False)


class PresupuestoDetalleUpdate(UpdateView):
    template_name = 'presupuestodetalle_edit.html'
    form_class = PresupuestoDetalleForm
    model = Presupuesto_Detalle

    def get_initial(self):
        super(PresupuestoDetalleUpdate, self).get_initial()
        lista_ambiente = Ambiente.objects.get(ambiente=self.object.ambiente)
        lista_mueble = Mueble.objects.get(mueble=self.object.mueble)
        lista_ocupacion = Ocupacion.objects.get(descripcion=self.object.ocupacidad)

        try:
            lista_tamano = Tamano.objects.get(descripcion=self.object.tamano)
        except Tamano.DoesNotExist:
            lista_tamano = Tamano.objects.get(descripcion='Mediano')

        if lista_tamano:
            self.initial = {
                "lista_mueble": lista_mueble.id,
                "lista_ambiente": lista_ambiente.id,
                "lista_tamano": lista_tamano.id,
                "lista_ocupacion": lista_ocupacion.id
            }
        else:
            self.initial = {
                "lista_mueble": lista_mueble.id,
                "lista_ambiente": lista_ambiente.id,
                "lista_ocupacion": lista_ocupacion.id
            }

        return self.initial

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()

        #actualizar valore de canti_ambiente y cant_mueble en presupuesto
        presu = Presupuesto_Detalle.objects.filter(presupuesto=self.request.POST.get('presupuesto'))
        cant_ambiente = presu.values('ambiente').annotate(
            acount=Count('ambiente')).order_by('ambiente')

        cant_mueble = presu.count()
        reporter = Presupuesto.objects.filter(pk=self.request.POST.get('presupuesto'))
        reporter.update(cantidad_ambientes=len(cant_ambiente))
        reporter.update(cantidad_muebles=cant_mueble)

        #redirect_to = self.request.GET['next']
        #if redirect_to:
        #    return HttpResponseRedirect(redirect_to)
        #else:
        #    return render_to_response(self.template_name, self.get_context_data())
        mensaje = {'estatus': 'ok', 'msj': 'Registro guardado'}
        return JsonResponse(mensaje, safe=False)


class PresupuestoServicioUpdate(UpdateView):
    template_name = 'presupuestoservivio_edit.html'
    form_class = PresupuestoServicioForm
    model = Presupuesto_servicio

    def get_initial(self):
        super(PresupuestoServicioUpdate, self).get_initial()
        lista_servicio = Servicio.objects.get(servicio=self.object.servicio)
        lista_material = Material.objects.get(material=self.object.material)
        self.initial = {
            "lista_servicio": lista_servicio.id,
            "lista_material": lista_material.id
            }
        return self.initial

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()

        redirect_to = self.request.GET['next']
        if redirect_to:
            return HttpResponseRedirect(redirect_to)
        else:
            return render_to_response(self.template_name, self.get_context_data())


class PresupuestoDelete(DeleteView):
    model = Presupuesto
    form_class = PresupuestoForm
    template_name = 'server_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        self.obj = self.get_object()
        self.obj.activo = 'Anulado'
        self.obj.save()

        redirect_to = self.request.GET['next']
        if redirect_to:
            return HttpResponseRedirect(redirect_to)
        else:
            return HttpResponseRedirect(reverse('upresupuesto:PresupuestoList'))


class PresupuestoDireccionDelete(DeleteView):
    model = Presupuesto_direccion
    template_name = 'server_confirm_delete.html'
    #success_url = reverse_lazy('upresupuesto:PresupuestoList')

    def delete(self, request, *args, **kwargs):
        self.obj = self.get_object()
        presu = self.obj.presupuesto
        self.obj.delete()

        cantOrig = Presupuesto_direccion.objects.filter(presupuesto=presu, tipo_direccion='Origen').count()
        cantDest = Presupuesto_direccion.objects.filter(presupuesto=presu, tipo_direccion='Destino').count()

        if cantOrig <= 0 or cantDest <= 0:
            updatepresu = Presupuesto.objects.filter(pk=presu.id)
            updatepresu.update(estado='Iniciado')

        mensaje = {'estatus': 'ok', 'msj': 'Registro guardado'}
        return JsonResponse(mensaje, safe=False)

        #redirect_to = self.request.GET['next']
        #if redirect_to:
        #    return HttpResponseRedirect(redirect_to)
        #else:
        #    return HttpResponseRedirect(reverse('upresupuesto:PresupuestoList'))


class PresupuestoDetalleDelete(DeleteView):
    model = Presupuesto_Detalle
    template_name = 'server_confirm_delete.html'
    #success_url = reverse_lazy('upresupuesto:PresupuestoList')

    def delete(self, request, *args, **kwargs):
        self.obj = self.get_object()
        presu = self.obj.presupuesto
        self.obj.delete()

        cant_item = Presupuesto_Detalle.objects.filter(presupuesto=presu).count()
        if cant_item <= 0:
            updatepresu = Presupuesto.objects.filter(pk=presu)
            updatepresu.update(estado='Preparado')

        mensaje = {'estatus': 'ok', 'msj': 'Registro guardado'}
        return JsonResponse(mensaje, safe=False)

        #redirect_to = self.request.GET['next']
        #if redirect_to:
        #    return HttpResponseRedirect(redirect_to)
        #else:
        #    return HttpResponseRedirect(reverse('upresupuesto:PresupuestoList'))


class PresupuestoServicioDelete(DeleteView):
    model = Presupuesto_servicio
    template_name = 'server_confirm_delete.html'
    #success_url = reverse_lazy('upresupuesto:PresupuestoList')

    def delete(self, request, *args, **kwargs):
        self.obj = self.get_object()
        presu = self.obj.detalle_presupuesto.id
        Presupuesto_servicio.objects.filter(servicio=self.obj.servicio, detalle_presupuesto=presu).delete()

        updatepresu = Presupuesto.objects.filter(presupuesto_detalle__id=presu)
        cant_item = Presupuesto_servicio.objects.filter(detalle_presupuesto__presupuesto=updatepresu).count()
        if cant_item <= 0:
            updatepresu.update(estado='Muebles cargados')

        #redirect_to = self.request.GET['next']
        #if redirect_to:
        #    return HttpResponseRedirect(redirect_to)
        #else:
        #    return HttpResponseRedirect(reverse('upresupuesto:PresupuestoList'))
        mensaje = {'estatus': 'ok', 'msj': 'Registro guardado'}
        return JsonResponse(mensaje, safe=False)


class PresupuestoDetailResumen(DetailView):

    model = Presupuesto
    context_object_name = "presupuesto"
    template_name = 'presupuesto_resumen.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(PresupuestoDetailResumen, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        presupuesto = update_presupuesto(self.request, self.object.pk)
        context['presupuesto'] = presupuesto
        context['detalle_list'] = Presupuesto_Detalle.objects.filter(presupuesto=self.object.pk)
        context['ambientes'] = Presupuesto_Detalle.objects.filter(presupuesto=self.object.pk).values('ambiente').annotate(acount=Count('ambiente')).order_by('ambiente')
        context['direccion_origen'] = Presupuesto_direccion.objects.filter(presupuesto=self.object.pk, tipo_direccion="Origen")
        context['direccion_destino'] = Presupuesto_direccion.objects.filter(presupuesto=self.object.pk, tipo_direccion="Destino")
        context['servicio'] = Presupuesto_servicio.objects.filter(detalle_presupuesto__presupuesto=self.object.pk).values('servicio', 'detalle_presupuesto', 'monto_servicio', 'tiempo_aplicado').annotate(tcount=Count('servicio')).order_by('servicio')
        context['empresa'] = Empresa.objects.get(id=1)
        context['now'] = timezone.now()
        context['servicio2'] = Presupuesto_servicio.objects.filter(detalle_presupuesto__presupuesto=self.object.pk).values('servicio', 'material', 'precio_material').annotate(tcount=Count('servicio'), smontomat=Sum('monto_material'), scantmat=Sum('cantidad_material'), svolmat=Sum('volumen_material'), spesomat=Sum('peso_material'), stiempoa=Sum('tiempo_aplicado'), smontoserv=Sum('monto_servicio')).order_by('servicio')
        context['pagesize'] = 'A4'

        #pdf = render_to_pdf('presupuesto_resumen_email.html', context)
       # pdf = hola_pdf(self.request)

        Email('presupuesto_resumen_email.html',
              context, 'Presupuesto Mudarte',
              'Resumen del presupuesto generado',
              '"Mudarte" <yusnelvy@gmail.com>',
              'yusnelvy@hotmail.com')

        return context


def generar_pdf(request):

    response = HttpResponse(content_type='application/pdf')
    pdf_name = "clientes.pdf"  # llamado clientes
    # la linea 26 es por si deseas descargar el pdf a tu computadora
    # response['Content-Disposition'] = 'attachment; filename=%s' % pdf_name
    buff = BytesIO()
    doc = SimpleDocTemplate(buff,
                            pagesize=letter,
                            rightMargin=40,
                            leftMargin=40,
                            topMargin=60,
                            bottomMargin=18,
                            )
    clientes = []
    styles = getSampleStyleSheet()
    header = Paragraph("Listado de Clientes", styles['Heading1'])
    clientes.append(header)
    headings = ('Nombre', 'mdza', 'veh', 'recur')
    allclientes = [(p.nombre_cliente, p.monto_mundanza_revisada, p.monto_vehiculo_revisado, p.monto_recursos_revisado) for p in Presupuesto.objects.all()]

    t = Table([headings] + allclientes)
    t.setStyle(TableStyle(
        [
            ('GRID', (0, 0), (3, -1), 1, colors.dodgerblue),
            ('LINEBELOW', (0, 0), (-1, 0), 2, colors.darkblue),
            ('BACKGROUND', (0, 0), (-1, 0), colors.dodgerblue)
        ]
    ))
    clientes.append(t)
    doc.build(clientes)
    response.write(buff.getvalue())
    buff.close()
    return response


class PresupuestoRevisarUpdateView(UpdateView):
    form_class = PresupuestoRevisarForm
    model = Presupuesto
    template_name = 'presupuesto_revisar.html'

    def get_context_data(self, **kwargs):
        # Obtenemos el contexto de la clase base
        context = super().get_context_data(**kwargs)
        # añadimos nuevas variables de contexto al diccionario
        context['direccion_origen'] = Presupuesto_direccion.objects.filter(presupuesto=self.object.pk, tipo_direccion="Origen")
        context['empresa'] = Empresa.objects.get(id=1)
        context['now'] = timezone.now()
        # devolvemos el contexto
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()

        estado = Presupuesto.objects.filter(pk=self.object.id)
        estado.update(estado='Terminado cotizador')

        redirect_to = self.request.REQUEST.get('next', '')
        if redirect_to:
            return HttpResponseRedirect(redirect_to)
        else:
            return render_to_response(self.template_name, self.get_context_data())


def ajax_tamano_request(request):
    # Expect an auto 'type' to be passed in via Ajax and POST
    if request.is_ajax() and request.method == 'POST':
        mueble = Mueble.objects.filter(id=request.POST.get('mueble', ''))
        tamanos = mueble.Tamano_Mueble.all()
        # get all the colors for this type of auto.
        mensaje = {'tamanos': tamanos}
        return JsonResponse(mensaje, safe=False)


def CalculoCantMaterial(muebleancho, mueblelargo, mueblealto, materialancho, calculo, cantidadmat):

    cantidadmaterial = 0
    nrovuelta = 4
    solape = Decimal(0.20)

    muebleancho = muebleancho/100  # en mts
    mueblelargo = mueblelargo/100
    mueblealto = mueblealto/100
    materialancho = materialancho/100

    if (calculo == '1'):  # materiales inelastico
        cantidad = Decimal((muebleancho * mueblelargo)+(muebleancho * mueblealto)+(mueblelargo * mueblealto))
        cantidad = cantidad * 2
        cantidad = cantidad * (1 + solape)
        cantidad = cantidad / materialancho
        #Parte entera con o sin signo
        entero = int(cantidad)
        #Parte decimal
        residuo = abs(cantidad) - abs(int(cantidad))
        redondear = Decimal(0.5)

        if (residuo == 0):
            residuof = 0
        else:
            if (residuo/redondear) > 1:
                cant1 = Decimal(round((residuo / redondear), 2))
                cant2 = cant1 % 1
                if cant2 > 0:
                    resto = 1
                else:
                    resto = 0
                cant3 = int(residuo/redondear)
                residuof = (cant3 + resto) * redondear
            else:
                residuof = redondear
        cantidadmaterial = entero + residuof

    elif (calculo == '2'):
        cantidad1 = ((mueblealto*(1 + solape)) / materialancho)
        redondear = 1
        entero = int(cantidad1)
        residuo = abs(cantidad1) - abs(int(cantidad1))

        if (residuo == 0):
            residuof = 0
        else:
            if((residuo/redondear) > 1):
                if((round((residuo/redondear), 2) % 1) > 0):
                    resto = 1
                else:
                    resto = 0
                residuof = (int((residuo/redondear)) + resto) * redondear
            else:
                residuof = redondear

        cantidad = nrovuelta*2*(muebleancho+mueblelargo)*(entero+residuof)
        entero = int(cantidad)
        residuo = abs(cantidad) - abs(int(cantidad))

        if (residuo == 0):
            residuof = 0
        else:
            if((residuo/redondear) > 1):
                if((round((residuo/redondear), 2) % 1) > 0):
                    resto = 1
                else:
                    resto = 0
                residuof = (int((residuo/redondear)) + resto) * redondear
            else:
                residuof = redondear

        cantidadmaterial = entero + residuof

    elif (calculo == '3'):

        volumenmueble = Decimal(round((muebleancho*mueblealto*mueblelargo), 2))
        cantidad = volumenmueble * cantidadmat

        #Parte entera con o sin signo
        entero = int(cantidad)
        #Parte decimal
        residuo = abs(cantidad) - abs(int(cantidad))
        redondear = 1

        if (residuo == 0):
            residuof = 0
        else:
            if (residuo/redondear) > 1:
                cant1 = Decimal(round((residuo / redondear), 2))
                cant2 = cant1 % 1
                if cant2 > 0:
                    resto = 1
                else:
                    resto = 0
                cant3 = int(residuo/redondear)
                residuof = (cant3 + resto) * redondear
            else:
                residuof = redondear
        cantidadmaterial = entero + residuof

    return(Decimal(round(cantidadmaterial, 2)))


def update_presupuesto(request, pk):

    #actualizar valores de canti_ambiente y cant_mueble en presupuesto
    precargado = DatosPrecargado.objects.all()
    if precargado:
        rendimiento_peso = precargado[0].rendimiento_peso
        rendimiento_volumen = precargado[0].rendimiento_volumen
        rendimiento_unidad = precargado[0].rendimiento_unidad
        duracion_optimamudanza = precargado[0].duracion_optimamudanza

    direccion = Presupuesto_direccion.objects.filter(presupuesto=pk, tipo_direccion='Origen')
    if direccion:
        tarifa_m3 = direccion[0].valor_metrocubico_complejiadad
        tarifa_amb = direccion[0].valor_ambiente_complejidad

    presu = Presupuesto_Detalle.objects.filter(presupuesto=pk)
    materiales = Presupuesto_servicio.objects.filter(detalle_presupuesto__presupuesto_id=pk)
    if materiales:
        peso_materiales = materiales.aggregate(pes_material=Sum('peso_material'))
        volumen_materiales = materiales.aggregate(vol_material=Sum('volumen_material'))
        monto_materiales = materiales.aggregate(mont_material=Sum('monto_material'))

        peso_materiales = peso_materiales['pes_material']
        volumen_materiales = volumen_materiales['vol_material']
        monto_materiales = monto_materiales['mont_material']
    else:
        peso_materiales = 0
        volumen_materiales = 0
        monto_materiales = 0

    materialserv = materiales.values('servicio', 'detalle_presupuesto', 'monto_servicio').annotate(tcount=Count('servicio')).order_by('servicio')
    if materialserv:
        monto_servicio = materialserv.aggregate(monto_serv=Sum('monto_servicio'))
        tiempo_servicio = materialserv.aggregate(tiempo_serv=Sum('tiempo_aplicado'))

        monto_servicio = monto_servicio['monto_serv']
        tiempo_servicio = tiempo_servicio['tiempo_serv']

    else:
        monto_servicio = 0
        tiempo_servicio = 0

    cant_ambiente = Presupuesto_Detalle.objects.filter(presupuesto=pk).values('ambiente').annotate(acount=Count('ambiente')).order_by('ambiente')
    detallemueble = Presupuesto_Detalle.objects.filter(presupuesto=pk, trasladable=True)
    if detallemueble:
        cant_mueble = detallemueble.count()
        volumen_muebles = detallemueble.aggregate(vol_mueble=Sum('volumen_mueble'))
        peso_muebles = detallemueble.aggregate(pes_mueble=Sum('peso'))

        volumen_muebles = volumen_muebles['vol_mueble']
        peso_muebles = peso_muebles['pes_mueble']

    else:
        cant_mueble = 0
        volumen_muebles = 0
        peso_muebles = 0

    cant_contenedor = presu.aggregate(cant_contenedor=Sum('cantidad_contenedor'))
    peso_contenedores = presu.aggregate(pes_contenedor=Sum('peso_contenedor'))

    peso_contenidos = presu.aggregate(pes_contenido=Sum('peso_contenido'))

    volumen_contenedores = presu.aggregate(vol_contenedor=Sum('volumen_contenedor'))
    volumen_contenidos = presu.aggregate(vol_contenido=Sum('volumen_contenido'))

    updatepresu = Presupuesto.objects.filter(pk=pk)
    updatepresu.update(cantidad_ambientes=len(cant_ambiente))
    updatepresu.update(cantidad_muebles=cant_mueble)
    updatepresu.update(cantidad_contenedores=cant_contenedor['cant_contenedor'])
    updatepresu.update(total_peso_contenedores=round(peso_contenedores['pes_contenedor'], 3))
    updatepresu.update(total_peso_muebles=round(peso_muebles, 3))
    updatepresu.update(total_peso_contenidos=round(peso_contenidos['pes_contenido'], 3))
    updatepresu.update(total_volumen_muebles=round(volumen_muebles, 3))
    updatepresu.update(total_volumen_contenedores=round(volumen_contenedores['vol_contenedor'], 3))
    updatepresu.update(total_volumen_contenidos=round(volumen_contenidos['vol_contenido'], 3))
    updatepresu.update(total_peso_materiales=round(peso_materiales, 3))
    updatepresu.update(total_volumen_materiales=round(volumen_materiales, 3))
    updatepresu.update(monto_materiales=round(monto_materiales, 2))
    updatepresu.update(monto_servicios=round(monto_servicio, 2))
    updatepresu.update(tiempo_servicios=round(tiempo_servicio, 2))

    presupuesto = Presupuesto.objects.get(pk=pk)

    totalm3mudanza = (
        presupuesto.total_volumen_muebles
        + presupuesto.total_volumen_contenedores
        + presupuesto.total_volumen_materiales
        )

    totalpesomudanza = (
        presupuesto.total_peso_muebles
        + presupuesto.total_peso_contenidos
        + presupuesto.total_peso_contenedores
        + presupuesto.total_peso_materiales
        )

    objmudanza = presupuesto.cantidadobjmudanza
    tiemposervicio = presupuesto.tiempo_servicios
    cant_amb = presupuesto.cantidad_ambientes
    montoservicio = presupuesto.monto_servicios
    montomaterial = presupuesto.monto_materiales
    recorridokm = presupuesto.recorrido_km
    tiemporecorrido = presupuesto.tiempo_recorrido

    cant_vehiculokg = 0
    descripcion_vehkg = ""
    montoveh_hrskg = 0
    montoveh_kmkg = 0
    cap_vehiculovolkg = 0
    cap_vehiculovolkg2 = 0
    cant_ayudantekg = 0
    descripcion_perskg = ""
    montopers_kg = 0
    montochoferkg = 0

    cant_vehiculovol = 0
    descripcion_vehvol = ""
    montoveh_hrsvol = 0
    montoveh_kmvol = 0
    cap_vehiculovol2 = 0
    cap_vehiculovol22 = 0
    cant_ayudantevol = 0
    descripcion_persvol = ""
    montopers_vol = 0
    montochofervol = 0

    cant_vehiculo = 0
    descripcion_veh = ""
    montoveh_hrs = 0
    montoveh_km = 0
    cap_vehiculo = 0
    cap_vehiculo2 = 0
    cant_ayudante = 0
    descripcion_pers = ""
    montopers = 0
    montochofer = 0
    montopersadic = 0
    montopersoptima = 0
    montopersteorica = 0

    vehiculos = Vehiculo.objects.all()
    ayudante = Cargo_trabajador.objects.get(cargo='Ayudante de mudanza')

    # for para obtener el arreglo por capacidad m3
    array_capacidadm3 = []
    array_capacidadpeso = []

    j = -1
    vrestopeso = totalpesomudanza
    vrestom3 = totalm3mudanza

    for i in range(len(vehiculos)):
        sw = 0

        entero = int(vrestopeso / vehiculos[i].capacidad_peso)
        vrestopeso = vrestopeso - entero * vehiculos[i].capacidad_peso
        if entero > 0:
            j += 1
            sw = 1
            array_capacidadpeso.append([j]*10)
            array_capacidadpeso[j][0] = entero
            array_capacidadpeso[j][1] = Decimal(round((vehiculos[i].capacidad_peso * array_capacidadpeso[j][0]), 3))
            array_capacidadpeso[j][2] = Decimal(round((vehiculos[i].tarifa_hora * array_capacidadpeso[j][0] * tiemporecorrido), 2))
            array_capacidadpeso[j][3] = Decimal(round((vehiculos[i].tarifa_recorrido * array_capacidadpeso[j][0] * recorridokm), 2))
            array_capacidadpeso[j][4] = 'Modelo: ' + vehiculos[i].modelo + \
                                        ' - Tarifa $/h: ' + str(vehiculos[i].tarifa_hora) + \
                                        ' - Tarifa $/Km: ' + str(vehiculos[i].tarifa_recorrido) + \
                                        ' - Capacidad m3: ' + str(vehiculos[i].capacidad_volumen) + \
                                        ' - Capacidad Kgs: ' + str(vehiculos[i].capacidad_peso) + \
                                        ' - Cantidad: ' + str(array_capacidadpeso[j][0]) + \
                                        ' - Volumen Total: ' + str(array_capacidadpeso[j][1]) + \
                                        ' - Total Tarifa $/h: ' + str(array_capacidadpeso[j][2]) + \
                                        ' - Total Tarifa $/Km: ' + str(array_capacidadpeso[j][3])
            array_capacidadpeso[j][9] = Decimal(round((vehiculos[i].capacidad_volumen * array_capacidadpeso[j][0]), 3))
            array_capacidadpeso[j][5] = vehiculos[i].cantidad_ayudante * array_capacidadpeso[j][0]
            array_capacidadpeso[j][6] = Decimal(round((array_capacidadpeso[j][5] * ayudante.tarifa_dia), 2))
            cargo = Cargo_trabajador.objects.get(pk=vehiculos[i].cargo.id)

            array_capacidadpeso[j][7] = Decimal(round((cargo.tarifa_dia * array_capacidadpeso[j][0]), 2))
            array_capacidadpeso[j][8] = 'Conductor asignado: ' + cargo.cargo + ' al modelo: ' + vehiculos[i].modelo + \
                                        ' - Tarifa $/día: ' + str(cargo.tarifa_dia) + \
                                        ' - Cantidad de conductor: ' + str(array_capacidadpeso[j][0]) + \
                                        ' - Total Tarifa $/día: ' + str(array_capacidadpeso[j][7]) + \
                                        ' - Cantidad de ayudantes: ' + str(array_capacidadpeso[j][5]) + \
                                        ' - Tarifa $/día: ' + str(ayudante.tarifa_dia) + \
                                        ' - Total Tarifa $/día: ' + str(array_capacidadpeso[j][6])

        if vrestopeso > 0:
            if i == len(vehiculos)-1:
                j += 1
                array_capacidadpeso.append([j]*10)
                array_capacidadpeso[j][0] = 1
                array_capacidadpeso[j][1] = Decimal(round((vehiculos[i].capacidad_peso * array_capacidadpeso[j][0]), 3))
                array_capacidadpeso[j][2] = Decimal(round((vehiculos[i].tarifa_hora * array_capacidadpeso[j][0] * tiemporecorrido), 2))
                array_capacidadpeso[j][3] = Decimal(round((vehiculos[i].tarifa_recorrido * array_capacidadpeso[j][0] * recorridokm), 2))
                array_capacidadpeso[j][4] = 'Modelo: ' + vehiculos[i].modelo + \
                                            ' - Tarifa $/h: ' + str(vehiculos[i].tarifa_hora) + \
                                            ' - Tarifa $/Km: ' + str(vehiculos[i].tarifa_recorrido) + \
                                            ' - Capacidad m3: ' + str(vehiculos[i].capacidad_volumen) + \
                                            ' - Capacidad Kgs: ' + str(vehiculos[i].capacidad_peso) + \
                                            ' - Cantidad: ' + str(array_capacidadpeso[j][0]) + \
                                            ' - Volumen Total: ' + str(array_capacidadpeso[j][1]) + \
                                            ' - Total Tarifa $/h: ' + str(array_capacidadpeso[j][2]) + \
                                            ' - Total Tarifa $/Km: ' + str(array_capacidadpeso[j][3])
                array_capacidadpeso[j][9] = Decimal(round((vehiculos[i].capacidad_volumen * array_capacidadpeso[j][0]), 3))
                array_capacidadpeso[j][5] = vehiculos[i].cantidad_ayudante * array_capacidadpeso[j][0]
                array_capacidadpeso[j][6] = Decimal(round((array_capacidadpeso[j][5] * ayudante.tarifa_dia), 2))
                cargo = Cargo_trabajador.objects.get(pk=vehiculos[i].cargo.id)

                array_capacidadpeso[j][7] = Decimal(round((cargo.tarifa_dia * array_capacidadpeso[j][0]), 2))
                array_capacidadpeso[j][8] = 'Conductor asignado: ' + cargo.cargo + ' al modelo: ' + vehiculos[i].modelo + \
                                            ' - Tarifa $/día: ' + str(cargo.tarifa_dia) + \
                                            ' - Cantidad de conductor: ' + str(array_capacidadpeso[j][0]) + \
                                            ' - Total Tarifa $/hrs: ' + str(array_capacidadpeso[j][7]) + \
                                            ' - Cantidad de ayudantes: ' + str(array_capacidadpeso[j][5]) + \
                                            ' - Tarifa $/día: ' + str(ayudante.tarifa_dia) + \
                                            ' - Total Tarifa $/hrs: ' + str(array_capacidadpeso[j][6])

                vrestopeso = vrestopeso - array_capacidadpeso[j][1]

            elif (vrestopeso > vehiculos[i+1].capacidad_peso):
                if sw == 0:
                    j += 1
                    sw = 1
                    array_capacidadpeso.append([j]*10)

                array_capacidadpeso[j][0] = array_capacidadpeso[j][0] + 1
                array_capacidadpeso[j][1] = Decimal(round((vehiculos[i].capacidad_peso * array_capacidadpeso[j][0]), 3))
                array_capacidadpeso[j][2] = Decimal(round((vehiculos[i].tarifa_hora * array_capacidadpeso[j][0] * tiemporecorrido), 2))
                array_capacidadpeso[j][3] = Decimal(round((vehiculos[i].tarifa_recorrido * array_capacidadpeso[j][0] * recorridokm), 2))
                array_capacidadpeso[j][4] = 'Modelo: ' + vehiculos[i].modelo + \
                                            ' - Tarifa $/h: ' + str(vehiculos[i].tarifa_hora) + \
                                            ' - Tarifa $/Km: ' + str(vehiculos[i].tarifa_recorrido) + \
                                            ' - Capacidad m3: ' + str(vehiculos[i].capacidad_volumen) + \
                                            ' - Capacidad Kgs: ' + str(vehiculos[i].capacidad_peso) + \
                                            ' - Cantidad: ' + str(array_capacidadpeso[j][0]) + \
                                            ' - Volumen Total: ' + str(array_capacidadpeso[j][1]) + \
                                            ' - Total Tarifa $/h: ' + str(array_capacidadpeso[j][2]) + \
                                            ' - Total Tarifa $/Km: ' + str(array_capacidadpeso[j][3])
                array_capacidadpeso[j][9] = Decimal(round((vehiculos[i].capacidad_volumen * array_capacidadpeso[j][0]), 3))
                array_capacidadpeso[j][5] = vehiculos[i].cantidad_ayudante * array_capacidadpeso[j][0]
                array_capacidadpeso[j][6] = Decimal(round((array_capacidadpeso[j][5] * ayudante.tarifa_dia), 2))
                cargo = Cargo_trabajador.objects.get(pk=vehiculos[i].cargo.id)

                array_capacidadpeso[j][7] = Decimal(round((cargo.tarifa_dia * array_capacidadpeso[j][0]), 2))
                array_capacidadpeso[j][8] = 'Conductor asignado: ' + cargo.cargo + ' al modelo: ' + vehiculos[i].modelo + \
                                            ' - Tarifa $/día: ' + str(cargo.tarifa_dia) + \
                                            ' - Cantidad de conductor: ' + str(array_capacidadpeso[j][0]) + \
                                            ' - Total Tarifa $/hrs: ' + str(array_capacidadpeso[j][7]) + \
                                            ' - Cantidad de ayudantes: ' + str(array_capacidadpeso[j][5]) + \
                                            ' - Tarifa $/día: ' + str(ayudante.tarifa_dia) + \
                                            ' - Total Tarifa $/hrs: ' + str(array_capacidadpeso[j][6])

                vrestopeso = vrestopeso - array_capacidadpeso[j][1]
        if vrestopeso <= 0:
            break

    for i in range(len(array_capacidadpeso)):

        cant_vehiculokg = cant_vehiculokg + array_capacidadpeso[i][0]
        cap_vehiculovolkg = cap_vehiculovolkg + array_capacidadpeso[i][1]
        montoveh_hrskg = montoveh_hrskg + array_capacidadpeso[i][2]
        montoveh_kmkg = montoveh_kmkg + array_capacidadpeso[i][3]
        cant_ayudantekg = cant_ayudantekg + array_capacidadpeso[i][5]
        montopers_kg = montopers_kg + array_capacidadpeso[i][6]
        montochoferkg = montochoferkg + array_capacidadpeso[i][7]
        cap_vehiculovolkg2 = cap_vehiculovolkg2 + array_capacidadpeso[i][9]

        if descripcion_vehkg == '':
            descripcion_vehkg = array_capacidadpeso[i][4]
        else:
            descripcion_vehkg = descripcion_vehkg + ', ' + array_capacidadpeso[i][4]

        if descripcion_perskg == '':
            descripcion_perskg = array_capacidadpeso[i][8]
        else:
            descripcion_perskg = descripcion_perskg + ', ' + array_capacidadpeso[i][8]

    # for para obtener el arreglo por capacidad m3
    j = -1
    for i in range(len(vehiculos)):
        sw = 0

        entero = int(vrestom3 / vehiculos[i].capacidad_volumen)
        vrestom3 = vrestom3 - entero * vehiculos[i].capacidad_volumen
        if entero > 0:
            j += 1
            sw = 1
            array_capacidadm3.append([j]*10)
            array_capacidadm3[j][0] = entero
            array_capacidadm3[j][1] = Decimal(round((vehiculos[i].capacidad_volumen * array_capacidadm3[j][0]), 3))
            array_capacidadm3[j][2] = Decimal(round((vehiculos[i].tarifa_hora * array_capacidadm3[j][0] * tiemporecorrido), 2))
            array_capacidadm3[j][3] = Decimal(round((vehiculos[i].tarifa_recorrido * array_capacidadm3[j][0] * recorridokm), 2))
            array_capacidadm3[j][4] = 'Modelo: ' + vehiculos[i].modelo + \
                                      ' - Tarifa $/h: ' + str(vehiculos[i].tarifa_hora) + \
                                      ' - Tarifa $/Km: ' + str(vehiculos[i].tarifa_recorrido) + \
                                      ' - Capacidad m3: ' + str(vehiculos[i].capacidad_volumen) + \
                                      ' - Capacidad Kgs: ' + str(vehiculos[i].capacidad_peso) + \
                                      ' - Cantidad: ' + str(array_capacidadm3[j][0]) + \
                                      ' - Volumen Total: ' + str(array_capacidadm3[j][1]) + \
                                      ' - Total Tarifa $/h: ' + str(array_capacidadm3[j][2]) + \
                                      ' - Total Tarifa $/Km: ' + str(array_capacidadm3[j][3])
            array_capacidadm3[j][9] = Decimal(round((vehiculos[i].capacidad_peso * array_capacidadm3[j][0]), 3))
            array_capacidadm3[j][5] = vehiculos[i].cantidad_ayudante * array_capacidadm3[j][0]
            array_capacidadm3[j][6] = Decimal(round((array_capacidadm3[j][5] * ayudante.tarifa_dia), 2))
            cargo = Cargo_trabajador.objects.get(pk=vehiculos[i].cargo.id)

            array_capacidadm3[j][7] = Decimal(round((cargo.tarifa_dia * array_capacidadm3[j][0]), 2))
            array_capacidadm3[j][8] = 'Conductor asignado: ' + cargo.cargo + ' al modelo: ' + vehiculos[i].modelo + \
                                      ' - Tarifa $/día: ' + str(cargo.tarifa_dia) + \
                                      ' - Cantidad de conductor: ' + str(array_capacidadm3[j][0]) + \
                                      ' - Total Tarifa $/hrs: ' + str(array_capacidadm3[j][7]) + \
                                      ' - Cantidad de ayudantes: ' + str(array_capacidadm3[j][5]) + \
                                      ' - Tarifa $/día: ' + str(ayudante.tarifa_dia) + \
                                      ' - Total Tarifa $/hrs: ' + str(array_capacidadm3[j][6])
        if vrestom3 > 0:
            if i == len(vehiculos)-1:
                j += 1
                array_capacidadm3.append([j]*10)
                array_capacidadm3[j][0] = 1
                array_capacidadm3[j][1] = Decimal(round((vehiculos[i].capacidad_volumen * array_capacidadm3[j][0]), 3))
                array_capacidadm3[j][2] = Decimal(round((vehiculos[i].tarifa_hora * array_capacidadm3[j][0] * tiemporecorrido), 2))
                array_capacidadm3[j][3] = Decimal(round((vehiculos[i].tarifa_recorrido * array_capacidadm3[j][0] * recorridokm), 2))
                array_capacidadm3[j][4] = 'Modelo: ' + vehiculos[i].modelo + \
                                          ' - Tarifa $/h: ' + str(vehiculos[i].tarifa_hora) + \
                                          ' - Tarifa $/Km: ' + str(vehiculos[i].tarifa_recorrido) + \
                                          ' - Capacidad m3: ' + str(vehiculos[i].capacidad_volumen) + \
                                          ' - Capacidad Kgs: ' + str(vehiculos[i].capacidad_peso) + \
                                          ' - Cantidad: ' + str(array_capacidadm3[j][0]) + \
                                          ' - Volumen Total: ' + str(array_capacidadm3[j][1]) + \
                                          ' - Total Tarifa $/h: ' + str(array_capacidadm3[j][2]) + \
                                          ' - Total Tarifa $/Km: ' + str(array_capacidadm3[j][3])
                array_capacidadm3[j][9] = Decimal(round((vehiculos[i].capacidad_peso * array_capacidadm3[j][0]), 3))
                array_capacidadm3[j][5] = vehiculos[i].cantidad_ayudante * array_capacidadm3[j][0]
                array_capacidadm3[j][6] = Decimal(round((array_capacidadm3[j][5] * ayudante.tarifa_dia), 2))
                cargo = Cargo_trabajador.objects.get(pk=vehiculos[i].cargo.id)

                array_capacidadm3[j][7] = Decimal(round((cargo.tarifa_dia * array_capacidadm3[j][0]), 2))
                array_capacidadm3[j][8] = 'Conductor asignado: ' + cargo.cargo + ' al modelo: ' + vehiculos[i].modelo + \
                                          ' - Tarifa $/día: ' + str(cargo.tarifa_dia) + \
                                          ' - Cantidad de conductor: ' + str(array_capacidadm3[j][0]) + \
                                          ' - Total Tarifa $/hrs: ' + str(array_capacidadm3[j][7]) + \
                                          ' - Cantidad de ayudantes: ' + str(array_capacidadm3[j][5]) + \
                                          ' - Tarifa $/día: ' + str(ayudante.tarifa_dia) + \
                                          ' - Total Tarifa $/hrs: ' + str(array_capacidadm3[j][6])
                vrestom3 = vrestom3 - array_capacidadm3[j][1]

            elif (vrestom3 > vehiculos[i+1].capacidad_volumen):
                if sw == 0:
                    j += 1
                    sw = 1
                    array_capacidadm3.append([j]*10)
                array_capacidadm3[j][0] = array_capacidadm3[j][0] + 1
                array_capacidadm3[j][1] = Decimal(round((vehiculos[i].capacidad_volumen * array_capacidadm3[j][0]), 3))
                array_capacidadm3[j][2] = Decimal(round((vehiculos[i].tarifa_hora * array_capacidadm3[j][0] * tiemporecorrido), 2))
                array_capacidadm3[j][3] = Decimal(round((vehiculos[i].tarifa_recorrido * array_capacidadm3[j][0] * recorridokm), 2))
                array_capacidadm3[j][4] = 'Modelo: ' + vehiculos[i].modelo + \
                                          ' - Tarifa $/h: ' + str(vehiculos[i].tarifa_hora) + \
                                          ' - Tarifa $/Km: ' + str(vehiculos[i].tarifa_recorrido) + \
                                          ' - Capacidad m3: ' + str(vehiculos[i].capacidad_volumen) + \
                                          ' - Capacidad Kgs: ' + str(vehiculos[i].capacidad_peso) + \
                                          ' - Cantidad: ' + str(array_capacidadm3[j][0]) + \
                                          ' - Volumen Total: ' + str(array_capacidadm3[j][1]) + \
                                          ' - Total Tarifa $/h: ' + str(array_capacidadm3[j][2]) + \
                                          ' - Total Tarifa $/Km: ' + str(array_capacidadm3[j][3])
                array_capacidadm3[j][9] = Decimal(round((vehiculos[i].capacidad_peso * array_capacidadm3[j][0]), 3))
                array_capacidadm3[j][5] = vehiculos[i].cantidad_ayudante * array_capacidadm3[j][0]
                array_capacidadm3[j][6] = Decimal(round((array_capacidadm3[j][5] * ayudante.tarifa_dia), 2))
                cargo = Cargo_trabajador.objects.get(pk=vehiculos[i].cargo.id)

                array_capacidadm3[j][7] = Decimal(round((cargo.tarifa_dia * array_capacidadm3[j][0]), 2))
                array_capacidadm3[j][8] = 'Conductor asignado: ' + cargo.cargo + ' al modelo: ' + vehiculos[i].modelo + \
                                          ' - Tarifa $/día: ' + str(cargo.tarifa_dia) + \
                                          ' - Cantidad de conductor: ' + str(array_capacidadm3[j][0]) + \
                                          ' - Total Tarifa $/hrs: ' + str(array_capacidadm3[j][7]) + \
                                          ' - Cantidad de ayudantes: ' + str(array_capacidadm3[j][5]) + \
                                          ' - Tarifa $/día: ' + str(ayudante.tarifa_dia) + \
                                          ' - Total Tarifa $/hrs: ' + str(array_capacidadm3[j][6])

                vrestom3 = vrestom3 - array_capacidadm3[j][1]
        if vrestom3 <= 0:
            break

    for i in range(len(array_capacidadm3)):

        cant_vehiculovol = cant_vehiculovol + array_capacidadm3[i][0]
        cap_vehiculovol2 = cap_vehiculovol2 + array_capacidadm3[i][1]
        montoveh_hrsvol = montoveh_hrsvol + array_capacidadm3[i][2]
        montoveh_kmvol = montoveh_kmvol + array_capacidadm3[i][3]
        cant_ayudantevol = cant_ayudantevol + array_capacidadm3[i][5]
        montopers_vol = montopers_vol + array_capacidadm3[i][6]
        montochofervol = montochofervol + array_capacidadm3[i][7]
        cap_vehiculovol22 = cap_vehiculovol22 + array_capacidadm3[i][9]

        if descripcion_vehvol == '':
            descripcion_vehvol = array_capacidadm3[i][4]
        else:
            descripcion_vehvol = descripcion_vehvol + ', ' + array_capacidadm3[i][4]

        if descripcion_persvol == '':
            descripcion_persvol = array_capacidadm3[i][8]
        else:
            descripcion_persvol = descripcion_persvol + ', ' + array_capacidadm3[i][8]

    if cant_vehiculokg > cant_vehiculovol:
        cant_vehiculo = cant_vehiculokg
        descripcion_veh = descripcion_vehkg
        montoveh_hrs = Decimal(round(montoveh_hrskg, 2))
        montoveh_km = Decimal(round(montoveh_kmkg, 2))
        cap_vehiculo = Decimal(round(cap_vehiculovolkg, 3))
        cap_vehiculo2 = Decimal(round(cap_vehiculovolkg2, 3))
        cant_ayudante = cant_ayudantekg
        descripcion_pers = descripcion_perskg
        montopers = Decimal(round(montopers_kg, 2))
        montochofer = Decimal(round(montochoferkg, 2))

    else:
        cant_vehiculo = cant_vehiculovol
        descripcion_veh = descripcion_vehvol
        montoveh_hrs = Decimal(round(montoveh_hrsvol, 2))
        montoveh_km = Decimal(round(montoveh_kmvol, 2))
        cap_vehiculo = Decimal(round(cap_vehiculovol22, 3))
        cap_vehiculo2 = Decimal(round(cap_vehiculovol2, 3))
        cant_ayudante = cant_ayudantevol
        descripcion_pers = descripcion_persvol
        montopers = Decimal(round(montopers_vol, 2))
        montochofer = Decimal(round(montochofervol, 2))

    demandapeso = Decimal(totalpesomudanza/rendimiento_peso)*2 + tiemposervicio
    demandavolumen = Decimal(totalm3mudanza/rendimiento_volumen)*2 + tiemposervicio
    demandaunidad = Decimal(objmudanza/rendimiento_unidad)*2 + tiemposervicio

    demanda = max(demandapeso, demandavolumen, demandaunidad)

    duracionteorica = Decimal(round((demanda/cant_ayudante), 2))

    if duracionteorica <= duracion_optimamudanza:
        cant_ayudanteadic = 0
        tiempocarga = duracionteorica
    elif duracionteorica > duracion_optimamudanza:
        tiempocarga = duracionteorica - duracion_optimamudanza
        cantidad = (tiempocarga/duracion_optimamudanza) * cant_ayudante

        #Parte entera con o sin signo
        entero = int(cantidad)
        #Parte decimal
        residuo = abs(cantidad) - abs(int(cantidad))
        redondear = 1

        if (residuo == 0):
            residuof = 0
        else:
            if (residuo/redondear) > 1:
                cant1 = round((residuo / redondear), 2)
                cant2 = cant1 % 1
                if cant2 > 0:
                    resto = 1
                else:
                    resto = 0
                cant3 = int(residuo/redondear)
                residuof = (cant3 + resto) * redondear
            else:
                residuof = redondear
        cant_ayudanteadic = entero + residuof
        montopersadic = cant_ayudanteadic*ayudante.tarifa_dia

        descripcion_pers = descripcion_pers + \
                           ' - Cantidad de ayudantes adicionales: ' + str(cant_ayudanteadic) + \
                           ' - Tarifa $/día: ' + str(ayudante.tarifa_dia) + \
                           ' - Total Tarifa $/hrs: ' + str(round(montopersadic, 2))

    montopersteorica = (montopers+montochofer) * duracionteorica

    if montopersadic == 0:
        montopersoptima = montopersteorica
    else:
        montopersoptima = (montopers+montochofer+montopersadic) * duracion_optimamudanza

    recursom3teorico = (totalm3mudanza*tarifa_m3)
    recursoambteorico = (cant_amb*tarifa_amb)

    recursom3optimo = (totalm3mudanza*tarifa_m3)
    recursoamboptimo = (cant_amb*tarifa_amb)

    recuersoteoricomax = max(recursom3teorico, recursoambteorico, montopersteorica)
    recuersooptimomax = max(recursom3optimo, recursoamboptimo, montopersoptima)
    vehiculomonto = montoveh_hrs + montoveh_km

    montoteoricomudanza = recuersoteoricomax + montoservicio + montomaterial + vehiculomonto
    montooptimomudanza = recuersooptimomax + montoservicio + montomaterial + vehiculomonto

    updatepresu = Presupuesto.objects.filter(pk=pk)
    updatepresu.update(descripcion_vehiculo=descripcion_veh)
    updatepresu.update(cantidad_vehiculo=cant_vehiculo)
    updatepresu.update(monto_vehiculo_hora=montoveh_hrs)
    updatepresu.update(monto_vehiculo_recorrido=montoveh_km)
    updatepresu.update(total_capacidad_vehiculokg=cap_vehiculo)
    updatepresu.update(total_capacidad_vehiculovol=cap_vehiculo2)
    updatepresu.update(descripcion_persona=descripcion_pers)
    updatepresu.update(cantidad_ayudante=cant_ayudante)
    updatepresu.update(cantidad_ayudanteadicional=cant_ayudanteadic)
    updatepresu.update(monto_personateorica=round(montopersteorica, 2))
    updatepresu.update(monto_personaoptima=round(montopersoptima, 2))
    updatepresu.update(duracion_teorica=round(duracionteorica, 2))
    updatepresu.update(duracion_optima=round(duracion_optimamudanza, 2))
    updatepresu.update(monto_mudanza_hrsdirectas=round(montoteoricomudanza, 2))
    updatepresu.update(monto_mundanza_hrsoptimas=round(montooptimomudanza, 2))
    updatepresu.update(monto_m3_inmueble=round((totalm3mudanza*tarifa_m3), 2))
    updatepresu.update(monto_amb_inmueble=round((cant_amb*tarifa_amb), 2))
    updatepresu.update(total_peso_mudanza=round(totalpesomudanza, 3))
    updatepresu.update(total_m3=round(totalm3mudanza, 3))

    presupuesto = Presupuesto.objects.get(pk=pk)

    return(presupuesto)
