from django.db import models

# Create your models here.


# Modelo para auto

class Auto(models.Model):
    idAuto =models.IntegerField(primary_key=True, verbose_name='Id auto')
    nombre =models.CharField(max_length=40, verbose_name=' Nombre auto')
    img=models.ImageField(upload_to='Modelo', blank=True, null=True)
    img1=models.ImageField(upload_to='imagen especificacion1', blank=True , null=True)
    texto1=models.CharField(max_length=40, verbose_name='especificaciones1', null=True)
    img2=models.ImageField(upload_to='imagen especificacion2', blank=True, null=True)
    texto2=models.CharField(max_length=40, verbose_name='especificaciones2', null=True)
    img3=models.ImageField(upload_to='imagen especificacion3', blank=True , null=True)
    texto3=models.CharField(max_length=40, verbose_name='especificaciones3', null=True)
    img4=models.ImageField(upload_to='imagen especificacion4', blank=True , null=True)
    texto4=models.CharField(max_length=40, verbose_name='especificaciones4', null=True)
    precio =models.IntegerField(verbose_name='Precio auto')
    foto =models.ImageField(upload_to='Catalogo', null=True)
    galeria1=models.ImageField(upload_to='Galeria1', blank=True, null=True)
    galeria2=models.ImageField(upload_to='Galeria2', blank=True, null=True)
    galeria3=models.ImageField(upload_to='Galeria3', blank=True, null=True)
    galeria4=models.ImageField(upload_to='Galeria4', blank=True, null=True)
    galeria5=models.ImageField(upload_to='Galeria5', blank=True, null=True)
    galeria6=models.ImageField(upload_to='Galeria6', blank=True, null=True)
    datoA =models.TextField(verbose_name='Descripcion auto 1', null=True)
    datoB =models.TextField(verbose_name='Descripcion auto 2', null=True)
    videoUrl =models.CharField(max_length=280, verbose_name='Url video', null=True)

    def __str__(self):
        return self.nombre


 






