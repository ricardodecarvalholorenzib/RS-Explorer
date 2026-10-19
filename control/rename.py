from cmd.cmd import clear
from rich.panel import Panel
from rich.console import Console

console = Console()


def rename(option, fs):
    clear()

    args = option.split()

    if len(args) < 2:
        console.print(Panel("Use: /editfilename --file_name", title="Error", border_style="red"))
        input("Press ENTER to leave")
        clear()

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
            new_name = input("Enter the new name for the file: ")

            if new_name:
                file.name = new_name
                console.print(Panel(f"File renamed to: '{new_name}'", title="Success", border_style="green"))
            else:
                console.print(Panel("No new name provided. File not renamed.", title="Info", border_style="yellow"))

            input("Press ENTER to leave")
            clear()