from django.contrib import admin

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

# Register your models here.

admin.site.register(Pais)
admin.site.register(Region)
admin.site.register(Provincia)
admin.site.register(Comuna)
admin.site.register(Direccion)
admin.site.register(TipoDestino)
admin.site.register(Destino)
admin.site.register(Usuario)
admin.site.register(Itinerario)
admin.site.register(ItinerarioDestino)
admin.site.register(EstadoReserva)
admin.site.register(Reserva)
admin.site.register(Favorito)