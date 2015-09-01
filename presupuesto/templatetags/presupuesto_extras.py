from django import template

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
                horas = horas + ' con ' + str(minuto) + ' min'
        else:
            horas = str(entero + 1) + ' h'
    else:
        if minuto < 60:
            horas = str(minuto) + ' min'
        else:
            horas = str(entero + 1) + ' h'

    return (horas)
