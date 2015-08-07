from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, JsonResponse
from django.views.generic import ListView, DetailView, View, UpdateView
from presupuesto.models import Presupuesto, Presupuesto_Detalle, \
    Presupuesto_direccion, Presupuesto_servicio
from presupuesto.forms import PresupuestoForm, \
    PresupuestoDireccionForm, PresupuestoDetalleForm, \
    PresupuestoServicioForm
from django.core.urlresolvers import reverse
from django.utils import timezone
from direccion.models import Complejidad_Inmueble, Tipo_Inmueble
from mueble.models import Ocupacion, Mueble, Tamano_Mueble, Tamano
from ambiente.models import Ambiente
from servicio.models import Servicio, Complejidad_Servicio, Material, Servicio_Material
from contenido.models import Contenido_Tipico, Contenido_Servicio

from formtools.wizard.views import SessionWizardView
from django.forms.formsets import formset_factory

from django.db.models import Count


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
        return render_to_response('presupuesto/presupuestodetalle_add.html', {
            'form_data': [form.cleaned_data for form in form_list],
        })


# Create your views here.
class PresupuestoList(ListView):
    model = Presupuesto
    paginate_by = 10
    context_object_name = 'presupuestos'
    template_name = 'presupuesto/presupuesto_lista.html'

    def get_queryset(self):
        queryset = super(PresupuestoList, self).get_queryset()
        return queryset.filter()


class PresupuestoDetail(DetailView):

    model = Presupuesto
    context_object_name = "presupuesto"
    template_name = 'presupuesto/presupuesto_ficha2.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(PresupuestoDetail, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        #context['listar_ambiente'] = Presupuesto_Detalle.objects.values('ambiente', 'ambiente__ambiente', 'mueble').annotate(tcount=Count('ambiente')).order_by('ambiente')
        context['detalle_list'] = Presupuesto_Detalle.objects.filter(presupuesto=self.object.pk)
        context['lista_ambiente'] = Presupuesto_Detalle.objects.filter(presupuesto=self.object.pk).values('ambiente').distinct()
        context['direccion_origen'] = Presupuesto_direccion.objects.filter(presupuesto=self.object.pk, tipo_direccion="Origen")
        context['direccion_destino'] = Presupuesto_direccion.objects.filter(presupuesto=self.object.pk, tipo_direccion="Destino")
        context['now'] = timezone.now()
        context['servicio'] = Presupuesto_servicio.objects.filter(detalle_presupuesto__presupuesto=self.object.pk).values('servicio', 'detalle_presupuesto', 'tarifa').annotate(tcount=Count('servicio')).order_by('servicio')

        return context


class PresupuestoDetalleList(ListView):
    model = Presupuesto_Detalle
    paginate_by = 25
    template_name = 'presupuesto/presupuestodetalle_lista.html'

    def get_queryset(self):
        queryset = super(PresupuestoDetalleList, self).get_queryset()
        return queryset.filter()


