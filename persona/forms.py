from django import forms
from persona.models import Persona

class Persona_Form(forms.ModelForm):

    class Meta:
        model = Persona
        
        fields = [
            'nombre',
            'fecha_nacimiento',
            'padre',
            'madre'
        ]
        labels = {
            'nombre': 'Nombre Completo',
            'fecha_nacimiento': 'Fecha de Nacimiento',
            'padre': 'Padre',
            'madre': 'Madre'
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'padre': forms.Select(attrs={'class':'form-control'}),
            'madre': forms.Select(attrs={'class':'form-control'}),
        }