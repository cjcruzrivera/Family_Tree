from django import forms

from familia.models import Familia

class Familia_Form(forms.ModelForm):

    class Meta:
        model = Familia
        fields = '__all__'
        labels = {
            'nombre': 'Nombre de la familia'
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
        }