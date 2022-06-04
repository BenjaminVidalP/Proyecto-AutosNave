from django.contrib import admin
from .models import Rol, Usuario, Auto, Comentario 

# Register your models here.

admin.site.register(Rol)
admin.site.register(Usuario)
admin.site.register(Auto)
admin.site.register(Comentario)

