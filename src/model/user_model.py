"""
Modelo de Usuario
"""
import sqlite3
from config.settings import DB_PATH
from database.queries import (
    CREATE_TABLE_USUARIOS,
    SELECT_ALL_USUARIOS,
    INSERT_USUARIO,
    DELETE_USUARIO,
    SELECT_USUARIO_BY_ID,
    UPDATE_USUARIO
)
import os

class UserModel:
    def __init__(self):
        self._crear_bd_si_no_existe()

    def _crear_bd_si_no_existe(self) -> bool:
        """Crea la BD y tabla si no existen"""
        from database.carga_inicial import cargar_datos_iniciales
        os.makedirs(os.path.dirname(DB_PATH), exist_ok=True) #Crea la carpeta database si no existe. exist_ok=True → No da error si ya existe
        bd_nueva = not os.path.exists(DB_PATH)
        print(f"Comprobando/Creando BD en: {DB_PATH}")

        with sqlite3.connect(DB_PATH) as conn: #Crea la BD si no existe
            cursor = conn. cursor()
            cursor.execute(CREATE_TABLE_USUARIOS)
            conn.commit()

        #return bd_nueva

        if bd_nueva:
            print("BD creada. Cargando datos iniciales...")
            cargar_datos_iniciales(self)


    def obtener_todos(self) -> list:
        """Obtiene todos los usuarios"""
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute(SELECT_ALL_USUARIOS)
            usuarios = cursor.fetchall()
            return usuarios

    def crear(self, nombre, apellidos, nick, password) -> bool:
        """Crea un nuevo usuario"""
        try:
            with sqlite3.connect(DB_PATH) as conn:
                cursor = conn.cursor()
                cursor.execute(INSERT_USUARIO, (nombre, apellidos, nick, password))
                id_usuario_nuevo = cursor.lastrowid
                conn.commit()
                return True, id_usuario_nuevo
        except sqlite3.IntegrityError:
            return False, -1  # Nick ya existe