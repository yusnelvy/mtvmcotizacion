from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, JsonResponse
from django.views.generic import ListView, DetailView, View, UpdateView
from presupuesto.models import Presupuesto, Presupuesto_Detalle, \
    Presupuesto_direccion
from presupuesto.forms import PresupuestoForm, \
    PresupuestoDireccionForm, PresupuestoDetalleForm
from django.core.urlresolvers import reverse
from django.utils import timezone
from direccion.models import Complejidad_Inmueble, Tipo_Inmueble
from mueble.models import Ocupacion, Mueble, Tamano_Mueble, Tamano
from ambiente.models import Ambiente

from formtools.wizard.views import SessionWizardView


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
    template_name = 'presupuesto/presupuesto_ficha.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(PresupuestoDetail, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['presupuesto_list'] = Presupuesto.objects.all()
        context['now'] = timezone.now()
        return context


class PresupuestoDetalleList(ListView):
    model = Presupuesto_Detalle
    paginate_by = 25
    template_name = 'presupuesto/presupuestodetalle_lista.html'

    def get_queryset(self):
        queryset = super(PresupuestoDetalleList, self).get_queryset()
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
    template_name = 'presupuesto/presupuestodireccion_add.html'

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
    template_name = 'presupuesto/presupuestodetalle_add.html'

    def get(self, request, *args, **kwargs):

        if self.request.is_ajax():
            ambiente_id = self.request.GET.get('id_lista_ambiente')
            mueble_id = self.request.GET.get('id_lista_mueble')
            tamano_id = self.request.GET.get('id_lista_tamano')
            ocupacion_id = self.request.GET.get('id_ocupacion')

            if (mueble_id and tamano_id is None):
                mueble = Mueble.objects.get(id=mueble_id)
                if mueble:
                    mueble = [{
                        'mueble': mueble.mueble,
                        'ocupacion': mueble.ocupacion.id,
                        'descripocupacion': mueble.ocupacion.descripcion,
                        'valorocupacion': mueble.ocupacion.valor,
                        'capacidadmueble': mueble.capacidad
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
                        'peso': tamano[0].peso
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

        data = {
            'presupuesto': self.request.GET.get('pre')
            }

        form = self.form_class(initial=data)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            # <process form cleaned data>
            redirect_to = request.GET['next']

            if redirect_to:
                return HttpResponseRedirect(redirect_to)
            else:
                return HttpResponseRedirect(reverse('upresupuesto:PresupuestoList'))

        return render(request, self.template_name, {'form': form})


class PresupuestoUpdate(UpdateView):
    template_name = 'presupuesto/presupuesto_edit.html'
    form_class = PresupuestoForm
    model = Presupuesto

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()

        redirect_to = self.request.GET['next']
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
