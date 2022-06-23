from django.urls import path
from api_rest.views import modificarEliminarAUTO, listado_Auto, agregar_AUTO, modificarEliminarMarca, listado_Marca, agregar_Marca, lista_usuarios, detalle_usuario
from api_rest.viewsLogin import loginApi


urlpatterns = [
     path('modificarEliminarAUTO/<id>', modificarEliminarAUTO, name="modificarEliminarAUTO"),
     path('listado_Auto/', listado_Auto, name="listado_Auto"),
     path('agregar_AUTO/', agregar_AUTO, name="agregar_AUTO"),
     path('loginApi/', loginApi, name="loginApi"),

     path('modificarEliminarMarca/<id>', modificarEliminarMarca, name="modificarEliminarMarca"),
     path('listado_Marca/', listado_Marca, name="listado_Marca"),
     path('agregar_Marca/<id>', agregar_Marca, name="agregar_Marca"),

     path('lista_usuarios/', lista_usuarios, name="lista_usuarios"),
     path('detalle_usuario/<id>', detalle_usuario, name="detalle_usuario"),
     
]
