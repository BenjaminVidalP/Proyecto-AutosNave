# Generated by Django 4.0.4 on 2022-06-23 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_auto_videourl'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('idMarca', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id Marca')),
                ('nombreMarca', models.CharField(max_length=40, verbose_name=' Nombre Marca')),
            ],
        ),
    ]
