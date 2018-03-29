# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse

from persona.forms import Persona_Form
from persona.models import Persona
# Create your views here.


def index(request):
    return render(request, 'persona/index.html')


def new_persona(request):
    if request.method == 'POST':
        form = Persona_Form(request.POST)
        if form.is_valid():
            registro = form.save(commit=False)
            if registro.padre:
                registro.generacion = registro.padre.generacion + 1
                registro.familia = registro.padre.familia            
            else:
                registro.generacion = 0
                registro.familia = None
            
            registro.save()
        return redirect('persona:index')
    else:
        form = Persona_Form()
    return render(request, 'persona/persona_form.html', {'form':form})


def list_persona(request):
    persona = Persona.objects.all()
    contexto = {'personas':persona}
    return render(request, 'persona/persona_list.html', contexto)