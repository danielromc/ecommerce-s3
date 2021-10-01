from django.db import models

# Create your models here.


from Productos.models import Consola
class Lanzamientos(models.Model):

    nombre= models.CharField(max_length=200)
    descripcion=models.TextField()
    plataforma= models.ForeignKey(Consola, on_delete=models.CASCADE)


    def __str__(self):
        return self.nombre