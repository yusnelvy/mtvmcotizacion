from django.shortcuts import render
from mueble.models import Tipo_Mueble, Ocupacion
from django.http import HttpResponse
import simplejson as json
import django.db


# Create your views here.
# lista
def lista_tipo_mueble(request):
    """docstring"""

    if request.method == "POST":
        if "item_id" in request.POST:
            try:
                id_tipomueble = request.POST['item_id']
                p = Tipo_Mueble.objects.get(pk=id_tipomueble)
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

    lista_tipomueble = Tipo_Mueble.objects.all()
    context = {'lista_tipomueble': lista_tipomueble}
    return render(request, 'tipomueble_lista.html', context)


def lista_ocupacion(request):
    """docstring"""

    if request.method == "POST":
        if "item_id" in request.POST:
            try:
                id_ocupacion = request.POST['item_id']
                p = Ocupacion.objects.get(pk=id_ocupacion)
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

    lista_ocupacion = Ocupacion.objects.all()
    context = {'lista_ocupacion': lista_ocupacion}
    return render(request, 'ocupacion_lista.html', context)
