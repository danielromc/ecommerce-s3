from django.urls import path, include
from rest_framework.routers import DefaultRouter

from Noticias.views import *

#localhost:8000/productos/api/crud/videojuego

router = DefaultRouter()


#router.register('tipo', TipoAPI)
#router.register('videojuego', VideoJuegoAPI)
#router.register('comentario', ComentarioAPI)

urlpatterns = [
    path('crud/', include(router.urls))
]