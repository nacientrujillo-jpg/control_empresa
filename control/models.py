from django.db import models

# Create your models here.

class Departamento(models.Model):
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.nombre

class Empleado(models.Model):
    nombre = models.CharField(max_length=150)
    cargo = models.CharField(max_length=100)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    foto = models.ImageField(upload_to="empleados_fotos/", blank=True, null=True)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, related_name="empleados")

    def __str__(self):
        return f"{self.nombre} - {self.cargo}"