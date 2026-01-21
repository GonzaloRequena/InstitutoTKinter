
def validar_contrasena(password:str) -> bool:
    """Valida la contraseña"""
    valido = False
    if not password:
        mensaje = "La contraseña no puede estar vacía"
    elif len(password) < 4:
        mensaje = "La contraseña tiene que tener al menos 4 caracteres"
    else:
        valido = True
        mensaje = "Contraseña válida"

    return valido, mensaje
