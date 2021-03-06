from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models import Auto, Marca
from .serializers import AUTOSerializers, MarcaSerializers, UserSerializers
from django.contrib.auth.models import User

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


# Create your views here.


@csrf_exempt
@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
# ----------------------Serializers1 ---------------
def listado_Auto(request):
    if request.method == 'GET':
        auto = Auto.objects.all()
        serializer = AUTOSerializers(auto, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AUTOSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


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
        m = Auto.objects.get(idAuto=id)
    except Auto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = AUTOSerializers(m)
        return Response(serializer.data)

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
@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
def listado_Marca(request):
    if request.method == 'GET':
        marca = Marca.objects.all()
        serializer = MarcaSerializers(marca, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MarcaSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def agregar_Marca(request):
    data = JSONParser().parse(request)
    serializer = MarcaSerializers(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((IsAuthenticated,))
def modificarEliminarMarca(request, id):
    try:
        m = Marca.objects.get(idMarca=id)
    except Marca.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = MarcaSerializers(m)
        return Response(serializer.data)

    if request.method == 'PUT':
        data2 = JSONParser().parse(request)
        serializer = MarcaSerializers(m, data=data2)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        m.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ----------------------Serializers3 ---------------
@csrf_exempt
@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated,))
def lista_usuarios(request):
    if request.method == 'GET':
        usuarios = User.objects.all()
        serializer = UserSerializers(usuarios, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializers(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

@api_view(['GET','PUT', 'DELETE'])
@permission_classes((IsAuthenticated,))
def detalle_usuario(request, id):
    try:
        usuarios = User.objects.get(id=id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = UserSerializers(usuarios)
        return Response(serializer.data)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UserSerializers(usuarios, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        usuarios.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)