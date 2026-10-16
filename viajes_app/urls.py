from django.urls import path, include
from . import views
from rest_framework import routers
from viajes_app import views


router = routers.DefaultRouter() 

router.register(r'paises', views.PaisViewSet)
router.register(r'regiones', views.RegionViewSet)
router.register(r'provincias', views.ProvinciaViewSet)
router.register(r'comunas', views.ComunaViewSet)
router.register(r'direcciones', views.DireccionViewSet)
router.register(r'tipos-destino', views.TipoDestinoViewSet)
router.register(r'destinos', views.DestinoViewSet)
router.register(r'usuarios', views.UsuarioViewSet)
router.register(r'itinerarios', views.ItinerarioViewSet)
router.register(r'itinerarios-destinos', views.ItinerarioDestinoViewSet)
router.register(r'estados-reserva', views.EstadoReservaViewSet)
router.register(r'reservas', views.ReservaViewSet)
router.register(r'favoritos', views.FavoritoViewSet)

urlpatterns = [
    path('', views.vista, name='bienvenida'),
    path('api/', include(router.urls)),
]