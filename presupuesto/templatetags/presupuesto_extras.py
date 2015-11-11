from django import template
from django.core.urlresolvers import reverse

register = template.Library()


@register.simple_tag
def calular_horas(hora):
    """docstring"""
    entero = int(hora)
    residuo = abs(hora) - abs(int(hora))
    minuto = ((residuo/100)*60)*100
    minuto = round(minuto)
    if entero > 0:

        horas = str(entero) + ' h'

        if minuto < 60:
            if minuto > 0:
                horas = horas + ' ' + str(minuto) + ' min'
        else:
            horas = str(entero + 1) + ' h'
    else:
        if minuto < 60:
            horas = str(minuto) + ' min'
        else:
            horas = str(entero + 1) + ' h'

    return (horas)


@register.inclusion_tag('widget.html', takes_context=True)
def widget_sidebar(context, widget, titulo):
    """docstring"""
    orden = context['estado'][0]['estado__orden']
    if widget == 'acciones_ficha_presupuesto':
        data = data_acciones_presupuesto(context, orden)
        return {'context': context, 'widget': widget, 'titulo': titulo, 'data': data}
    if widget == 'pasos_presupuesto':
        data = data_pasos_presupuesto(context, orden)
        return {'context': context, 'widget': widget, 'titulo': titulo, 'data': data}
    if widget == 'acciones_resumen_presupuesto':
        data = data_acciones_resumen(context, orden)
        return {'context': context, 'widget': widget, 'titulo': titulo, 'data': data}


def data_acciones_resumen(context, orden):
    """docstring"""
    grupocon = context['user'].groups.count
    grupoall = context['user'].groups.all
    superusu = context['user'].is_superuser
    ree = context.request.user.groups.count
    if orden == 4:
        urlfinalizars = reverse('upresupuestos:presupuesto_finalizado_cliente',
                                args=(context['presupuesto'],))
        data = [
            {'btnNombre': grupocon,
             'url': '',
             'datanumero': context['presupuesto'],
             'dataopcion': urlfinalizars + '?estado_orden=5',
             'botonFinalizar': 'botonFinalizar',
             'elementoHidden': '1'}
        ]
        return data
    if orden == 5:
        if ree == 1:
            for group in grupoall:
                if group == 'cotizador':
                    urlfinalizars = reverse('upresupuestos:presupuesto_finalizado_cliente',
                                            args=(context['presupuesto'],))
                    data = [
                        {'btnNombre': 'paso',
                         'url': '',
                         'datanumero': context['presupuesto'],
                         'dataopcion': urlfinalizars + '?estado_orden=5',
                         'botonFinalizar': 'botonFinalizar',
                         'elementoHidden': '1'}
                    ]
                    return data
                else:
                    urlfinalizars = reverse('upresupuestos:presupuesto_finalizado_cliente',
                                            args=(context['presupuesto'],))
                    data = [
                        {'btnNombre': grupoall,
                         'url': '',
                         'datanumero': context['presupuesto'],
                         'dataopcion': urlfinalizars + '?estado_orden=5',
                         'botonFinalizar': 'botonFinalizar',
                         'elementoHidden': '1'}
                    ]
                    return data

        elif superusu:
            urlfinalizars = reverse('upresupuestos:presupuesto_finalizado_cliente',
                                    args=(context['presupuesto'],))
            data = [
                {'btnNombre': grupoall,
                 'url': '',
                 'datanumero': context['presupuesto'],
                 'dataopcion': urlfinalizars + '?estado_orden=5',
                 'botonFinalizar': 'botonFinalizar',
                 'elementoHidden': '1'}
            ]
            return data
        else:
            urlfinalizars = reverse('upresupuestos:presupuesto_finalizado_cliente',
                                    args=(context['presupuesto'],))
            data = [
                {'btnNombre': grupoall,
                 'url': '',
                 'datanumero': context['presupuesto'],
                 'dataopcion': urlfinalizars + '?estado_orden=5',
                 'botonFinalizar': 'botonFinalizar',
                 'elementoHidden': '1'}
            ]
            return data


