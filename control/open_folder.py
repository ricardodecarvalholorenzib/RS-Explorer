from rich.console import Console
from rich.panel import Panel

console = Console()


def open_folder_command(option, fs):
    parts = option.split("--", 1)

    if len(parts) < 2 or not parts[1].strip():
        console.print(
            Panel(
                "Use: /openfolder --folder_name",
                title="Missing folder name",
                border_style="red",
            )
        )
        input("Press ENTER to leave")
        return

    name = parts[1].strip()
    folder = fs.open_folder(name)

    if folder is None:
        console.print(
            Panel(
                f"No folder named '{name}' was found in the current directory.",
                title="Folder not found",
                border_style="red",
            )
        )
        input("Press ENTER to leave")
        return

    fs.current = folder
