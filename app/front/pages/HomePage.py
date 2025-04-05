# pages/HomePage.py
import customtkinter as ctk

class HomePage:
    def __init__(self, app):
        self.app = app
        self.frame = ctk.CTkFrame(app.root)

        self.frame_title = "Home"
        
        label = ctk.CTkLabel(self.frame, text="Página Principal (Home)", font=ctk.CTkFont(size=24, weight="bold"))
        label.pack(pady=20)
