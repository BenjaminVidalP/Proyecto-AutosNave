from rest_framework import serializers
from core.models import Auto, Marca
from django.contrib.auth.models import User


class AUTOSerializers(serializers.ModelSerializer):
    class Meta:
        model = Auto
        fields = ['idAuto', 'nombre','precio', 'texto1', 'texto2', 'texto3', 'texto4', 'datoA', 'datoB']


class MarcaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = ['idMarca', 'nombreMarca']

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
