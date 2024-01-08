from django import forms
from django.forms import ModelForm
from .models import Blog
from django.contrib.auth.models import User  # Importa el modelo User si no lo has hecho
# from django import UserCreationFormulario, UserEditionFormulario
from .models import Blog
from django import forms


from .models import Avatar

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

from django.contrib.auth.forms import UserCreationForm, UserChangeForm, UserModel


class UserCreationFormulario(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

    class Meta:
        model = UserModel
        fields = ["password1", "password2", "username", "email"]
        help_texts = {k: "" for k in fields}


class UserEditionFormulario(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")

    class Meta:
        model = UserModel
        fields = ["email", "password1", "password2", "first_name", "last_name"]
        help_texts = {k: "" for k in fields}
        
class UserAvatarFormulario(forms.ModelForm):

    class Meta:
        model = Avatar
        fields = ["imagen"]