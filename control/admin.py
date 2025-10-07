from django.contrib import admin

# Register your models here.

from .models import Departamento, Empleado

@admin.register(Departamento)
class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "ubicacion")

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "cargo", "salario", "departamento")