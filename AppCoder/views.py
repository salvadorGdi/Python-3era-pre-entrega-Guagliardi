from django.shortcuts import render
from .forms import CursoForm, ProfesorForm, EstudianteForm, BuscarCursoForm
from .models import Curso

# Create your views here.

def inicio(request):
    return render(request, "inicio.html")

def crear_curso(request):
    if request.method == "POST":
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CursoForm()
    return render(request, "curso_form.html", {"form": form})

def crear_profesor(request):
    if request.method == "POST":
        form = ProfesorForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ProfesorForm()
    return render(request, "profesor_form.html", {"form": form})

def crear_estudiante(request):
    if request.method == "POST":
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = EstudianteForm()
    return render(request, "estudiante_form.html", {"form": form})

def buscar_curso(request):
    resultado = None
    if request.method == "GET":
        form = BuscarCursoForm(request.GET)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            resultado = Curso.objects.filter(nombre__icontains=nombre)
    else:
        form = BuscarCursoForm()
    return render(request, "buscar_curso.html", {"form": form, "resultado": resultado})