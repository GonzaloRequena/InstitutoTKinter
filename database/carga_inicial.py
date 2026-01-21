"""
Script para cargar datos iniciales en la base de datos
"""
from src.model.user_model import UserModel

def cargar_datos_iniciales(model : UserModel):
    """Carga 5 usuarios de ejemplo"""

    usuarios = [
        ("Juan", "García López", "juangl", "1234"),
        ("María", "Rodríguez Pérez", "mariarp", "pass123"),
        ("Carlos", "Martínez Sánchez", "carlosm", "carlos2024"),
        ("Ana", "López Fernández", "analf", "ana456"),
        ("Pedro", "Sánchez Gómez", "pedrosg", "pedro789"),
    ]

    print("Cargando usuarios iniciales...")

    for nombre, apellidos, nick, password in usuarios:
        exito = model.crear(nombre, apellidos, nick, password)
        if exito:
            print(f"✓ Usuario '{nick}' creado")
        else:
            print(f"✗ Usuario '{nick}' ya existe")

    print("\n¡Carga completada!")
    print(f"Total usuarios:  {len(model.obtener_todos())}")