def data_pasos_presupuesto(context, orden):
    """docstring"""
    dni = context['presupuesto'].dni
    dorigen = context['direccion_origen']
    ddestino = context['direccion_destino']
    listaa = context['lista_ambiente']
    if orden == 1 or orden == 2 or orden == 3:
        if dni and dorigen and ddestino and listaa:
            data = [
                {'paso': 'Datos básicos del presupuesto',
                 'ancla': '#datos-personales',
                 'span': 'ok'},
                {'paso': 'Direcciones',
                 'ancla': '#direcciones',
                 'span': 'ok'},
                {'paso': 'Muebles a mudar',
                 'ancla': '#ambientes',
                 'span': 'ok'},
                {'paso': 'Servicios contratados',
                 'ancla': '#',
                 'span': 'minus'}
            ]
            return data
        elif dni and dorigen and ddestino:
            data = [
                {'paso': 'Datos básicos del presupuesto',
                 'ancla': '#datos-personales',
                 'span': 'ok'},
                {'paso': 'Direcciones',
                 'ancla': '#direcciones',
                 'span': 'ok'},
                {'paso': 'Muebles a mudar',
                 'ancla': '#ambientes',
                 'span': 'minus'},
                {'paso': 'Servicios contratados',
                 'ancla': '#',
                 'span': 'minus'}
            ]
            return data
        elif dni:
            data = [
                {'paso': 'Datos básicos del presupuesto',
                 'ancla': '#datos-personales',
                 'span': 'ok'},
                {'paso': 'Direcciones',
                 'ancla': '#direcciones',
                 'span': 'minus'},
                {'paso': 'Muebles a mudar',
                 'ancla': '#ambientes',
                 'span': 'minus'},
                {'paso': 'Servicios contratados',
                 'ancla': '#',
                 'span': 'minus'}
            ]
            return data
    else:
        if dni and dorigen and ddestino and listaa:
            data = [
                {'paso': 'Datos básicos del presupuesto',
                 'ancla': '#datos-personales',
                 'span': 'ok'},
                {'paso': 'Direcciones',
                 'ancla': '#direcciones',
                 'span': 'ok'},
                {'paso': 'Muebles a mudar',
                 'ancla': '#ambientes',
                 'span': 'ok'},
                {'paso': 'Servicios contratados',
                 'ancla': '#',
                 'span': 'ok'}
            ]
            return data
        elif dni and dorigen and ddestino:
            data = [
                {'paso': 'Datos básicos del presupuesto',
                 'ancla': '#datos-personales',
                 'span': 'ok'},
                {'paso': 'Direcciones',
                 'ancla': '#direcciones',
                 'span': 'ok'},
                {'paso': 'Muebles a mudar',
                 'ancla': '#ambientes',
                 'span': 'minus'},
                {'paso': 'Servicios contratados',
                 'ancla': '#',
                 'span': 'ok'}
            ]
            return data
        elif dni:
            data = [
                {'paso': 'Datos básicos del presupuesto',
                 'ancla': '#datos-personales',
                 'span': 'ok'},
                {'paso': 'Direcciones',
                 'ancla': '#direcciones',
                 'span': 'minus'},
                {'paso': 'Muebles a mudar',
                 'ancla': '#ambientes',
                 'span': 'minus'},
                {'paso': 'Servicios contratados',
                 'ancla': '#',
                 'span': 'ok'}
            ]
            return data