class PresupuestoDetalleDetail(DetailView):

    model = Presupuesto_Detalle
    template_name = 'presupuesto/presupuestodetalle_ficha.html'
    context_object_name = "detallepresupuesto"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(PresupuestoDetalleDetail, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['servicio_list'] = Presupuesto_servicio.objects.filter(detalle_presupuesto=self.object.pk)
        context['now'] = timezone.now()
        return context


class PresupuestoDireccionList(ListView):
    model = Presupuesto_direccion
    paginate_by = 25
    template_name = 'presupuesto/presupuestodireccion_lista.html'

    def get_queryset(self):
        queryset = super(PresupuestoDireccionList, self).get_queryset()
        return queryset.filter(presupuesto_id=self.kwargs['presupuesto_id'])


class PresupuestoView(View):
    form_class = PresupuestoForm
    template_name = 'presupuesto/presupuesto_add.html'

    def get(self, request, *args, **kwargs):

        data = {
            'cotizador': self.request.user
        }

        form = self.form_class(initial=data)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            # <process form cleaned data>
            return HttpResponseRedirect('/presupuesto/')

        return render(request, self.template_name, {'form': form})


class PresupuestoDireccionView(View):
    form_class = PresupuestoDireccionForm
    template_name = 'presupuesto/presupuestodireccion_add2.html'

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

        complejidad = Complejidad_Inmueble.objects.get(complejidad='Media')
        ocupacion = Ocupacion.objects.get(id=3)

        data = {
            'presupuesto': self.request.GET['pre'],
            'tipo_direccion': request.GET['tipo'],
            'complejidad': complejidad,
            'factor_complejidad': complejidad.factor,
            'valor_ambiente_complejidad': complejidad.valor_ambiente,
            'valor_metrocubico_complejiadad': complejidad.valor_metrocubico,
            'lista_ocupacion': ocupacion.id,
            'ocupacidad_inmueble': ocupacion.descripcion,
            'valor_ocupacidad': ocupacion.valor
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
            # <process form cleaned data>
            redirect_to = request.GET['next']

            if redirect_to:
                return HttpResponseRedirect(redirect_to)
            else:
                return HttpResponseRedirect(reverse('upresupuesto:PresupuestoList'))

        return render(request, self.template_name, {'form': form})


class PresupuestoDetalleView(View):
    form_class = PresupuestoDetalleForm
    template_name = 'presupuesto/presupuestodetalle_add2.html'

    def get(self, request, *args, **kwargs):

        if self.request.is_ajax():
            ambiente_id = self.request.GET.get('id_lista_ambiente')
            mueble_id = self.request.GET.get('id_lista_mueble')
            tamano_id = self.request.GET.get('id_lista_tamano')
            ocupacion_id = self.request.GET.get('id_ocupacion')

            if (mueble_id and tamano_id is None):
                mueble = Mueble.objects.get(id=mueble_id)
                contenido = Contenido_Tipico.objects.filter(mueble=mueble_id, predefinido=True)[:1]
                contenidoservicio = Contenido_Servicio.objects.filter(contenido=contenido[0].contenido_id, predefinido=True)
                contenedor = Material.objects.filter(servicio_material__servicio_id=contenidoservicio[0].servicio_id, contenedor=True)[:1]

                if mueble:
                    mueble = [{
                        'mueble': mueble.mueble,
                        'ocupacion': mueble.ocupacion.id,
                        'descripocupacion': mueble.ocupacion.descripcion,
                        'valorocupacion': mueble.ocupacion.valor,
                        'capacidadmueble': mueble.capacidad,
                        'densidadcontenido': contenido[0].contenido.densidad_media,
                        'vol_contenedor': round(contenedor[0].volumen, 2),
                        'peso_contenedor': round(contenedor[0].peso, 2),
                        'capacidadvolcontenedor': contenedor[0].capacidad_volumen,
                        'capacidadpesocontenedor': contenedor[0].capacidad_peso,
                        'descripcioncontenedor': contenedor[0].material
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
                tamano = Tamano_Mueble.objects.filter(tamano_id=tamano_id, mueble_id=mueble_id)[:1]

                if tamano:
                    tamano = [{
                        'tamano': tamano[0].tamano.descripcion,
                        'densidad': tamano[0].densidad.descripcion,
                        'ancho': tamano[0].ancho,
                        'largo': tamano[0].largo,
                        'alto': tamano[0].alto,
                        'peso': tamano[0].peso,
                        'valor_densidad': round(tamano[0].densidad_valor, 2),
                        'volumen_mueble': round(tamano[0].volumenmueble, 2),
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
                'presupuesto': self.request.GET.get('pre'),
                }

        form = self.form_class(initial=data)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()

            presu = Presupuesto_Detalle.objects.filter(presupuesto=self.request.POST.get('presupuesto'))
            cant_ambiente = presu.annotate(acount=Count('ambiente')).order_by('ambiente')
            cant_mueble = presu.count()
            #prueba para ver si actualiza el campo cant ambiente en la cotizacion
            reporter = Presupuesto.objects.filter(pk=self.request.POST.get('presupuesto'))
            reporter.update(cantidad_ambientes=cant_ambiente[0].acount)
            reporter.update(cantidad_muebles=cant_mueble)

            # <process form cleaned data>
            redirect_to = request.GET['next']

            if redirect_to:
                return HttpResponseRedirect(redirect_to)
            else:
                return HttpResponseRedirect(reverse('upresupuesto:PresupuestoList'))

        return render(request, self.template_name, {'form': form})


class PresupuestoServicioView(View):
    form_class = PresupuestoServicioForm
    template_name = 'presupuesto/presupuestoservicio_add3.html'

    def get(self, request, *args, **kwargs):

        if self.request.is_ajax():
            servicio_id = self.request.GET.get('id_lista_servicio')
            if servicio_id:
                servicio = Servicio.objects.get(id=servicio_id)
                if servicio:
                    servicio = [{
                        'servicio': servicio.servicio
                    }]
                return JsonResponse(servicio, safe=False)

        if self.request.GET.get('serv'):
            serviciod = self.request.GET.get('serv')
            servicio = Servicio.objects.get(servicio=serviciod)

            data = {
                'detalle_presupuesto': self.request.GET.get('pre'),
                'servicio': servicio.servicio,
                'lista_servicio': servicio.id
            }
        else:
            data = {
                'detalle_presupuesto': self.request.GET.get('pre'),
            }

        form = self.form_class(initial=data)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):

        form = self.form_class(request.POST)
        if form.is_valid():
            complejidad = Complejidad_Servicio.objects.filter(servicio=self.request.POST.get('lista_servicio'), complejidad__descripcion='Media')
            if complejidad:
                tarifa = complejidad[0].tarifa
                factor_tiempo = complejidad[0].factor_tiempo

            materiales = Servicio_Material.objects.filter(servicio=self.request.POST.get('lista_servicio'))
            mueble = Presupuesto_Detalle.objects.get(id=self.request.POST.get('detalle_presupuesto'))

            for material in materiales:
                tiempoaplicado = 0
                if material.material.contenedor is True:
                    tiempoaplicado = factor_tiempo
                else:
                    tiempoaplicado = (factor_tiempo * mueble.volumen_mueble)

                agregar = Presupuesto_servicio.objects.create(servicio=self.request.POST.get('servicio'),
                                                              tarifa=tarifa, material=material.material.material,
                                                              monto_material=material.material.precio,
                                                              volumen_material=material.material.volumen,
                                                              peso_material=material.material.peso,
                                                              detalle_presupuesto_id=self.request.POST.get('detalle_presupuesto'),
                                                              tiempo_aplicado=tiempoaplicado)
                agregar.save()

            # <process form cleaned data>
            redirect_to = request.GET['next']

            if redirect_to:
                return HttpResponseRedirect(redirect_to)
            else:
                return HttpResponseRedirect(reverse('upresupuesto:PresupuestoList'))

        return render(request, self.template_name, {'form': form})


class PresupuestoServicioViewFomset(View):
    form_class_formset = formset_factory(PresupuestoServicioForm, extra=5)
    template_name = 'presupuesto/presupuestoservicio_add2.html'

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
            return HttpResponseRedirect('/presupuesto/')

        return render(request, self.template_name, {'formset': formset})


class PresupuestoUpdate(UpdateView):
    template_name = 'presupuesto/presupuesto_edit.html'
    form_class = PresupuestoForm
    model = Presupuesto

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()

        redirect_to = request.GET['next']
        if redirect_to:
            return HttpResponseRedirect(redirect_to)
        else:
            return render_to_response(self.template_name, self.get_context_data())


class PresupuestoGenarar(UpdateView):
    template_name = 'presupuesto/presupuesto_edit.html'
    form_class = PresupuestoForm
    model = Presupuesto

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()

        redirect_to = request.GET['next']
        if redirect_to:
            return HttpResponseRedirect(redirect_to)
        else:
            return render_to_response(self.template_name, self.get_context_data())



class PresupuestoDireccionUpdate(UpdateView):
    template_name = 'presupuesto/presupuestodireccion_edit.html'
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

        redirect_to = self.request.GET['next']
        if redirect_to:
            return HttpResponseRedirect(redirect_to)
        else:
            return render_to_response(self.template_name, self.get_context_data())


class PresupuestoDetalleUpdate(UpdateView):
    template_name = 'presupuesto/presupuestodetalle_edit.html'
    form_class = PresupuestoDetalleForm
    model = Presupuesto_Detalle

    def get_initial(self):
        super(PresupuestoDetalleUpdate, self).get_initial()
        lista_ambiente = Ambiente.objects.get(ambiente=self.object.ambiente)
        lista_mueble = Mueble.objects.get(mueble=self.object.mueble)
        lista_tamano = Tamano.objects.get(descripcion=self.object.tamano)
        lista_ocupacion = Ocupacion.objects.get(descripcion=self.object.ocupacidad)
        self.initial = {
            "lista_mueble": lista_mueble.id,
            "lista_ambiente": lista_ambiente.id,
            "lista_tamano": lista_tamano.id,
            "lista_ocupacion": lista_ocupacion.id
            }
        return self.initial

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()

        presu = Presupuesto_Detalle.objects.filter(presupuesto=self.request.POST.get('presupuesto'))
        cant_ambiente = presu.annotate(acount=Count('ambiente')).order_by('ambiente')
        cant_mueble = presu.count()
        #prueba para ver si actualiza el campo cant ambiente en la cotizacion
        reporter = Presupuesto.objects.filter(pk=self.request.POST.get('presupuesto'))
        reporter.update(cantidad_ambientes=cant_ambiente[0].acount)
        reporter.update(cantidad_muebles=cant_mueble)

        redirect_to = self.request.GET['next']
        if redirect_to:
            return HttpResponseRedirect(redirect_to)
        else:
            return render_to_response(self.template_name, self.get_context_data())


class PresupuestoServicioUpdate(UpdateView):
    template_name = 'presupuesto/presupuestoservivio_edit.html'
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


def ajax_tamano_request(request):
    # Expect an auto 'type' to be passed in via Ajax and POST
    if request.is_ajax() and request.method == 'POST':
        mueble = Mueble.objects.filter(id=request.POST.get('mueble', ''))
        tamanos = mueble.Tamano_Mueble.all()
        # get all the colors for this type of auto.
        mensaje = {'tamanos': tamanos}
        return JsonResponse(mensaje, safe=False)


#
