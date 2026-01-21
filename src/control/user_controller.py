"""
Controlador de Usuario - Intermediario entre Vista y Modelo
"""
from src.model.user_model import UserModel
from utils import validar_contrasena

class UserController:
    def __init__(self):
        self.model = UserModel()

    def listar_usuarios(self):
        """Obtiene lista de usuarios"""
        return self.model.obtener_todos()

    def agregar_usuario(self, nombre, apellidos, nick, password) -> str:
        """Agrega un nuevo usuario"""
        id_usuario_nuevo = -1
        if not nombre or not apellidos or not nick or not password:
            return False, "Todos los campos son obligatorios", id_usuario_nuevo

        valido, mensaje = validar_contrasena(password)
        if not valido:
            return valido, mensaje, id_usuario_nuevo

        exito, id_usuario_nuevo = self.model.crear(nombre, apellidos, nick, password)

        if exito:
            return True, "Usuario creado exitosamente", id_usuario_nuevo
        else:
            return False, "El nick ya existe", id_usuario_nuevo
