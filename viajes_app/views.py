from django.shortcuts import render
from rest_framework import viewsets
from .models import Pais
from .serializers import PaisSerializer
from .models import Region
from .serializers import RegionSerializer
from .models import Provincia
from .serializers import ProvinciaSerializer
from .models import Comuna
from .serializers import ComunaSerializer
from .models import Direccion
from .serializers import DireccionSerializer
from .models import TipoDestino
from .serializers import TipoDestinoSerializer
from .models import Destino
from .serializers import DestinoSerializer
from .models import Usuario
from .serializers import UsuarioSerializer
from .models import Itinerario
from .serializers import ItinerarioSerializer
from .models import ItinerarioDestino
from .serializers import ItinerarioDestinoSerializer
from .models import EstadoReserva
from .serializers import EstadoReservaSerializer
from .models import Reserva
from .serializers import ReservaSerializer
from .models import Favorito
from .serializers import FavoritoSerializer

# Create your views here.
from django.shortcuts import render

def vista(request):
    return render(request, "viajes_core/vista.html")

class PaisViewSet(viewsets.ModelViewSet):
    queryset = Pais.objects.all()
    serializer_class = PaisSerializer

class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

class ProvinciaViewSet(viewsets.ModelViewSet):
    queryset = Provincia.objects.all()
    serializer_class = ProvinciaSerializer

class ComunaViewSet(viewsets.ModelViewSet):
    queryset = Comuna.objects.all()
    serializer_class = ComunaSerializer

class DireccionViewSet(viewsets.ModelViewSet):
    queryset = Direccion.objects.all()
    serializer_class = DireccionSerializer

class TipoDestinoViewSet(viewsets.ModelViewSet):    
    queryset = TipoDestino.objects.all()
    serializer_class = TipoDestinoSerializer

class DestinoViewSet(viewsets.ModelViewSet):
    queryset = Destino.objects.all()
    serializer_class = DestinoSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class ItinerarioViewSet(viewsets.ModelViewSet):
    queryset = Itinerario.objects.all()
    serializer_class = ItinerarioSerializer

class ItinerarioDestinoViewSet(viewsets.ModelViewSet):
    queryset = ItinerarioDestino.objects.all()
    serializer_class = ItinerarioDestinoSerializer

class EstadoReservaViewSet(viewsets.ModelViewSet):
    queryset = EstadoReserva.objects.all()
    serializer_class = EstadoReservaSerializer

class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

class FavoritoViewSet(viewsets.ModelViewSet):
    queryset = Favorito.objects.all()
    serializer_class = FavoritoSerializer