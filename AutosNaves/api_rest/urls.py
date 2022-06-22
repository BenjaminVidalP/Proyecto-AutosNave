from django.urls import path
from api_rest.views import modificarEliminarAUTO1, modificarEliminarAUTO2, modificarEliminarAUTO3
from api_rest.viewsLogin import loginApi
urlpatterns = [
    path('modificarEliminarAUTO/<id>',modificarEliminarAUTO1,name="modificarEliminarAUTO"),
    path('modificarEliminarAUTO2/<id>',modificarEliminarAUTO2,name="modificarEliminarAUTO2"),
    path('modificarEliminarAUTO3/<id>',modificarEliminarAUTO3,name="modificarEliminarAUTO3"),
    path('loginApi/',loginApi,name="loginApi"),
]