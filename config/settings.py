APP_NAME = "Prueba TKinter"
WINDOW_SIZE = "700x400"
APP_VERSION = "1.0.0"
RESIZEABLE_W = True
RESIZEABLE_H = True

# ruta para Configurar icono de la ventana (se configura en el main)
from resources import resource_path
try:
    ICON_PATH = resource_path("resources/icons/icono_exe.ico")
except Exception as e:
    print(f"Error al cargar icono:  {e}")

##### 3ª version del proyecto
import os
import sys
def get_db_path() -> bytes:
    #Poner la ubicacion de la BD en una carpeta escribible donde se
    # guardan los datos de la aplicacion según el propio sistema.

    if getattr(sys, 'frozen', False):
        # .exe:  Guardar en AppData
        appdata = os.getenv('APPDATA')
        db_dir = os.path.join(appdata, APP_NAME)
    else:
        # Desarrollo
        db_dir = os.path.join(os.path.abspath("."), "database")

    os.makedirs(db_dir, exist_ok=True)
    return os.path.join(db_dir, "usuarios.db")

DB_PATH = get_db_path()

# Debug: Ver dónde está la BD
if __name__ == "__main__":
    print(f"BD en: {DB_PATH}")