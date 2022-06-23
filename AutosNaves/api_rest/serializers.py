from rest_framework import serializers
from core.models import Auto, Marca


class AUTOSerializers(serializers.ModelSerializer):
    class Meta:
        model = Auto
        fields = ['idAuto', 'nombre','precio', 'texto1', 'texto2', 'texto3', 'texto4', 'datoA', 'datoB']


class MarcaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = ['idMarca', 'nombreMarca']
