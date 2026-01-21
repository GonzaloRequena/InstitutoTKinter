from tkinter import messagebox

import customtkinter as ctk
from src.control import user_controller

class EditView(ctk.CTkToplevel):

    def __init__(self, master, controller, cargar_usuarios, item):
        # recibe la ventana master (mainview), el controlador, la función para recargar usuarios y el id del usuario a editar
        # valdria con master y desde ahi se podrian usar el controlador y el cargar usuarios. Pero asi es más desacoplado y
        # respeta algo mas la encapsulación. Solo se usa master para indicar la vetana principal.
        # los demas metodos estan controlados a los que se accede.
        # controler se usa el del master para que sea la misma instancia y por lo tanto sea exactamente igual. evita conflictos.

        super().__init__(master)
        self.title("Editar Usuario")
        self.controller = controller
        self.cargar_usuarios = cargar_usuarios #se usa porque hay que recargar la tabla en la ventana principal.
        #self.guardar_cambios_callback = None


        id_usuario, nombre, apellidos, nick = self.controller.carga_usuario(item)


        ######FRAME INFORMACION USUARIO
        f_informacion = ctk.CTkFrame(self)
        f_informacion.pack(pady = 10)

        ctk.CTkLabel(
            f_informacion,
            text = "Editando el Usuario",
            font = ctk.CTkFont(size = 16, weight = "bold")
        ).pack(pady = 10)

        self.entry_nombre = ctk.CTkEntry(
            f_informacion,
            width = 300
        )
        self.entry_nombre.pack(pady = 5)
        self.entry_nombre.insert(0, nombre) #0 indica al principio del campo de texto.

        self.entry_apellidos = ctk.CTkEntry(
            f_informacion,
            width = 300
        )
        self.entry_apellidos.pack(pady = 5)
        self.entry_apellidos.insert(0, apellidos)

        self.entry_nick = ctk.CTkEntry(
            f_informacion,
            width = 300
        )
        self.entry_nick.pack(pady = 5)
        self.entry_nick.insert(0, nick)


        self.entry_password = ctk.CTkEntry(
            f_informacion,
            width=150,
            show="*")
        self.entry_password.pack(pady = 5)


        ######BOTONERA
        f_botonera = ctk.CTkFrame(self)
        f_botonera.pack(pady = 10)

        ctk.CTkButton(
            f_botonera,
            text = "Guardar Cambios",
            command = lambda: self._guardar_cambios(item)
        ).pack(pady = 10, side = ctk.LEFT, padx = 10 )

        ctk.CTkButton(
            f_botonera,
            text = "Cerrar Ventana",
            command = self.destroy
        ).pack(pady = 10, side = ctk.LEFT, padx = 10 )


    def _guardar_cambios(self, item):
        nombre = self.entry_nombre.get().strip()
        apellidos = self.entry_apellidos.get().strip()
        nick = self.entry_nick.get().strip()
        password = self.entry_password.get().strip()

            # Validar campos vacíos
        if not nombre or not apellidos or not nick or not password:
            messagebox.showerror("Error", "Nombre, apellidos, nick y password son obligatorios")
            return

        self.controller.edita_usuario( item, nombre, apellidos, nick, password)
        self.cargar_usuarios()