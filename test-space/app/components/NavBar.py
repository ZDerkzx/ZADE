# components/NavBar.py
import customtkinter as ctk

class NavBar:
    def __init__(self, app, parent, pages):
        """
        app: instancia de la clase App (para poder llamar a show_page)
        parent: widget padre donde se insertará la barra (normalmente la página)
        pages: diccionario de {'Nombre visible': 'clave_interna'}
        """
        self.app = app
        self.frame = ctk.CTkFrame(parent, height=40, fg_color="#f0f0f0")
        self.frame.pack(side="top", fill="x")

        for label, key in pages.items():
            btn = ctk.CTkButton(self.frame, text=label, command=lambda k=key: self.app.show_page(k))
            btn.pack(side="left", padx=5, pady=5)
