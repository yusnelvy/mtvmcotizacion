"""
    # Espacio para la documentacion docstring
    # pendiente por elaborar
"""

from django.shortcuts import render, render_to_response
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect
from django.template.context import RequestContext
from .forms import SignUpForm

from django.contrib.auth.decorators import login_required


def pantalla_inicial(request):

    # Funcion para levantar la pantalla inicial del sistema
    #

    return render(request, 'inicio/base_menu.html')


def signup(request):
    if request.method == 'POST':  # If the form has been submitted...
        form = SignUpForm(request.POST)  # A form bound to the POST data
        if form.is_valid():  # All validation rules pass

            # Process the data in form.cleaned_data
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            email = form.cleaned_data["email"]
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]

            # At this point, user is a User object that has already been saved
            # to the database. You can continue to change its attributes
            # if you want to change other fields.
            user = User.objects.create_user(username, email, password)
            user.first_name = first_name
            user.last_name = last_name

            # Save new user attributes
            user.save()

            return HttpResponseRedirect(reverse('uinicio:pantalla_inicial'))  # Redirect after POST
    else:
        form = SignUpForm()

    data = {
        'form': form,
    }
    return render_to_response('inicio/signup.html', data, context_instance=RequestContext(request))


@login_required()
def home(request):
    return render_to_response('inicio/home.html', {'user': request.user}, context_instance=RequestContext(request))
