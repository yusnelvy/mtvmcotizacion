"""Docstring"""

from django.shortcuts import render, render_to_response
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect
from django.template.context import RequestContext
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required


def pantalla_inicial(request):
    """Docstring"""
    return render(request, 'base_menu.html')


def signup(request):
    """Docstring"""
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            email = form.cleaned_data["email"]
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            user = User.objects.create_user(username, email, password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()

            return HttpResponseRedirect(reverse('uinicio:pantalla_inicial'))
    else:
        form = SignUpForm()

    data = {
        'form': form,
    }
    return render_to_response('signup.html', data, context_instance=RequestContext(request))


@login_required()
def home(request):
    """Docstring"""
    return render_to_response('home.html',
                              {'user': request.user}, context_instance=RequestContext(request))
