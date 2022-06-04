from django.db import models

# Create your models here.
class Rol(models.Model):
    nombreRol =models.CharField(max_length=40, verbose_name= 'Nombre rol')
    tipoRol =models.CharField(max_length=20, verbose_name= 'Nombre de rol')

    def __str__(self):
        return self.nombreRol


#Modelo para usuario

class Usuario(models.Model):
    idUsuario =models.IntegerField(primary_key=True, verbose_name='Id de usuario')
    nombreUsuario =models.CharField(max_length=30, verbose_name= 'Nombre usuario')
    apellidoUsuario =models.CharField(max_length=40, verbose_name= 'Apellido usuario')
    correo =models.CharField(max_length=30, verbose_name= 'Correo')
    clave =models.CharField(max_length=30, verbose_name= 'Clave')
    fotoPerfil =models.ImageField(upload_to='PerfilUsuario')
    telefono =models.IntegerField()

    def __str__(self):
        return self.nombreUsuario


# Modelo para auto

class Auto(models.Model):
    idAuto =models.IntegerField(primary_key=True, verbose_name='Id auto')
    nombre =models.CharField(max_length=40, verbose_name=' Nombre auto')
    precio =models.IntegerField(verbose_name='Precio auto')
    foto =models.ImageField(upload_to='Catalogo', null=True)
    descripcion =models.TextField(verbose_name='Descripcion auto')
    url =models.URLField(max_length=200, verbose_name='Url video')

    def __str__(self):
        return self.nombre


 # Modelo para comentario

class Comentario(models.Model):
    idComentario =models.TextField(verbose_name= 'Comentario')
    fecha =models.DateField()
    baneo =models.BooleanField(verbose_name='Baneo')
    fechaBaneo =models.DateField()
    razonBaneo =models.TextField(verbose_name='Razon baneo')
    descripcion =models.TextField()

    def __str__(self):
        return self.fecha






