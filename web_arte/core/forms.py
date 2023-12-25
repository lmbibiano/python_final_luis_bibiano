from django import forms
from django.forms import ModelForm
from .models import Blog
from django.contrib.auth.models import User  # Importa el modelo User si no lo has hecho

from .models import Blog

# escribir formularios


# Estos son los formularios hechos por el usuario
class ArteFormulario(forms.Form):
    titulo = forms.CharField(max_length=40)
    url = forms.URLField()


class HistoriaFormulario(forms.Form):
    titulo = forms.CharField(max_length=40)
    url = forms.URLField()


class ArtistaFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    url = forms.URLField()
    
from django import forms
from .models import Blog

# class BlogForm(forms.ModelForm):
#     class Meta:
#         model = Blog
#         fields = ['titulo', 'descripcion', 'terminado', 'imprtante', 'rrss_url']
        


# 20/12 8 53

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['titulo', 'descripcion', 'terminado', 'imprtante', 'rrss_url', 'autor']

