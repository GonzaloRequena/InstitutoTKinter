import customtkinter as ctk
from config import *

class MainView(ctk.CTk):

    def __init__(self):
        super().__init__()
        self._crear_interfaz()
        self.geometry(WINDOW_SIZE)
        self.title(f"{APP_NAME} v{APP_VERSION}")
        self.resizable(RESIZEABLE_W, RESIZEABLE_H)
        self.iconbitmap(ICON_PATH)

    def _crear_interfaz(self):
        label = ctk.CTkLabel(
            self,
            text="JORGE",
        )
        label.pack(expand=True)
