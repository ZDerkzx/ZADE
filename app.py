import customtkinter as ctk

def mostrar_valor():
    # Obtener el valor actual del CTkSlider
    valor = slider.get()
    print(f"Valor seleccionado: {valor}")

# Crear la ventana principal
ventana = ctk.CTk()

# Crear un widget CTkSlider (barra deslizante)
label = ctk.CTkLabel(ventana, text=slider.get())
label.pack(padx=20, pady=10)

slider = ctk.CTkSlider(ventana, from_=0, to=100)
slider.pack(padx=20, pady=20)

# Crear un botón para mostrar el valor actual del CTkSlider
boton = ctk.CTkButton(ventana, text="Mostrar valor", command=mostrar_valor)
boton.pack(padx=20, pady=20)

# Ejecutar el bucle principal de la interfaz gráfica
ventana.mainloop()
