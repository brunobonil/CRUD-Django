from django.shortcuts import redirect, render
from .models import Curso
from django.contrib import messages

# Create your views here.

def home(request):
    cursos = Curso.objects.all()
    messages.success(request, '¡Cursos listados!')
    return render(request, "gestionCursos.html", {"cursos": cursos})

def registrarCurso(request):
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    creditos=request.POST['numCredito']

    curso=Curso.objects.create(codigo=codigo, nombre=nombre, creditos=creditos)
    messages.success(request, '¡Curso registrado!')

    return redirect('/')

def eliminarCurso(request, codigo):
    curso=Curso.objects.get(codigo=codigo)
    curso.delete()
    messages.success(request, '¡Curso eliminado!')
    return redirect('/')

def edicionCurso(request, codigo):
    cursos=Curso.objects.get(codigo=codigo)
    return render(request, "edicionCurso.html", {"curso": cursos})

def editarCurso(request):
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    creditos=request.POST['numCredito']

    curso=Curso.objects.get(codigo=codigo)
    curso.nombre = nombre
    curso.creditos = creditos
    curso.save()
    messages.success(request, '¡Curso modificado!')
    return redirect('/')


