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
@api_view(['GET', 'PUT', 'DELETE', 'POST'])
@permission_classes((IsAuthenticated,))
def modificarEliminarAUTO1(request, id):
    try:
        m = Auto.objects.get(idAuto=id)
    except Auto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AUTOSerializers(m)
        return Response(serializer.data)

    elif request.method == 'PUT':
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

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AUTOSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ----------------------Serializers2 ---------------
@api_view(['GET', 'PUT', 'DELETE', 'POST'])
@permission_classes((IsAuthenticated,))
def modificarEliminarAUTO2(request, id):
    try:
        m = Auto.objects.get(idAuto=id)
    except Auto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AUTOSerializers2(m)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data2 = JSONParser().parse(request)
        serializer = AUTOSerializers2(m, data=data2)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        m.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AUTOSerializers2(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ----------------------Serializers3 ---------------


@api_view(['GET', 'PUT', 'DELETE', 'POST'])
@permission_classes((IsAuthenticated,))
def modificarEliminarAUTO3(request, id):
    try:
        m = Auto.objects.get(idAuto=id)
    except Auto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AUTOSerializers3(m)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data2 = JSONParser().parse(request)
        serializer = AUTOSerializers3(m, data=data2)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        m.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AUTOSerializers3(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
