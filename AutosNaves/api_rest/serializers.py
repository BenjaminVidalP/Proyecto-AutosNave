from enum import auto
from tkinter.tix import AUTO
from rest_framework import serializers
from core.models import Auto

class AUTOSerializers(serializers.ModelSerializer):
    class Meta:
        model = Auto
        fields = ['idAuto','nombre','texto2']

class AUTOSerializers2(serializers.ModelSerializer):
    class Meta:
        model = Auto
        fields = ['idAuto','nombre','texto1','img','texto2']