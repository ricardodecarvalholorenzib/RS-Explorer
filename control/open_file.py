from rich.panel import Panel
from rich.console import Console
from rich.table import Table
from rich import box
from cmd.cmd import clear

console = Console()


def open_file_command(option, fs):
    clear()

    args = option.split()

    if len(args) < 2:
        print("Use: /openfile --file_name")

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

        else:
            console.print(Panel(file.content, title=file.name))

            input("Press ENTER to leave")