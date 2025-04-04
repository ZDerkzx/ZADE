import subprocess
import json

import customtkinter as ctk


lista_Command = []

app = ctk.CTk()
app.geometry("400x300")
app.title("Zade Automatization")

def task_exc_AddCMD():
    input1 = input_1.get()
    lista_Command.append(input1)
    print(lista_Command)
    return lista_Command

def task_exc_start(pausetime):    
    array_str = json.dumps(lista_Command)
    subprocess.run(['./taskers/task_executeCommands.exe', array_str, pausetime])

def fn_deleteCMD(index):
    lista_Command.pop(index)

input_1 = ctk.CTkEntry(app, placeholder_text="Escribe el comando")
input_1.pack(pady=5)

button_1 = ctk.CTkButton(app, text="Add Command", command=task_exc_AddCMD)
button_1.pack(pady=5)

input_2 = ctk.CTkEntry(app, placeholder_text="Ingresa El tiempo")
input_2.pack(pady=5)

button_2 = ctk.CTkButton(app, text="Submit", command=lambda: task_exc_start(input_2.get()))
button_2.pack(pady=5)

app.mainloop()


