from django.shortcuts import render, redirect
from .models import Blog, Curso, Historial, Artista
from .forms import ArteFormulario, HistoriaFormulario, ArtistaFormulario, BlogForm
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


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
        return redirect('ruta_de_redireccion')  # Redirige a donde desees después de guardar el blog
    else:
        return render(request, 'core/crear_blog.html')