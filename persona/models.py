from django.db import models


# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    sexo = models.CharField(max_length=1)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    estado = models.BooleanField(default=True)
    generacion = models.IntegerField()

    def __unicode__(self):
        return self.nombre
