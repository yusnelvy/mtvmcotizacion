from django.contrib.auth import logout
from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, JsonResponse
from django.db.models import Q
from django.template import RequestContext
import re
from premisas.models import PerzonalizacionVisual


def logout_page(request):
    """
    Log users out and re-direct them to the main page.
    """
    logout(request)
    return HttpResponseRedirect('/')


def show_dashboard(request):
    """
    Mostrar el dashboard inicial
    """
    context = {'show_dashboard': ""}
    return render(request, 'base_menu.html', context)


# funciones para realizar las consultas de busqueda (search)
def normalize_query(query_string,
                    findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
                    normspace=re.compile(r'\s{2,}').sub):
    ''' Splits the query string in invidual keywords, getting rid of unecessary spaces
        and grouping quoted words together.
        Example:

        >>> normalize_query('  some random  words "with   quotes  " and   spaces')
        ['some', 'random', 'words', 'with quotes', 'and', 'spaces']

    '''
    return [normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)]


def get_query(query_string, search_fields):
    ''' Returns a query, that is a combination of Q objects. That combination
        aims to search keywords within a model by testing the given search fields.

    '''
    query = None  # Query to search for every search term
    terms = normalize_query(query_string)
    for term in terms:
        or_query = None  # Query to search for a given term in each field
        for field_name in search_fields:
            q = Q(**{"%s__icontains" % field_name: term})
            if or_query is None:
                or_query = q
            else:
                or_query = or_query | q
        if query is None:
            query = or_query
        else:
            query = query & or_query
    return query


def handler404(request):
    """error 404"""
    error = "Pagina no encontrada"
    response = render_to_response('404.html',
                                  {'codigo': 404, 'error': error},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request):
    """error 500"""
    error = "Error de servidor"
    response = render_to_response('404.html',
                                  {'codigo': 500, 'error': error},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response


def handler403(request):
    """error 403"""
    error = "Error, pagina prohibida acceso denegado."
    response = render_to_response('404.html',
                                  {'codigo': 403, 'error': error},
                                  context_instance=RequestContext(request))
    response.status_code = 403
    return response


def handler400(request):
    """error 400"""
    error = "Error, solicitud incorrecta."
    response = render_to_response('404.html',
                                  {'codigo': 400, 'error': error},
                                  context_instance=RequestContext(request))
    response.status_code = 400
    return response


def sidebarUpdate(request):
    """e"""
    sidebarStatus = PerzonalizacionVisual.objects.filter(usuario__username="std",
                                                        tipo="sidebarClosedOpen")

    if sidebarStatus[0].valor == '0':
        sidebarStatus.update(valor=1)
    else:
        sidebarStatus.update(valor=0)

    sidebarStatus = PerzonalizacionVisual.objects.values('valor').filter(usuario__username="std",
                                                                         tipo="sidebarClosedOpen")

    mensaje = {'estatus': 'ok', 'msj': 'Registro guardado', 'sidebarStatus': sidebarStatus[0]['valor']}
    return JsonResponse(mensaje, safe=False)


def sidebar(request):
    """e"""
    all_categories = PerzonalizacionVisual.objects.values('valor').filter(usuario__username="std",
                                                                          tipo="sidebarClosedOpen")

    return {
        'sidebar': all_categories[0]['valor'],
    }
