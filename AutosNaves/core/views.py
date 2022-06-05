from django.shortcuts import render, redirect
from .models import Auto
from django.contrib import messages

# Create your views here.


def GestionAutos(request):
    autosListado = Auto.objects.all()
    messages.success(request, '¡Autos Actualizados!')
    return render(request, "core/GestionAutos.html", {"autos":autosListado})

def registrarAutos(request):
    idAuto=request.POST['idAuto']
    nombre=request.POST['nombre']
    precio=request.POST['precio']
    f=request.FILES['file']
    auto=Auto.objects.create(idAuto=idAuto, nombre=nombre, precio=precio,foto=f)
    messages.success(request, '¡Auto Registrado!')
    return redirect('GestionAutos/')

def editarAuto(request, idAuto):
    auto = Auto.objects.get(idAuto=idAuto)
    return render(request, "core/editarAuto.html", {"auto":auto})

def edicionAuto(request):
    idAuto=request.POST['idAuto']
    nombre=request.POST['nombre']
    precio=request.POST['precio']
    auto = Auto.objects.get(idAuto=idAuto)
    if(request.FILES.get("file")):
        foto = request.FILES["file"]
        auto.foto = foto

    
    auto.nombre = nombre
    auto.precio = precio
    auto.save()

    messages.success(request, '¡Auto Actualizado!')
    return redirect('GestionAutos/')

def eliminarAuto(request, idAuto):
    auto = Auto.objects.get(idAuto=idAuto)
    auto.delete()
    messages.success(request, '¡Auto Eliminado!')
    return redirect('/')


def home(request):

    return render(request, 'core/pagina-home.html')

#---------------------INICIO/REGISTRO/PerfilUsuario-----------------

def InicioSesion(request):

    return render(request, 'core/InicioSesion.html')

def RegistroSesion(request):

    return render(request, 'core/RegistroSesion.html')

def PerfilUsuario(request):

    return render(request, 'core/PerfilUsuario.html')

def Catalogo(request):
     return render(request, 'core/Catalogo.html' )

#-----------------------MARCAS-------------------------

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

#-----------------------PLANTILLAS------------------------

def camaro(request):
    contexto = {"nombreA":"Camaro", "img":"/static/core/img/ChevroletCamaro/Baner-camaro.jpg"
                ,"img1":"/static/core/img/ChevroletCamaro/motor-camaro.png","texto1":"6.2"
                ,"img2":"/static/core/img/ChevroletCamaro/caja-camaro.png","texto2":"CAJA AUTO"
                ,"img3":"/static/core/img/ChevroletCamaro/velocimetro-camaro.png","texto3":"0 A 100 KM/H"
                ,"img4":"/static/core/img/ChevroletCamaro/certificacion-camaro.png","texto4":"Servicio"
                ,"galeriaimg1":"/static/core/img/ChevroletCamaro/galeria1.jpg"
                ,"galeriaimg2":"/static/core/img/ChevroletCamaro/galeria2.jpg"
                ,"galeriaimg3":"/static/core/img/ChevroletCamaro/galeria3.jpg"
                ,"galeriaimg4":"/static/core/img/ChevroletCamaro/galeria4.jpg"
                ,"galeriaimg5":"/static/core/img/ChevroletCamaro/galeria5.jpg"
                ,"galeriaimg6":"/static/core/img/ChevroletCamaro/galeria6.jpg"
                ,"nombreG":"Galeria de Imagenes"
                ,"datosA":"Un facelift al performance." 
                ,"datosB":"El nuevo Camaro fue rediseñado de principio a fin. Su línea ha evolucionado para verse aún mas estilizada, pero eso no es todo, incluye tecnología, performance y un manejo superior. Aceléralo hasta el fondo y descubre lo que significa la adrenalina."
                ,"videoA":"https://www.youtube.com/embed/0ZzMcwdb2W0"}
    return render(request,'core/ChevroletCamaro.html',contexto)


#-------------------------mapa-api------------------------

def mapa(request):

    return render(request, 'core/mapa.html')


#----------------------AUTOS Y CAMIONETAS ---------------

#--Chevrolet--


def onix(request):

    return render(request, 'core/ChevroletOnixSedan.html')

def sail(request):

    return render(request, 'core/ChevroletSail.html')

#--Ford--

def territory(request):

    return render(request, 'core/FordAllNewTerritory.html')

def focus(request):

    return render(request, 'core/FordFocus.html')

def raptor(request):

    return render(request, 'core/FordRaptor.html')

#--Hyundai--

def accent(request):

    return render(request, 'core/HyundaiAccent.html')

def tucson(request):

    return render(request, 'core/HyundaiTucson.html')

def veloster(request):

    return render(request, 'core/HyundaiVeloster.html')

#--Jeep--

def cherokee(request):

    return render(request, 'core/JeepCherokee.html')

def gladiator(request):

    return render(request, 'core/JeepGladiator.html')

def wrangler(request):

    return render(request, 'core/JeepWrangler.html')

# Administrador

def admin(request):
    return render(request, 'core/Administrador.html')

# Agregar Autos

def AgregarAutos(request):
    return render(request, 'core/AgregarAutos.html')

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