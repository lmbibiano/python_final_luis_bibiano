from django.db import models
from django.contrib.auth.models import User  # Importa el modelo User si no lo has hecho


#los modelos ya creados y guardados 
class Curso(models.Model):
    titulo = models.CharField(max_length=40)
    url = models.URLField(null=True)

    def __str__(self):
        return self.titulo


class Historial(models.Model):
    titulo = models.CharField(max_length=40)
    url = models.URLField(null=True)

    def __str__(self):
        return self.titulo


class Artista(models.Model):
    nombre = models.CharField(max_length=40)
    url = models.URLField(null=True)

    def __str__(self):
        return self.nombre
    

class Blog(models.Model):
    titulo = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True)
    creación = models.DateField(auto_now_add=True)
    terminado = models.DateField(null=True)
    imprtante = models.BooleanField()
    rrss_url = models.URLField(null=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.titulo + ' por ' + self.autor.username