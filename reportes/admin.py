# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from reportes.models import Parentesco, Relaciones

admin.site.register(Parentesco)
admin.site.register(Relaciones)