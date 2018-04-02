# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect

from familia.forms import Familia_Form
from familia.models import Familia

# Create your views here.

def index(request):
    familia = Familia.objects.all().order_by("id")
    contexto = {'familias': familia}
    return render(request, 'familia/index.html', contexto)

def new_familia(request):
    if(request.method == 'POST'):
        form = Familia_Form(request.POST)
        if form.is_valid():
            form.save()
        return redirect('familia:index')
    else:
        form = Familia_Form()
    return render(request,'familia/familia_form.html', {'form':form})

def list_familia(request):
    familia = Familia.objects.all().order_by('id')
    contexto = {'familias': familia}
    return render(request, 'familia/familia_list.html', contexto)

def edit_familia(request, id_familia):
    familia = Familia.objects.get(id=id_familia)
    if request.method == "GET":
        form = Familia_Form(instance=familia)
    else:
        form = Familia_Form(request.POST, instance=familia)
        if form.is_valid():
            form.save()
        return redirect('familia:index')
    return render(request, 'familia/familia_form.html', {'form':form})

def delete_familia(request, id_familia):
    familia = Familia.objects.get(id=id_familia)
    if request.method == 'POST':
        familia.delete()
        return redirect('familia:listar_familias')
    return render(request, 'familia/familia_delete.html', {'familia':familia})    