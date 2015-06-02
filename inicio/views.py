"""
    # Espacio para la documentacion docstring
    # pendiente por elaborar
"""

from django.shortcuts import render

# Create your views here.


def pantalla_inicial(request):

    # Funcion para levantar la pantalla inicial del sistema
    #

    return render(request, 'base_menu.html')
