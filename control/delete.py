from rich.panel import Panel
from rich.console import Console
from cmd.cmd import clear

console = Console()

def delete(option, fs):
    clear()

    args = option.split()

    if len(args) < 2:
        console.print(Panel("Use: /deletefile --file_name", title="Error", border_style="red"))

    else:
        name = args[1].removeprefix("--")

        file = fs.open_file(name)

        if file is None:
            console.print(
                Panel(
                    "TypeError: No files found. Try another name",
                    style="#FF5C40",
                    title="Error",
                    border_style="red"
                )
            )

            input("Press ENTER to leave")
            clear()

        else:
            fs.delete_file(name)
            console.print(Panel(f"File '{name}' deleted successfully!", style="green", title="Success", border_style="green"))
            input("Press ENTER to leave")
            clear()