from django.urls import path
from api_rest.views import modificarEliminarAUTO, listado_Auto, agregar_AUTO, modificarEliminarAUTO2, listado_Auto2, agregar_AUTO2, modificarEliminarAUTO3, listado_Auto3, agregar_AUTO3
from api_rest.viewsLogin import loginApi
urlpatterns = [
    path('modificarEliminarAUTO/<id>', modificarEliminarAUTO,
         name="modificarEliminarAUTO"),
    path('listado_Auto/<id>', listado_Auto, name="listado_Auto"),
    path('agregar_AUTO/<id>', agregar_AUTO, name="agregar_AUTO"),
    path('modificarEliminarAUTO2/<id>', modificarEliminarAUTO2,
         name="modificarEliminarAUTO2"),
    path('listado_Auto2/<id>', listado_Auto2, name="listado_Auto2"),
    path('agregar_AUTO2/<id>', agregar_AUTO2, name="agregar_AUTO2"),
    path('modificarEliminarAUTO3/<id>', modificarEliminarAUTO3,
         name="modificarEliminarAUTO3"),
    path('listado_Auto3/<id>', listado_Auto3, name="listado_Auto3"),
    path('agregar_AUTO3/<id>', agregar_AUTO3, name="agregar_AUTO3"),
    path('loginApi/', loginApi, name="loginApi"),
]