def data_acciones_presupuesto(context, orden):
    """docstring"""
    activo = context['presupuesto'].activo.orden
    nexturl = context.request.path
    if activo != 9:
        if orden == 3:
            data = [
                {'btnNombre': 'Como contratar servicios',
                 'url': "$('.comoContratarServicio').modal();",
                 'elementoHidden': '1'}
            ]
            return data
        if orden == 4:
            urlverresumen = reverse('upresupuestos:PresupuestoDetailResumen',
                                    args=(context['presupuesto'],))
            urlfinalizars = reverse('upresupuestos:presupuesto_finalizado_cliente',
                                    args=(context['presupuesto'],))
            data = [
                {'btnNombre': 'Ver resumen',
                 'url': 'location="' + urlverresumen + '"'},
                {'btnNombre': 'Finalizar solicitud',
                 'url': '',
                 'datanumero': context['presupuesto'],
                 'dataopcion': urlfinalizars + '?estado_orden=5',
                 'botonFinalizar': 'botonFinalizar'}
            ]
            return data
        if orden == 5:
            urlverresumen = reverse('upresupuestos:PresupuestoDetailResumen',
                                    args=(context['presupuesto'],))
            urlrevisar = reverse('upresupuestos:PresupuestoRevisarUpdateView',
                                 args=(context['presupuesto'],))
            urlautorizar = reverse('upresupuestos:presupuesto_finalizado_cliente',
                                   args=(context['presupuesto'],))
            data = [
                {'btnNombre': 'Ver resumen',
                 'url': 'location="' + urlverresumen + '"'},
                {'btnNombre': 'Revisar presupuesto',
                 'url': 'location="' + urlrevisar + '?next=' + str(nexturl) + '"',
                 'btnsuccess': 'default'},
                {'btnNombre': 'Terminar presupuesto',
                 'url': '',
                 'datanumero': context['presupuesto'],
                 'dataopcion': urlautorizar + '?estado_orden=7&terminar=terminar',
                 'botonFinalizar': 'botonFinalizar',
                 'btnsuccess': 'success'}
            ]
            return data
        if orden == 6:
            urlverresumen = reverse('upresupuestos:PresupuestoDetailResumen',
                                    args=(context['presupuesto'],))
            urlrevisar = reverse('upresupuestos:PresupuestoRevisarUpdateView',
                                 args=(context['presupuesto'],))
            urlautorizar = reverse('upresupuestos:presupuesto_finalizado_cliente',
                                   args=(context['presupuesto'],))
            data = [
                {'btnNombre': 'Ver resumen',
                 'url': 'location="' + urlverresumen + '"'},
                {'btnNombre': 'Revisar presupuesto',
                 'url': 'location="' + urlrevisar + '?next=' + str(nexturl) + '"',
                 'btnsuccess': 'default'},
                {'btnNombre': 'Autorizar',
                 'url': '',
                 'datanumero': context['presupuesto'],
                 'dataopcion': urlautorizar + '?estado_orden=7',
                 'botonFinalizar': 'botonFinalizar',
                 'btnsuccess': 'success'}
            ]
            return data
        if orden == 7:
            urlverresumen = reverse('upresupuestos:PresupuestoDetailResumen',
                                    args=(context['presupuesto'],))
            urlrevisar = reverse('upresupuestos:PresupuestoRevisarUpdateView',
                                 args=(context['presupuesto'],))
            urlautorizar = reverse('upresupuestos:presupuesto_finalizado_cliente',
                                   args=(context['presupuesto'],))
            data = [
                {'btnNombre': 'Ver resumen',
                 'url': 'location="' + urlverresumen + '"'},
                {'btnNombre': 'Revisar presupuesto',
                 'url': 'location="' + urlrevisar + '?next=' + str(nexturl) + '"',
                 'btnsuccess': 'default'},
                {'btnNombre': 'Enviar correo',
                 'btnsuccess': 'success'},
                {'btnNombre': 'Reabrir el presupuesto',
                 'url': '',
                 'datanumero': context['presupuesto'],
                 'dataopcion': urlautorizar + '?estado_orden=5',
                 'botonFinalizar': 'botonFinalizar'}
            ]
            return data
    else:
        urlactivar = reverse('upresupuestos:presupuesto_finalizado_cliente',
                             args=(context['presupuesto'],))
        data = [
            {'btnNombre': 'Activar presupuesto',
             'url': '',
             'datanumero': context['presupuesto'],
             'dataopcion': urlactivar + '?estado_orden=' + str(nexturl) + '&activar=Activo',
             'botonFinalizar': 'botonFinalizar',
             'elementoHidden': '1'}
        ]
        return data
