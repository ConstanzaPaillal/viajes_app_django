from django.db import models

# Create your models here.

class Pais(models.Model):
    nombre = models.CharField(max_length=50,null=False)
    nacionalidad = models.CharField(max_length=30,null=False)
    iso_2 = models.CharField(max_length=2,null=False)
    iso_3 = models.CharField(max_length=3,null=False)
    habilitado = models.BooleanField(default=True,null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table_comment = "Información de países del mundo, para asociar a destinos y usuarios."

class Region(models.Model):
    codigo = models.CharField(max_length=2,null=False)
    region = models.CharField(max_length=30,null=False)
    habilitado = models.BooleanField(default=True,null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table_comment = "Regiones de Chile, data de SUBDERE."

class Provincia(models.Model):
    codigo = models.CharField(max_length=3,null=False)
    provincia = models.CharField(max_length=50,null=False)
    region = models.ForeignKey(Region,on_delete=models.CASCADE,null=False)
    habilitado = models.BooleanField(default=True,null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table_comment = "Provincias de Chile, data de SUBDERE. Pertenece a una región específica."

class Comuna(models.Model):
    codigo = models.CharField(max_length=5,null=False)
    comuna = models.CharField(max_length=60,null=False)
    provincia = models.ForeignKey(Provincia,on_delete=models.CASCADE,null=False)
    habilitado = models.BooleanField(default=True,null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table_comment = "Comunas de Chile, data de SUBDERE. Pertenece a una provincia específica."

class Direccion(models.Model):
    comuna = models.ForeignKey(Comuna,on_delete=models.CASCADE,null=False)
    calle = models.CharField(max_length=100,null=True)
    numero = models.CharField(max_length=10,null=True)
    departamento = models.CharField(max_length=10,null=True)
    habilitado = models.BooleanField(default=True,null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table_comment = "Direcciones asociadas a destinos o usuarios."

class TipoDestino(models.Model):
    tipo = models.CharField(max_length=30,null=False)
    descripcion = models.CharField(max_length=255,null=True)
    habilitado = models.BooleanField(default=True,null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table_comment = "Categorías de destino turístico (playa, montaña, ciudad, rural)."

class Destino(models.Model):
    nombre = models.CharField(max_length=100,null=False)
    descripcion = models.TextField(null=True)
    tipo_destino = models.ForeignKey(TipoDestino,on_delete=models.CASCADE,null=False)
    pais = models.ForeignKey(Pais,on_delete=models.CASCADE,null=False)
    direccion = models.ForeignKey(Direccion,on_delete=models.CASCADE,null=True)
    precio_referencial = models.DecimalField(max_digits=10,decimal_places=2,null=True)
    habilitado = models.BooleanField(default=True,null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table_comment = "Destinos turísticos disponibles para itinerarios y reservas."

class Usuario(models.Model):
    nombre = models.CharField(max_length=150,null=False)
    rut = models.CharField(max_length=12,null=False)
    correo = models.EmailField(null=True)
    telefono = models.CharField(max_length=15,null=True)
    nacionalidad = models.ForeignKey(Pais,on_delete=models.CASCADE,null=True)
    fecha_nacimiento = models.DateField(null=False)
    contrasenia = models.CharField(max_length=128,null=True)
    direccion = models.ForeignKey(Direccion,on_delete=models.CASCADE,null=True)
    habilitado = models.BooleanField(default=True,null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table_comment = "Registro de usuarios de la aplicación de viajes."

class Itinerario(models.Model):
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE,null=False)
    titulo = models.CharField(max_length=120,null=False)
    fecha_inicio = models.DateField(null=False)
    fecha_fin = models.DateField(null=False)
    habilitado = models.BooleanField(default=True,null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table_comment = "Itinerarios de viaje creados por un usuario."

class ItinerarioDestino(models.Model):
    itinerario = models.ForeignKey(Itinerario,on_delete=models.CASCADE,null=False)
    destino = models.ForeignKey(Destino,on_delete=models.CASCADE,null=False)
    orden = models.PositiveIntegerField(null=False)
    fecha_visita = models.DateField(null=False)
    habilitado = models.BooleanField(default=True,null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table_comment = "Destinos que componen un itinerario, con su orden y fecha de visita."

class EstadoReserva(models.Model):
    estado = models.CharField(max_length=30,null=False)
    descripcion = models.CharField(max_length=255,null=True)
    habilitado = models.BooleanField(default=True,null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table_comment = "Estados posibles de una reserva (pendiente, confirmada, cancelada)."

class Reserva(models.Model):
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE,null=False)
    destino = models.ForeignKey(Destino,on_delete=models.CASCADE,null=False)
    estado = models.ForeignKey(EstadoReserva,on_delete=models.CASCADE,null=False)
    fecha_entrada = models.DateField(null=False)
    fecha_salida = models.DateField(null=False)
    fecha_reserva = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table_comment = "Registro de reservas de destinos realizadas por los usuarios."

class Favorito(models.Model):
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE,null=False)
    destino = models.ForeignKey(Destino,on_delete=models.CASCADE,null=False)
    agregado_en = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table_comment = "Destinos marcados como favoritos por un usuario."