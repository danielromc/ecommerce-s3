from django.urls import path, include
from rest_framework.routers import DefaultRouter

from Checkout.views import *

#localhost:8000/productos/api/crud/carrito

router = DefaultRouter()
router.register('carrito', CarritoComprasAPI, basename="carrito")
router.register('articulos', ArticulosAPI, basename="articulos")
router.register('info', InfoEnvioAPI, basename="envio")

urlpatterns = [
    path('crud/', include(router.urls))
]