from django.shortcuts import render

# Create your views here.

from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Departamento, Empleado
from .forms import DepartamentoForm, EmpleadoForm

# Departamento
class DepartamentoListView(ListView):
    model = Departamento
    template_name = "control/departamento_list.html"
    context_object_name = "departamentos"

class DepartamentoCreateView(CreateView):
    model = Departamento
    form_class = DepartamentoForm
    template_name = "control/departamento_form.html"
    success_url = reverse_lazy("control:departamento_list")

class DepartamentoUpdateView(UpdateView):
    model = Departamento
    form_class = DepartamentoForm
    template_name = "control/departamento_form.html"
    success_url = reverse_lazy("control:departamento_list")

class DepartamentoDeleteView(DeleteView):
    model = Departamento
    template_name = "control/departamento_confirm_delete.html"
    success_url = reverse_lazy("control:departamento_list")

# Empleado
class EmpleadoListView(ListView):
    model = Empleado
    template_name = "control/empleado_list.html"
    context_object_name = "empleados"

class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "control/empleado_detail.html"
    context_object_name = "empleado"

class EmpleadoCreateView(CreateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = "control/empleado_form.html"
    success_url = reverse_lazy("control:empleado_list")

class EmpleadoUpdateView(UpdateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = "control/empleado_form.html"
    success_url = reverse_lazy("control:empleado_list")

class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "control/empleado_confirm_delete.html"
    success_url = reverse_lazy("control:empleado_list")
