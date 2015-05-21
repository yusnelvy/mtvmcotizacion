from django.shortcuts import render
from cotizacion.models import Estado_Cotizacion, Piso, Tiempo_Carga
from django.http import HttpResponseRedirect, HttpResponse
import simplejson as json
import django.db


# Create your views here.
# lista
def lista_estado_cotizacion(request):
    """docstring"""

    if request.method == "POST":
        if "item_id" in request.POST:
            try:
                id_estadocotizacion = request.POST['item_id']
                p = Estado_Cotizacion.objects.get(pk=id_estadocotizacion)
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

    lista_estadocotizacion = Estado_Cotizacion.objects.all()
    context = {'lista_estadocotizacion': lista_estadocotizacion}
    return render(request, 'cotizacion/estadocotizacion_lista.html', context)


def lista_piso(request):
    """docstring"""

    if request.method == "POST":
        if "item_id" in request.POST:
            try:
                id_piso = request.POST['item_id']
                p = Piso.objects.get(pk=id_piso)
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

    lista_piso = Piso.objects.all()
    context = {'lista_piso': lista_piso}
    return render(request, 'cotizacion/piso_lista.html', context)


def lista_tiempocarga(request):
    """docstring"""

    if request.method == "POST":
        if "item_id" in request.POST:
            try:
                id_tiempocarga = request.POST['item_id']
                p = Tiempo_Carga.objects.get(pk=id_tiempocarga)
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

    lista_tiempocarga = Tiempo_Carga.objects.all()
    context = {'lista_tiempocarga': lista_tiempocarga}
    return render(request, 'cotizacion/tiempocarga_lista.html', context)
