-- Crea el usuario que usa Django para conectarse a la base de datos.
-- IMPORTANTE: el nombre y la contraseña deben ser los mismos que se escriben en el archivo .env
CREATE USER IF NOT EXISTS 'Usuario'@'%' IDENTIFIED BY 'mi_contraseña';