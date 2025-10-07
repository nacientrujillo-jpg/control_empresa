from django import forms
from .models import Empleado, Departamento

class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = ['nombre', 'ubicacion']

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['nombre', 'cargo', 'salario', 'foto', 'departamento']
