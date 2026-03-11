from django.shortcuts import render, get_object_or_404
from .models import Estudiante,Profesor,Curso, Entregable

def index(request):
    return render(request,"task.html")

def second_task(request):
    return render(request,"Second_task.html")

def lista_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'estudiantes_list.html', {'estudiantes': estudiantes})

def detalle_estudiante(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    return render(request, 'estudiante_detail.html', {'estudiante': estudiante})