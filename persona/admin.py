# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from persona.models import Persona, Parejas

admin.site.register(Persona)
admin.site.register(Parejas)