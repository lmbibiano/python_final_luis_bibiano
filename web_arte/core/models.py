from django.db import models
from django.contrib.auth.models import User  
from django.contrib.auth.models import User#     Importa el modelo User si no lo has hecho


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
    

from django.contrib.auth.models import User

class Avatar(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.FileField(upload_to="media/avatares", null=True, blank=True)

    def __str__(self):
        return f"{self.user} - {self.imagen}"
    
class Perfil(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=2200)

    def __str__(self):
        return f"{self.usuario}"


class Post(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.FileField(upload_to="media/posts", null=True, blank=True)
    epigrafe = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.epigrafe}"


class Comentario(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.CharField(max_length=2200)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f"@{self.autor}: '{self.post}'"