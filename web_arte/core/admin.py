
from django.contrib import admin
from .models import Curso, Historial, Artista
from .models import Blog
from . import models

# Register your models here.

# modelos registrados en el administrador
admin.site.register(Curso)
admin.site.register(Historial)
admin.site.register(Artista)
admin.site.register(Blog)


admin.site.register(models.Avatar)

admin.site.register(models.Post)
admin.site.register(models.Comentario)
admin.site.register(models.Perfil)

