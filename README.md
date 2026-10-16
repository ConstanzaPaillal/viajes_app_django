# Viajes App

API REST desarrollada con Python, Django y Django REST Framework para explorar destinos turísticos, organizar itinerarios, guardar favoritos y gestionar reservas.

## Tecnologías

- Python 3
- Django
- Django REST Framework
- MySQL (WAMP)
- python-decouple (variables de entorno)

## Instalación

1. Clonar el repositorio y entrar a la carpeta del proyecto (donde está `manage.py`).
2. Crear y activar el ambiente virtual:
   - Crear: `python -m venv ambiente`
   - Activar en Windows: `ambiente\Scripts\activate`
   - Activar en Mac/Linux: `source ambiente/bin/activate`
3. Instalar las dependencias: `python -m pip install -r requirements.txt`
4. Crear la base de datos en MySQL ejecutando, en este orden, los scripts de la carpeta `scripts_sql/` (por ejemplo desde la pestaña SQL de phpMyAdmin):
   1. `01_crear_base_datos.sql`
   2. `02_crear_usuario.sql` (cambiar antes la contraseña)
   3. `03_asignar_permisos.sql`
5. Crear el archivo `.env` copiando `.env.example` y completando los valores (clave secreta y datos de conexión a la base de datos).
6. Aplicar las migraciones: `python manage.py migrate`
7. Cargar los datos de ejemplo (el orden importa por las relaciones entre tablas):

   ```
   python manage.py loaddata tipos_destinos.json pais.json region.json provincia.json comuna.json direccion.json destino.json estado_reserva.json usuario.json itinerario.json itinerario_destino.json reserva.json favorito.json
   ```
8. (Opcional) Crear un superusuario para el panel de administración: `python manage.py createsuperuser`
9. Ejecutar el servidor: `python manage.py runserver`

## Rutas principales

| Ruta | Descripción |
|---|---|
| `http://127.0.0.1:8000/` | Página de bienvenida con los destinos |
| `http://127.0.0.1:8000/api/` | Raíz de la API REST |
| `http://127.0.0.1:8000/admin/` | Panel de administración de Django |

## Endpoints de la API

Cada endpoint admite `GET` (listar y ver detalle), `POST`, `PUT`, `PATCH` y `DELETE`.

| Endpoint | Recurso |
|---|---|
| `/api/paises/` | Países |
| `/api/regiones/` | Regiones |
| `/api/provincias/` | Provincias |
| `/api/comunas/` | Comunas |
| `/api/direcciones/` | Direcciones |
| `/api/tipos-destino/` | Tipos de destino |
| `/api/destinos/` | Destinos |
| `/api/usuarios/` | Usuarios |
| `/api/itinerarios/` | Itinerarios |
| `/api/itinerarios-destinos/` | Destinos de cada itinerario |
| `/api/estados-reserva/` | Estados de reserva |
| `/api/reservas/` | Reservas |
| `/api/favoritos/` | Favoritos |

Para ver o modificar un registro puntual se agrega su id, por ejemplo `/api/destinos/1/`.

## Estructura del proyecto

```
viajes_django/
├── manage.py
├── requirements.txt
├── .env.example
├── scripts_sql/          # Scripts para crear la base de datos, el usuario y los permisos
├── viajes_django/        # Configuración del proyecto (settings, urls)
└── viajes_app/
    ├── models.py         # Modelo de datos
    ├── serializers.py    # Serializers de DRF
    ├── views.py          # ModelViewSet y vista de bienvenida
    ├── urls.py           # Router y rutas de la app
    ├── fixtures/         # Datos de ejemplo en JSON
    ├── migrations/
    └── templates/
```