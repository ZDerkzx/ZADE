# services.py

import json
import os
import subprocess

FILE_PATH = "commands.json"

def load_commands():
    if not os.path.exists(FILE_PATH):
        return []
    with open(FILE_PATH, "r") as f:
        return json.load(f)

def save_commands(commands):
    with open(FILE_PATH, "w") as f:
        json.dump(commands, f)

def add_command(cmd: str):
    commands = load_commands()
    commands.append(cmd)
    save_commands(commands)
    return cmd

def delete_command(index: int):
    commands = load_commands()
    if 0 <= index < len(commands):
        removed = commands.pop(index)
        save_commands(commands)
        return removed
    else:
        return None

def get_commands():
    return load_commands()

def run_commands(pause_time: str):
    commands = load_commands()
    if not commands:
        return False, "No hay comandos para ejecutar."
    array_str = json.dumps(commands)
    try:
        subprocess.run(['./taskers/task_executeCommands.exe', array_str, pause_time])
        return True, "Comandos ejecutados."
    except FileNotFoundError:
        return False, "No se encontró task_executeCommands.exe"
