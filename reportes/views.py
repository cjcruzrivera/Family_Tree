# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def desarrollador(request):
    return render(request, 'desarrollador.html')

def index(request):
    return render(request, 'index.html')

def index_reportes(request):
    return render(request, 'reportes/index.html')

# Create your views here.
