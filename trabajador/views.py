from django.shortcuts import render, render_to_response
from trabajador.models import Cargo_trabajador
from trabajador.models import CargotrabajadorForm
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.core.urlresolvers import reverse
import django.db
import simplejson as json


# Create your views here.
# lista
def lista_cargotrabajador(request):
    """docstring"""

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

    lista_cargo = Cargo_trabajador.objects.all()
    context = {'lista_cargo': lista_cargo}
    return render(request, 'trabajador/cargotrabajador_lista.html', context)


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
    return render_to_response('trabajador/cargotrabajador_add.html',
                              {'form_cargotrabajador': form_cargotrabajador, 'create': True},
                              context_instance=RequestContext(request))


# editar
def edit_cargotrabajador(request, pk):
    """docstring"""

    id_cargo = Cargo_trabajador.objects.get(pk=pk)

    if request.method == 'POST':
        # formulario enviado
        form_edit_cargotrabajador = CargotrabajadorForm(request.POST, instance=id_cargo)

        if form_edit_cargotrabajador.is_valid():
            # formulario validado correctamente
            form_edit_cargotrabajador.save()

            return HttpResponseRedirect(reverse('utrabajadores:lista_cargotrabajador'))
    else:
        # formulario inicial
        form_edit_cargotrabajador = CargotrabajadorForm(instance=id_cargo)

    return render_to_response('trabajador/cargotrabajador_edit.html',
                              {'form_edit_cargotrabajador': form_edit_cargotrabajador, 'create': False},
                              context_instance=RequestContext(request))
