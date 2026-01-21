"""
Consultas SQL de la aplicación (Crear tabla y CRUD de usuarios
"""

# Crear tabla
CREATE_TABLE_USUARIOS = '''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        apellidos TEXT NOT NULL,
        nick TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
'''

# Selects
SELECT_ALL_USUARIOS = 'SELECT id, nombre, apellidos, nick FROM usuarios'
SELECT_USUARIO_BY_ID = 'SELECT id, nombre, apellidos, nick FROM usuarios WHERE id = ?'

# Inserts
INSERT_USUARIO = '''
    INSERT INTO usuarios (nombre, apellidos, nick, password)
    VALUES (?, ?, ?, ?)
'''

# Deletes
DELETE_USUARIO = 'DELETE FROM usuarios WHERE id = ? '

# Updates
UPDATE_USUARIO = '''
    UPDATE usuarios 
    SET nombre = ?, apellidos = ?, nick = ?, password = ?
    WHERE id = ?
'''