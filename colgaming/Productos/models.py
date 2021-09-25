from django.db import models

# Create your models here.

class TipoJuego(models.Model):
    nombre = models.CharField(max_length=200)
    formato = models.CharField(max_length=200)
    foto = models.ImageField(null =True, blank=True)

    def __str__(self):
        #Identificar un objeto
        return self.nombre
    
    def numProductos(self):
        pass

class VideoJuego(models.Model):
    nombre = models.CharField(max_length=200)
    tipo = models.ForeignKey(TipoJuego, on_delete=models.CASCADE)
    plataforma = models.CharField(max_length=200)
    precio = models.IntegerField()
    descripcion = models.TextField()
    foto = models.ImageField(blank = True, null=True)
    calificacion = models.FloatField(default=0)
    marca = models.CharField(max_length=20, default="")
    ref = models.CharField(max_length=100, default="")

    @property   #=> convierte un método en un atributo
    def tipoJuego(self):
        from Productos.serializers import TipoSerial
        return TipoSerial(self.tipo).data

    def __str__(self):
        return self.nombre
    
    def calcularCalificacion(self):
        pass

class Comentario(models.Model):
    usuario = models.CharField(max_length=200)
    videojuego = models.ForeignKey(VideoJuego, on_delete=models.CASCADE)
    calificacion = models.FloatField()
    fecha = models.DateField(auto_now_add=True) #16/09/2021
    #DateTimeField() 16/09/2021 - 3:13:40 p.m.
    #TimeField()
    contenido = models.TextField()

    def __str__(self):
        return self.usuario + " - " + self.producto.nombre   