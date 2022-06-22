from rest_framework import serializers
from core.models import Auto


class AUTOSerializers(serializers.ModelSerializer):
    class Meta:
        model = Auto
        fields = ['idAuto', 'nombre','precio', 'texto1', 'texto2', 'texto3', 'texto4', 'datoA', 'datoB']


