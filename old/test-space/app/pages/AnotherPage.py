# pages/HomePage.py
import customtkinter as ctk

class AnotherPage:
    def __init__(self, app):
        self.app = app
        self.frame = ctk.CTkFrame(app.root)

        self.frame_title = "Other"
        
        label = ctk.CTkLabel(self.frame, text="la otra page", font=ctk.CTkFont(size=24, weight="bold"))
        label.pack(pady=20)
