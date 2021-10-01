from django.db.models import fields
from rest_framework import serializers

#Serializador => objeto Python -> diccionario -> JSON

from Productos.models import *

class TipoSerial (serializers.ModelSerializer):
    class Meta:
        #Metaclase => flexibiliza la forma en cómo se emplean los métodos y atributos de un clase
        model = CategoriaJuego
        fields = '__all__'
        #fields = ['nombre', 'formato",foto"]

class VideoJuegoSerial (serializers.ModelSerializer):
    class Meta:
        #Metaclase => flexibiliza la forma en cómo se emplean los métodos y atributos de un clase
        model = VideoJuego
        #fields = '__all__'
        fields = ['nombre', "foto", "tipo","plataforma", "descripcion", "calcularCalificacion", "marca", "ref"]

class ComentarioSerial(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = '__all__'