from unicodedata import name
from django.contrib import admin
from django.urls import path
from .views import  GestionAutos, registrarAutos, eliminarAuto, editarAuto,edicionAuto, home, CHEVROLET, FORD, HYUNDAI, JEEP, mapa, Marcas, Auto, admin, Autos, Camionetas,InicioSesion, RegistroSesion, PerfilUsuario, AtencionCliente, EditarPerfil, Catalogo


urlpatterns = [
    path('registrarAutos/',registrarAutos, name="registrarAutos" ),
    path('eliminarAuto/<idAuto>', eliminarAuto ),
    path('editarAuto/<idAuto>', editarAuto ),
    path('edicionAuto/', edicionAuto, name="edicionAuto"),
    path('GestionAutos/' , GestionAutos, name="Gestion"),
    path('', home,name="home"),
    path('CHEVROLET/', CHEVROLET,name="CHEVROLET"),
    path('FORD/', FORD,name="FORD"),
    path('HYUNDAI/', HYUNDAI,name="HYUNDAI"),
    path('JEEP/', JEEP,name="JEEP"),
    path('mapa/', mapa,name="mapa"),
    path('Marcas/', Marcas,name="Marcas"),
    path('Auto/', Auto, name="Auto"),
    path('Administrador/', admin, name="administrador"),
    path('Autos/', Autos, name="Autos"),
    path('Camionetas/', Camionetas, name="Camionetas"),
    path('InicioSesion/' ,InicioSesion, name="InicioSesion"),
    path('RegistroSesion/',RegistroSesion, name="RegistroSesion"),
    path('PerfilUsuario/', PerfilUsuario, name="PerfilUsuario"),
    path('AtencionCliente/', AtencionCliente, name="AtencionCliente"),
    path('EditarPerfil/', EditarPerfil, name="EditarPerfil"),
    path('Catalogo/', Catalogo, name= "Catalogo"),

]