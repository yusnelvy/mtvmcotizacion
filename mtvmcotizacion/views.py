from django.contrib.auth import logout
from django.http import HttpResponseRedirect


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
