import customtkinter as ctk

from pages.HomePage import HomePage
from pages.AnotherPage import AnotherPage

from components.NavBar import NavBar

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("CTk App")
        self.root.geometry("800x600")  # Opcional: tamaño inicial

        self.pages = {
            "home": HomePage(self),
            "other": AnotherPage(self),
        }

        self.nav_map = {page.frame_title: key for key, page in self.pages.items()}

        for page in self.pages.values():
            NavBar(self, page.frame, self.nav_map)

        self.show_page("home")
    
    def show_page(self, page_name):
        for page in self.pages.values():
            page.frame.pack_forget()

        self.pages[page_name].frame.pack(fill="both", expand=True)

if __name__ == "__main__":
    ctk.set_appearance_mode("System")  # También puedes usar "Dark" o "Light"
    ctk.set_default_color_theme("blue")  # Puedes cambiar el color del tema

    root = ctk.CTk()  # Cambio aquí
    app = App(root)
    root.mainloop()
