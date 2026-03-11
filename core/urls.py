from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="task"),
    path("Segunda",views.second_task, name="Second Task"),
    path("estudiantes/",views.lista_estudiantes,name="Lista Estudiantes"),
    path('estudiantes/<int:pk>/', views.detalle_estudiante, name='detalle_estudiante')
]