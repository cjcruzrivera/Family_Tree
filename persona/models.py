from django.db import models
from familia.models import Familia


# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    estado = models.BooleanField(default=True)
    padre = models.ForeignKey('self', related_name='padre_persona',blank=True, null=True)
    madre = models.ForeignKey('self', related_name='madre_persona',blank=True, null=True)
    abuelos = models.ManyToManyField('self',blank=True)
    hermanos = models.ManyToManyField('self',blank=True)
    tios = models.ManyToManyField('self', symmetrical=False,blank=True) 
    pareja = models.ManyToManyField('self', symmetrical=False, blank=True, through='Parejas', related_name='parejas_persona')  
    primos = models.ManyToManyField('self',blank=True)    
    generacion = models.IntegerField()
    familia = models.ForeignKey(Familia, null=True)

    def __unicode__(self):
        return '{}'.format(self.nombre)


class Parejas(models.Model):
    persona = models.ForeignKey(Persona)
    persona2 = models.ForeignKey(Persona, related_name='pareja_persona')
    estado = models.BooleanField()