from rest_framework import viewsets
from Productos.serializers import *

# Create your views here.

class TipoAPI (viewsets.ModelViewSet):
    serializer_class = TipoSerial
    #queryset => objetos que queremos enviar al frontend
    queryset = CategoriaJuego.objects.all()

class VideoJuegoAPI (viewsets.ModelViewSet):
    serializer_class = VideoJuegoSerial
    #queryset => objetos que queremos enviar al frontend
    queryset = VideoJuego.objects.all()

class ComentarioAPI(viewsets.ModelViewSet):
    serializer_class = ComentarioSerial
    queryset = Comentario.objects.all()