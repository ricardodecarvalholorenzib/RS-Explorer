from core.filesystem import File, FileSystem
from cmd.slash import Commands
from rich.console import Console
from rich.table import Table
from rich import box

console = Console()

def show_files(fs):
    table = Table(
        title="📋 RS Explorer",
        border_style="blue",
        box=box.DOUBLE,
        show_lines=True,
        expand=True
    )

    table.add_column("File Name", style="cyan", justify="center")
    table.add_column("Type", style="cyan", justify="center")

    if not fs.current.children:
        table.add_row("No files", "No type")
    else:
        for arquivo in fs.current.children:
            if isinstance(arquivo, File):
                tipo = "📄 File"
            else:
                tipo = "📁 Folder"

            table.add_row(arquivo.name, tipo)

    console.print(table)

def init():

    fs = FileSystem()
    commands = Commands(fs)

    while True:

        show_files(fs)

        option = commands.get_option()

        if commands.exit(option):
            break

        if commands.create_file(option):
            continue

        if commands.open_file(option):
            continue

        if commands.clear_screen(option):
            continue

        if commands.create_folder(option):
            continue

        if commands.show_help(option):
            continue

        if commands.open_folder(option):
            continue

        if commands.back(option):
            continue

        else:
            commands.error(option)

init()