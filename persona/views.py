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
        return redirect('persona:listar_personas')
    else:
        form = Persona_Form()
    return render(request, 'persona/persona_form.html', {'form':form})


def list_persona(request):
    persona = Persona.objects.all().order_by('id')
    contexto = {'personas':persona}
    return render(request, 'persona/persona_list.html', contexto)


def edit_persona(request, id_persona):
    persona = Persona.objects.get(id=id_persona)
    if request.method == "GET":
        form = Persona_Form(instance=persona)
    else:
        form = Persona_Form(request.POST,instance=persona)
        if form.is_valid():
            form.save()
            return redirect('persona:listar_personas')
    return render(request, 'persona/persona_form.html', {'form':form})

def delete_persona(request, id_persona):
    persona = Persona.objects.get(id=id_persona)
    if request.method == 'POST':
        persona.delete()
        return redirect('persona:listar_personas')
    return render(request, 'persona/persona_delete.html', {'persona': persona})