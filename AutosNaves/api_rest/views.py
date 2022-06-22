from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models import Auto
from .serializers import AUTOSerializers, AUTOSerializers2, AUTOSerializers3

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


# Create your views here.


@csrf_exempt
# ----------------------Serializers1 ---------------
def listado_Auto(request):
    if request.method == 'GET':
        Auto = Auto.objects.all()
        serializer = AUTOSerializers(Auto, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AUTOSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def agregar_AUTO(request):
    data = JSONParser().parse(request)
    serializer = AUTOSerializers(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((IsAuthenticated,))
def modificarEliminarAUTO(request, id):
    try:
        m = Auto.objects.get(codigoChip=id)
    except Auto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        data2 = JSONParser().parse(request)
        serializer = AUTOSerializers(m, data=data2)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        m.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ----------------------Serializers2 ---------------
def listado_Auto2(request):
    if request.method == 'GET':
        Auto = Auto.objects.all()
        serializer = AUTOSerializers2(Auto, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AUTOSerializers2(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def agregar_AUTO2(request):
    data = JSONParser().parse(request)
    serializer = AUTOSerializers2(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((IsAuthenticated,))
def modificarEliminarAUTO2(request, id):
    try:
        m = Auto.objects.get(idAuto=id)
    except Auto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        data2 = JSONParser().parse(request)
        serializer = AUTOSerializers(m, data=data2)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        m.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ----------------------Serializers3 ---------------


def listado_Auto3(request):
    if request.method == 'GET':
        Auto = Auto.objects.all()
        serializer = AUTOSerializers3(Auto, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AUTOSerializers3(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def agregar_AUTO3(request):
    data = JSONParser().parse(request)
    serializer = AUTOSerializers2(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((IsAuthenticated,))
def modificarEliminarAUTO3(request, id):
    try:
        m = Auto.objects.get(idAuto=id)
    except Auto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        data2 = JSONParser().parse(request)
        serializer = AUTOSerializers(m, data=data2)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        m.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
