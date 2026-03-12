from django.urls import path
from . import views

urlpatterns = [
    path("",views.lista_estudiantes,name="Lista Estudiantes"),
    path('estudiantes/<int:pk>/', views.detalle_estudiante, name='detalle_estudiante')
]