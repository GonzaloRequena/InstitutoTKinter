"""
Vista principal con tabla de usuarios
"""
import customtkinter as ctk
from tkinter import ttk, messagebox
from config.settings import APP_NAME, APP_VERSION, WINDOW_SIZE, RESIZEABLE_W, RESIZEABLE_H, ICON_PATH
from src.control.user_controller import UserController
from src.views.edit_view import EditView


class MainView(ctk.CTk):

    def __init__(self):
        super().__init__()
        self.controller = UserController() #instancia del controlador de usuario
        self._configurar_ventana() #configura la ventana principal com tamaño, titulo, icono, etc
        self._crear_interfaz() #crea la interfaz de usuario, botones, label, etc
        self._cargar_usuarios() #carga los usuarios en la tabla - arbol al iniciar la aplicacion

    def _configurar_ventana(self):
        """Configura la ventana principal"""
        self.title(f"{APP_NAME} v{APP_VERSION}")
        self.geometry(WINDOW_SIZE)
        self.resizable(RESIZEABLE_W, RESIZEABLE_H)
        self.iconbitmap(ICON_PATH)
    def _crear_interfaz(self):
        # label = ctk.CTkLabel(
        #     self,
        #     text="JORGE",
        # )
        # label.pack(expand=True)

        titulo = ctk.CTkLabel(
            self,
            text="GESTIÓN DE USUARIOS",
            font=("Arial", 24, "bold")
        )
        titulo.pack(pady=20)

        ########################## FORMULARIO (FRAME)
        frame_form = ctk.CTkFrame(self)
        frame_form.pack(pady=10, padx=20, fill="x")

        # Campos del formulario
        ctk.CTkLabel(frame_form, text="Nombre:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.entry_nombre = ctk.CTkEntry(frame_form, width=150)
        self.entry_nombre.grid(row=0, column=1, padx=5, pady=5)

        ctk.CTkLabel(frame_form, text="Apellidos:").grid(row=0, column=2, padx=5, pady=5, sticky="e")
        self.entry_apellidos = ctk.CTkEntry(frame_form, width=150)
        self.entry_apellidos.grid(row=0, column=3, padx=5, pady=5)

        ctk.CTkLabel(frame_form, text="Nick:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.entry_nick = ctk.CTkEntry(frame_form, width=150)
        self.entry_nick.grid(row=1, column=1, padx=5, pady=5)

        ctk.CTkLabel(frame_form, text="Password:").grid(row=1, column=2, padx=5, pady=5, sticky="e")
        self.entry_password = ctk.CTkEntry(frame_form, width=150, show="*")
        self.entry_password.grid(row=1, column=3, padx=5, pady=5)

        ########################## BOTONES (FRAME)
        frame_botones = ctk.CTkFrame(self)
        frame_botones.pack(pady=10)

        ctk.CTkButton(
            frame_botones,
            text="Agregar Usuario",
            command=self._agregar_usuario,
            width=150
        ).pack(side="left", padx=5)

        ctk.CTkButton(
            frame_botones,
            text="Eliminar Seleccionado",
            command=self._eliminar_usuario,
            width=150,
            fg_color="red"
        ).pack(side="left", padx=5)

        ctk.CTkButton(
            frame_botones,
            text="Actualizar Lista",
            command=self._cargar_usuarios,
            width=150
        ).pack(side="left", padx=5)

        ctk.CTkButton(
            frame_botones,
            text="Editar Usuario ventana",
            command=self._editar_usuario,
            width=150).pack(side="left", padx=5)

        ########################## TABLA de usuarios (Treeview)
        frame_tabla = ctk.CTkFrame(self)
        frame_tabla.pack(pady=10, padx=20, fill="both", expand=True)

        # Scrollbar
        scrollbar = ttk.Scrollbar(frame_tabla)  # crea el scrollbar asociado al frame
        scrollbar.pack(side="right", fill="y")  # lo posiciona a la derecha y lo hace vertical

        # Treeview
        self.tabla = ttk.Treeview(
            frame_tabla,
            columns=("Nombre", "Apellidos", "Nick"),
            # columnas que tendra la tabla. Se configuran despues pero hay que crearlas aqui
            show="headings",  # oculta la columna vacia de la izquierda
            yscrollcommand=scrollbar.set  # Asociar scrollbar. si muevo la tabla se mueve la barra
        )

        scrollbar.config(
            command=self.tabla.yview)  # Asociar scrollbar. método yview. Cuando mueva la barra, se mueve la tabla

        # Configurar columnas
        # self.tabla.heading("ID", text="ID")
        self.tabla.heading("Nombre", text="Nombre")
        self.tabla.heading("Apellidos", text="Apellidos")
        self.tabla.heading("Nick", text="Nick")

        # self.tabla.column("ID", width=50, anchor="center")
        self.tabla.column("Nombre", width=150)
        self.tabla.column("Apellidos", width=200)
        self.tabla.column("Nick", width=150)

        # Doble clic para editar
        self.tabla.bind("<Double-1>", lambda e: self._editar_usuario())

        self.tabla.pack(fill="both", expand=True)

    def _cargar_usuarios(self):
        """Carga todos los usuarios de la BD en la tabla"""
        # Limpiar tabla
        for item in self.tabla.get_children():
            self.tabla.delete(item)

        # Obtener usuarios del controlador
        usuarios = self.controller.listar_usuarios()

        # Insertar en tabla
        for usuario in usuarios:
            id_usuario, nombre, apellidos, nick = usuario
            self.tabla.insert("", "end", iid=id_usuario,
                              values=(nombre, apellidos, nick))  # el id_usuario lo oculta en iid

    def _agregar_usuario(self):
        """Agrega un nuevo usuario"""
        nombre = self.entry_nombre.get().strip()
        apellidos = self.entry_apellidos.get().strip()
        nick = self.entry_nick.get().strip()
        password = self.entry_password.get().strip()

        exito, mensaje, id_usuario_nuevo = self.controller.agregar_usuario(nombre, apellidos, nick, password)

        if exito:
            messagebox.showinfo("Éxito", mensaje)
            self.tabla.insert("", "end", iid=id_usuario_nuevo, values=(nombre, apellidos, nick))
            self._limpiar_formulario()
        else:
            messagebox.showerror("Error", mensaje)

    def _eliminar_usuario(self):
        """Elimina el usuario seleccionado"""
        seleccion = self.tabla.selection()

        if not seleccion:
            messagebox.showwarning("Advertencia", "Selecciona un usuario")
            return

        for id_usuario in seleccion:  # recorro los ids seleccionados. tabla.selection devuelve una lista con los iid.
            # Obtener ID del usuario seleccionado
            # id_usuario = seleccion[0] # si solo quiero eliminar de 1 en 1. Asi cogeria el primero de los seleccionados.

            nombre, apellidos, nick = self.tabla.item(id_usuario)["values"]  # obtengo los valores de la tabla.

            # Confirmar
            confirmar = messagebox.askyesno(
                "Confirmar",
                f"¿Eliminar usuario: {nombre} - {apellidos} - {nick}?"
            )

            if confirmar:
                self.controller.eliminar_usuario(id_usuario)
                messagebox.showinfo("Éxito", "Usuario eliminado")
                self._cargar_usuarios()

    def _limpiar_formulario(self):
        """Limpia los campos del formulario"""
        self.entry_nombre.delete(0, 'end')
        self.entry_apellidos.delete(0, 'end')
        self.entry_nick.delete(0, 'end')
        self.entry_password.delete(0, 'end')

    def _editar_usuario(self):
        """Edita el usuario seleccionado"""
        seleccion = self.tabla.selection()

        if not seleccion:
            messagebox.showwarning("Advertencia", "Selecciona un usuario")
            return

        # self.controller.editar_usuario(self.tabla.item)

        # Obtener ID del usuario seleccionado
        item = seleccion[0]

        # Ventana emergente para ver los datos y editar de un usuario.
        # Lo unico que pasamos de informacion es la pantalla master y el id_usuario, ya en la ventana se cogen desde BD para no pasarselos desde la vista.
        editar_ventana = EditView(self, self.controller, self._cargar_usuarios, item)

    def _editar_usuario(self):
        pass
