from django.shortcuts import render, redirect
from .models import Blog, Curso, Historial, Artista
from .forms import ArteFormulario, HistoriaFormulario, ArtistaFormulario, BlogForm
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UserCreationFormulario, UserEditionFormulario
from django.contrib.auth.views import PasswordChangeView
from .models import Avatar
from .forms import UserAvatarFormulario, UserAvatarFormulario# Importa el modelo Avatar desde tu archivo models.py


# Create your views here.


# este es el formulario que esta en el index
def arteFormulario(request):
    cursos = Curso.objects.all()
    if request.method == "POST":
        miFormulario = ArteFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            curso = Curso(titulo=informacion["titulo"], url=informacion["url"])
            curso.save()
    else:
        miFormulario = ArteFormulario()
    return render(
        request, "core/index.html", {"miFormulario": miFormulario, "cursos": cursos}
    )


def historiaFormulario(request):
    historias = Historial.objects.all()
    if request.method == "POST":
        fomularioHistoria = HistoriaFormulario(request.POST)
        print(fomularioHistoria)
        if fomularioHistoria.is_valid():
            informacion2 = fomularioHistoria.cleaned_data
            historia = Historial(titulo=informacion2["titulo"], url=informacion2["url"])
            historia.save()
    else:
        fomularioHistoria = HistoriaFormulario()
    return render(
        request,
        "core/historia.html",
        {"fomularioHistoria": fomularioHistoria, "historias": historias},
    )


def artistaFormulario(request):
    artistas = Artista.objects.all()
    if request.method == "POST":
        formularioArtista = ArtistaFormulario(request.POST)
        print(formularioArtista)
        if formularioArtista.is_valid():
            informacion3 = formularioArtista.cleaned_data
            artista = Artista(nombre=informacion3["nombre"], url=informacion3["url"])
            artista.save()
    else:
        formularioArtista = ArtistaFormulario()
    return render(
        request,
        "core/artista.html",
        {"formularioArtista": formularioArtista, "artistas": artistas},
    )


def busquedaCurso(request):
    return render(request, "core/curso_busqueda.html")


def buscar(request):
    if (
        "curso" in request.GET
    ):  # Cambiado a 'curso' ya que es el nombre del campo en el formulario
        titulo = request.GET["curso"]
        cursos = Curso.objects.filter(titulo__icontains=titulo)
        return render(
            request,
            "core/resultado_busqueda.html",
            {"cursos": cursos, "titulo": titulo},
        )
    else:
        respuesta = "No enviaste datos"
        return HttpResponse(respuesta)


def busquedaHistoria(request):
    return render(request, "core/historia_busqueda.html")


def buscar_historia(request):
    if (
        "historia" in request.GET
    ):  # Cambiado a 'curso' ya que es el nombre del campo en el formulario
        titulo = request.GET["historia"]
        historias = Historial.objects.filter(titulo__icontains=titulo)
        return render(
            request,
            "core/resultado_busqueda_historia.html",
            {"historias": historias, "titulo": titulo},
        )
    else:
        respuesta2 = "No enviaste datos"
        return HttpResponse(respuesta2)


def busquedaArtista(request):
    return render(request, "core/artista_busqueda.html")


def buscar_artista(request):
    if (
        "artista" in request.GET
    ):  # Cambiado a 'curso' ya que es el nombre del campo en el formulario
        nombre = request.GET["artista"]
        artistas = Artista.objects.filter(nombre__icontains=nombre)
        return render(
            request,
            "core/artista_resultado.html",
            {"artistas": artistas, "nombre": nombre},
        )
    else:
        respuesta3 = "No enviaste datos"
        return HttpResponse(respuesta3)
    
@login_required
def blogs_view(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            nuevo_blog = form.save(commit=False)
            nuevo_blog.autor = request.user  # Asigna el autor actual
            nuevo_blog.save()
            return redirect('/')# return HttpResponseRedirect('/success/') por ejemplo
    else:
        # Si es una solicitud GET, crea una instancia del formulario vacío
        form = BlogForm()

    return render(request, "core/blogs.html", {'form': form})

def registro_usuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirecciona al usuario a la página de inicio de sesión después del registro
    else:
        form = UserCreationForm()
    return render(request, 'core/registro.html', {'form': form})

def crear_blog(request):
    if request.method == 'POST':
        # Obtener los datos del formulario
        titulo = request.POST.get('titulo')
        descripcion = request.POST.get('descripcion')

        # Obtener el autor actual (usuario logueado)
        autor = request.user

        # Crear una nueva instancia de Blog y asignar el autor
        nuevo_blog = Blog(titulo=titulo, descripcion=descripcion, autor=autor)
        nuevo_blog.save()
        return redirect('blogs.html')  # Redirige a donde desees después de guardar el blog
    else:
        return render(request, 'core/crear_blog.html')
    
    

def editar_perfil_view(request):

    usuario = request.user
    avatar = Avatar.objects.filter(user=usuario).last()
    avatar_url = avatar.imagen.url if avatar is not None else ""


    if request.method == "GET":


        valores_iniciales = {
            "email": usuario.email,
            "first_name": usuario.first_name,
            "last_name": usuario.last_name
        }


        formulario = UserEditionFormulario(initial=valores_iniciales)
        return render(
            request,
            "core/editar_perfil.html",
            context={"form": formulario, "usuario": usuario, "avatar_url": avatar_url}
            )
    else:
        formulario = UserEditionFormulario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data

            usuario.email = informacion["email"]

            usuario.set_password(informacion["password1"])

            usuario.first_name = informacion["first_name"]
            usuario.last_name = informacion["last_name"]
            usuario.save()
        return redirect("/")
    

def crear_avatar_view(request):

    usuario = request.user

    if request.method == "GET":
        formulario = UserAvatarFormulario()
        return render(
            request,
            "core/crear_avatar.html",
            context={"form": formulario, "usuario": usuario}
        )
    else:
        formulario = UserAvatarFormulario(request.POST, request.FILES)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            modelo = Avatar(user=usuario, imagen=informacion["imagen"])
            modelo.save()
            return redirect("/")