# main.py

import click
from services import add_command, delete_command, get_commands, run_commands

@click.group()
def cli():
    pass

@cli.command()
@click.argument("cmd")
def add(cmd):
    """Agrega un comando a la lista"""
    added = add_command(cmd)
    click.echo(f"✅ Comando agregado: {added}")

@cli.command()
@click.argument("index", type=int)
def delete(index):
    """Elimina un comando por índice"""
    removed = delete_command(index)
    if removed:
        click.echo(f"🗑️ Comando eliminado: {removed}")
    else:
        click.echo("❌ Índice inválido.")

@cli.command(name="list")
def list_commands():
    """Muestra la lista de comandos"""
    commands = get_commands()
    if not commands:
        click.echo("📭 Lista vacía.")
    else:
        for i, cmd in enumerate(commands):
            click.echo(f"{i}: {cmd}")

@cli.command()
@click.argument("pause_time")
def run(pause_time):
    """Ejecuta los comandos usando task_executeCommands.exe"""
    success, message = run_commands(pause_time)
    icon = "🚀" if success else "❌"
    click.echo(f"{icon} {message}")

if __name__ == '__main__':
    cli()

