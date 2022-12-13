from django import forms
from ejemplo.models import Familiar, Mascota , Auto

class Buscar(forms.Form):
    nombre = forms.CharField(max_length=100)
    
class FamiliarForm(forms.ModelForm):
  class Meta:
    model = Familiar
    fields = ['nombre', 'direccion', 'numero_pasaporte', 'fecha_nacimiento' ]

#MASCOTA

class MascotaForm(forms.ModelForm):
  class Meta:
    model = Mascota
    fields = ['propietario', 'nombre', 'raza' ]

#AUTO
class AutoForm(forms.ModelForm):
  class Meta:
    model = Auto
    fields = ['propietario', 'modelo']