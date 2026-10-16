-- Concede privilegios al usuario SOLO sobre la base de datos del proyecto
GRANT ALL PRIVILEGES ON viajes_db.* TO 'Usuario'@'%';

-- Aplica los cambios de privilegios
FLUSH PRIVILEGES;