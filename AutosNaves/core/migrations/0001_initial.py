# Generated by Django 4.0.4 on 2022-05-26 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auto',
            fields=[
                ('idAuto', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id auto')),
                ('nombre', models.CharField(max_length=40, verbose_name=' Nombre auto')),
                ('precio', models.IntegerField(verbose_name='Precio auto')),
                ('foto', models.ImageField(upload_to='Catalogo')),
                ('descripcion', models.TextField(verbose_name='Descripcion auto')),
                ('url', models.URLField(verbose_name='Url video')),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idComentario', models.TextField(verbose_name='Comentario')),
                ('fecha', models.DateField()),
                ('baneo', models.BooleanField(verbose_name='Baneo')),
                ('fechaBaneo', models.DateField()),
                ('razonBaneo', models.TextField(verbose_name='Razon baneo')),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreRol', models.CharField(max_length=40, verbose_name='Nombre rol')),
                ('tipoRol', models.CharField(max_length=20, verbose_name='Nombre de rol')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('idUsuario', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id de usuario')),
                ('nombreUsuario', models.CharField(max_length=30, verbose_name='Nombre usuario')),
                ('apellidoUsuario', models.CharField(max_length=40, verbose_name='Apellido usuario')),
                ('correo', models.CharField(max_length=30, verbose_name='Correo')),
                ('clave', models.CharField(max_length=30, verbose_name='Clave')),
                ('fotoPerfil', models.ImageField(upload_to='PerfilUsuario')),
                ('telefono', models.IntegerField()),
            ],
        ),
    ]
