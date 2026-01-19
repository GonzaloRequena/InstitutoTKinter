"""
Script para compilar a .exe - VERSIÓN COMPLETA

se ejecuta con python build_exe.py

"""

import PyInstaller.__main__     # Importa PyInstaller para usarlo como librería
import shutil                   # Para manejo de carpetas (rmtree para eliminar)
import os                       # Para operaciones con archivos y carpetas

def limpiar(): # PyInstaller crea carpetas build/ (archivos temporales) y dist/ (ejecutables) al compilar. Aqui se eliminan si existen de antes
    """Elimina builds anteriores"""
    print(" Limpiando...")

    for carpeta in ['build', 'dist']:
        if os.path.exists(carpeta):
            try:
                shutil.rmtree(carpeta) # elimina carpeta y todo su contenido
                print(f"  ✓ {carpeta}/ eliminada")
            except:
                pass

def compilar():
    """Compila la aplicación"""
    print("\n Compilando...\n")

    from config.settings import ICON_PATH

    PyInstaller.__main__.run([
        'main.py',                          # Archivo de entrada (punto de partida)
        f'--icon={ICON_PATH}',   # Agregar icono del .exe. SOLO admite .ico
        '--name=APP_MVC_Paquetes_Python',   # Nombre del . exe
        '--onefile',                        # Un solo archivo .exe
        '--windowed',                        # SIN ventana de consola (solo GUI)


        # Agregar recursos (archivos de datos). origen : destino.
        # Los archivos que no son .py no se copian directamente al .exe
        '--add-data=resources;resources',           # Windows usa ; para separar rutas.
        # '--add-data=resources:resources',         # Linux/Mac

        # Modo debug (muestra más información)
        # '--debug=all',

        # No usar UPX (compresión, a veces causa problemas con falsos positivos de antivirus, puede crasear el .exe,
        # incompatible con algunas DDL como pillow, mas lento porque necesita descomprimir en memoria, etc
        '--noupx',#

        # Especificar carpeta de salida, por defecto es dist/
        #'--distpath=ejecutables',

        # Agregar información de versión (Windows). Se accede mediante click derecho en el exe -> propiedades -> detalles
        '--version-file=version_info.txt',

        # Coleccionar TODAS las dependencias
        # callect-all fuerza a que se incluya todos los módulos del paquete
        '--collect-all=customtkinter',      # libreria de ventanas para escritorio
        '--collect-all=PIL',                # libreria de manejo de imagenes para tkinter
        '--collect-submodules=pkg_resources', # para evitar errores en el manejo de archivos. os.path.join puede dar problemas en .exe

        # Copiar metadata
        # Copia Información sobre el paquete: versión, autor, dependencias.
        # Algunos paquetes verifican su propia versión en tiempo de ejecución. Si falta la metadata, pueden dar errores
        '--copy-metadata=customtkinter',
        '--copy-metadata=packaging',
        '--copy-metadata=platformdirs',

        # Hidden imports COMPLETOS
        # Son módulos que se importan de forma dinámica o indirecta
        # PyInstaller no puede detectarlos automáticamente
        '--hidden-import=PIL._tkinter_finder', #módulo específico que --collect-all a veces no detecta correctamente
        '--hidden-import=platformdirs',
        '--hidden-import=jaraco.text', #módulo que llama customtekinter y que collect-all no detecta
        '--hidden-import=importlib_resources',
        '--hidden-import=importlib_metadata',
        '--hidden-import=pkg_resources',

        '--noconfirm', # sobreescribe los archivos sin preguntar
        '--clean', #limpia la cache de pyinstaller antes de compilar
    ])

    print("\n✅ ¡Compilación exitosa!")
    print(" Ejecutable: dist/APP_MVC_Paquetes_Python.exe")


if __name__ == "__main__":
    print("=" * 60)
    print("  COMPILADOR APP MVC")
    print("=" * 60)
    print()

    limpiar()
    compilar()

    print("\n" + "=" * 60)
    print("  ¡LISTO!")
    print("=" * 60)
