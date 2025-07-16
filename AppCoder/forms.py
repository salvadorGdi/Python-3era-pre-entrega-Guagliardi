from django import forms
from .models import Curso, Profesor, Estudiante

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre', 'camada']

class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = ['nombre', 'email']

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['nombre', 'curso']

class BuscarCursoForm(forms.Form):
    nombre = forms.CharField(label="Nombre del curso")