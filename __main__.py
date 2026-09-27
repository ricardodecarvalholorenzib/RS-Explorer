from rich.panel import Panel
from rich.console import Console
from rich.table import Table
from rich import box
from cmd.cmd import clear
from core.filesystem import FileSystem, File

fs = FileSystem()

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

while True:
    show_files(fs)

    option = input("> ").lower()

    if option.startswith("/createfile"):
        from control.create_file import create_file_command
        
        create_file_command(option, fs)
        clear()

    elif option.startswith("/openfile"):
        from control.open_file import open_file_command
        open_file_command(option, fs)

    elif option.startswith("/clear"):
        clear()

    elif option.startswith("/createfolder"):
        from control.create_folder import create_folder_command

        create_folder_command(option, fs)
        clear()

    elif option.startswith("/help"):
        from assistance.help import help

        help()
        clear()

    elif option.startswith("/exit"):
        break

    else:
        console.print(Panel(f"\n[bright_red]TypeError[/]: [red]cannot find command '{option}'. Use '/help' to see all the available commands[/]", style="#FF5C40", title="Error", border_style="red"))