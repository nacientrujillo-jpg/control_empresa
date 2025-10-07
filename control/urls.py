from django.urls import path
from . import views

app_name = "control"

urlpatterns = [
    # Departamentos
    path("departamentos/", views.DepartamentoListView.as_view(), name="departamento_list"),
    path("departamentos/nuevo/", views.DepartamentoCreateView.as_view(), name="departamento_create"),
    path("departamentos/<int:pk>/editar/", views.DepartamentoUpdateView.as_view(), name="departamento_update"),
    path("departamentos/<int:pk>/eliminar/", views.DepartamentoDeleteView.as_view(), name="departamento_delete"),

    # Empleados
    path("empleados/", views.EmpleadoListView.as_view(), name="empleado_list"),
    path("empleados/nuevo/", views.EmpleadoCreateView.as_view(), name="empleado_create"),
    path("empleados/<int:pk>/", views.EmpleadoDetailView.as_view(), name="empleado_detail"),
    path("empleados/<int:pk>/editar/", views.EmpleadoUpdateView.as_view(), name="empleado_update"),
    path("empleados/<int:pk>/eliminar/", views.EmpleadoDeleteView.as_view(), name="empleado_delete"),
]
