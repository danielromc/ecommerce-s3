from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from django.shortcuts import get_object_or_404


from Checkout.serializers import *

# Create your views here.

class CarritoComprasAPI(viewsets.ViewSet):
    def list(self, request):
        carritos = CarritoCompras.objects.all()
        serializer = CarritoSerial(carritos, many=True)
        return Response(serializer.data)

    def create(self, request):
        #Crear registros en base de datos
        #nuevoCarrito = CarritoCompras.objects.create(usuario = request.data["usuario"], dcto=request.data["dcto"], cantMinima = request.data["cantMinima"])
        serialCarrito = CarritoSerial(data=request.data)
        if serialCarrito.is_valid():
            serialCarrito.save()
            return Response({"Exito": True})
        return Response(serialCarrito.errors)

    def retrieve(self, request, pk=None):
        #pk => primary key -> es decir: argumento que permite identificar y obtener objetos
        #retrieve => enviar la información de uno o varios objetos
        carritosUsuario = CarritoCompras.objects.filter(usuario=pk)
        carritoS = CarritoSerial(carritosUsuario, many=True)
        return Response(carritoS.data)

class ArticulosAPI(viewsets.ViewSet):
    def list(self, request):
        articulos = Articulo.objects.all()
        serializer = ArticuloSerial(articulos, many=True)
        return Response(serializer.data)

    def create(self, request):
        serialArticulo = ArticuloSerial(data=request.data, many=True)
        if serialArticulo.is_valid():
            serialArticulo.save()
            return Response({'Creados':True})
        return Response(serialArticulo.errors)    

class InfoEnvioAPI(viewsets.ViewSet):
    def create(self, request):
        serializer = ArticuloSerial(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'Creados':True})
        return Response(serializer.errors, HTTP_400_BAD_REQUEST)
    
    def partial_update(self, request, pk=None):
        info = get_object_or_404(InfoEnvio, pk=pk)
        serializer = CarritoSerial(info, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'update':True})
        return Response(serializer.errors, HTTP_400_BAD_REQUEST)