from django.urls import path
from api_rest.views import agregar_AUTO, listado_AUTO,modificarEliminarAUTO
from api_rest.viewsLogin import loginApi
urlpatterns = [
    path('listado_AUTO/',listado_AUTO,name="listado_AUTO"),
    path('agregar_AUTO/',agregar_AUTO,name="agregar_AUTO"),
    path('modificarEliminarAUTO/<id>',modificarEliminarAUTO,name="modificarEliminarAUTO"),
    path('loginApi/',loginApi,name="loginApi"),
]