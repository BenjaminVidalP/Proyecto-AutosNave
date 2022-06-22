from django.shortcuts import render, redirect
from .models import Auto
from django.contrib import messages
from .forms import UserRegisterForm
from . import views
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.


def login(request):

    return render(request, 'core/login.html')


def registro(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado')
            return redirect('login')
    else:
        form = UserRegisterForm()

    contexto = {'form': form}
    return render(request, 'core/registro.html', contexto)


def logout(request):

    return render(request, 'core/logout.html')


@permission_required('app.add_producto')
def GestionAutos(request):
    autosListado = Auto.objects.all()
    messages.success(request, '¡Autos Actualizados!')
    return render(request, "core/GestionAutos.html", {"autos": autosListado})


@permission_required('app.add_producto')
def registrarAutos(request):
    idAuto = request.POST['idAuto']
    nombre = request.POST['nombre']
    img = request.FILES['banner']
    img1 = request.FILES['img1']
    texto1 = request.POST['text1']
    img2 = request.FILES['img2']
    texto2 = request.POST['text2']
    img3 = request.FILES['img3']
    texto3 = request.POST['text3']
    img4 = request.FILES['img4']
    texto4 = request.POST['text4']
    precio = request.POST['precio']
    foto = request.FILES['foto']
    galeria1 = request.FILES['galeria1']
    galeria2 = request.FILES['galeria2']
    galeria3 = request.FILES['galeria3']
    galeria4 = request.FILES['galeria4']
    galeria5 = request.FILES['galeria5']
    galeria6 = request.FILES['galeria6']
    datoA = request.POST['datoA']
    datoB = request.POST['datoB']
    videoUrl = request.POST['video']

    auto = Auto.objects.create(idAuto=idAuto, nombre=nombre, img=img, img1=img1, texto1=texto1, img2=img2, texto2=texto2, img3=img3, texto3=texto3, img4=img4, texto4=texto4, precio=precio,
                               foto=foto, galeria1=galeria1, galeria2=galeria2, galeria3=galeria3, galeria4=galeria4, galeria5=galeria5, galeria6=galeria6, datoA=datoA, datoB=datoB, videoUrl=videoUrl)
    messages.success(request, '¡Auto Registrado!')
    return redirect('GestionAutos')


@permission_required('app.add_producto')
def editarAuto(request, idAuto):
    auto = Auto.objects.get(idAuto=idAuto)
    return render(request, "core/editarAuto.html", {"auto": auto})


def productos(request, idAuto):
    auto = Auto.objects.get(idAuto=idAuto)
    return render(request, "core/productos.html", {"auto": auto})


@permission_required('app.add_producto')
def edicionAuto(request):
    idAuto = request.POST['idAuto']
    nombre = request.POST['nombre']
    precio = request.POST['precio']
    auto = Auto.objects.get(idAuto=idAuto)
    if(request.FILES.get("file")):
        foto = request.FILES["file"]
        auto.foto = foto

    auto.nombre = nombre
    auto.precio = precio
    auto.save()

    messages.success(request, '¡Auto Actualizado!')
    return redirect('GestionAutos')


@permission_required('app.add_producto')
def eliminarAuto(request, idAuto):
    auto = Auto.objects.get(idAuto=idAuto)
    auto.delete()
    messages.success(request, '¡Auto Eliminado!')
    return redirect('GestionAutos')


def home(request):

    return render(request, 'core/pagina-home.html')

# ---------------------INICIO/REGISTRO/PerfilUsuario-----------------


def PerfilUsuario(request):

    return render(request, 'core/PerfilUsuario.html')


def Catalogo(request):
    autos = Auto.objects.all()
    return render(request, 'core/Catalogo.html', {"veiculo": autos})

# -----------------------MARCAS-------------------------


def Marcas(request):

    return render(request, 'core/Marcas.html')


def CHEVROLET(request):

    return render(request, 'core/CHEVROLET.html')


def FORD(request):

    return render(request, 'core/FORD.html')


def HYUNDAI(request):

    return render(request, 'core/HYUNDAI.html')


def JEEP(request):

    return render(request, 'core/JEEP.html')

# -----------------------PLANTILLAS------------------------


# -------------------------mapa-api------------------------

def mapa(request):

    return render(request, 'core/mapa.html')


# ----------------------AUTOS Y CAMIONETAS ---------------

# Administrador

def admin(request):
    return render(request, 'core/Administrador.html')

# Seccion Autos


def Autos(request):
    return render(request, 'core/Autos.html')

# Seccion Camionetas


def Camionetas(request):
    return render(request, 'core/Camionetas.html')


def AtencionCliente(request):
    return render(request, 'core/AtencionCliente.html')


def EditarPerfil(request):
    return render(request, 'core/EditarPerfil.html')


def AutosNuevos(request):
    return render(request, 'core/AutosNuevos.html')


def AutosSemiNuevos(request):
    return render(request, 'core/AutosSemiNuevos.html')
