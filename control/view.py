from rich import box
from rich.console import Console
from rich.table import Table
from core.filesystem import File

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