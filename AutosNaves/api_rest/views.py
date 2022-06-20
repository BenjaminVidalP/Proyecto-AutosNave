from django.shortcuts import render
from rest_framework import viewsets
from api_rest.serializers import AUTOSerializers, AUTOSerializers2 
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from enum import auto
from urllib import response

# Create your views here.

#----------------------Serializers ---------------
@csrf_exempt
@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
def listado_AUTO(request):
    if request.method == 'GET':
        Auto = auto.objects.all()
        serializer = AUTOSerializers(auto,many=True)
        return response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AUTOSerializers(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def agregar_AUTO(request):
    data = JSONParser().parse(request)
    serializer = AUTOSerializers2(data = data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status = status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
@permission_classes((IsAuthenticated,))
def modificarEliminarAUTO(request, id):
    try:
        m = auto.objects.get(idAuto = id)
    except auto.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = AUTOSerializers2(m)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        data2 = JSONParser().parse(request)
        serializer = AUTOSerializers2(m, data = data2)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "DELETE":
        m.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)