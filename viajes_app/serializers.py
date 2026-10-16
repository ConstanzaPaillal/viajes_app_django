from rest_framework import serializers

from .models import Pais
from .models import Region
from .models import Provincia
from .models import Comuna
from .models import Direccion
from .models import TipoDestino
from .models import Destino
from .models import Usuario
from .models import Itinerario
from .models import ItinerarioDestino
from .models import EstadoReserva
from .models import Reserva
from .models import Favorito


class PaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pais
        fields = ('__all__')

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ('__all__')


class ProvinciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provincia
        fields = ('__all__')

class ComunaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comuna
        fields = ('__all__')

class DireccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direccion
        fields = ('__all__')

class TipoDestinoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDestino
        fields = ('__all__')

class DestinoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destino
        fields = ('__all__')

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('__all__')

class ItinerarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Itinerario
        fields = ('__all__')

class ItinerarioDestinoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItinerarioDestino
        fields = ('__all__')

class EstadoReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoReserva
        fields = ('__all__')

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = ('__all__')

class FavoritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorito
        fields = ('__all__')