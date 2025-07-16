from django.db import models

# Create your models here.

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    camada = models.IntegerField()
    def __str__(self):
        return f"{self.nombre} (Camada {self.camada})"

class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)