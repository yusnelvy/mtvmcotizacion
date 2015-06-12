"""
    # Espacio para la documentacion docstring
    # pendiente por elaborar
"""

from django.shortcuts import render


def pantalla_inicial(request):

    # Funcion para levantar la pantalla inicial del sistema
    #

    return render(request, 'inicio/base_menu.html')
