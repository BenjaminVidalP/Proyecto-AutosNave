from django.urls import path
from api_rest.views import modificarEliminarAUTO, listado_Auto, agregar_AUTO
from api_rest.viewsLogin import loginApi
urlpatterns = [
     path('modificarEliminarAUTO/<id>', modificarEliminarAUTO,
          name="modificarEliminarAUTO"),
     path('listado_Auto/', listado_Auto, name="listado_Auto"),
     path('agregar_AUTO/', agregar_AUTO, name="agregar_AUTO"),
     path('loginApi/', loginApi, name="loginApi"),
]
