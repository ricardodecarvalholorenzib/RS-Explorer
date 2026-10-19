from rich.panel import Panel
from rich.console import Console
from __main__ import init
from cmd.cmd import clear
from cmd.slash import Commands

console = Console()


def open_folder_command(option, fs):
    clear()

    args = option.split()

    if len(args) < 2:
        print("Use: /openfolder --folder_name")
        input("Press ENTER to leave")
        return

    name = args[1].removeprefix("--")

    folder = fs.open_folder(name)

    if folder is None:
        console.print(
            Panel(
                "No folder found. Try another name.",
                style="#FF5C40",
                title="Error",
                border_style="red"
            )
        )
        input("Press ENTER to leave")
        return

    else:
        console.print(
            Panel(
                "",
                title=folder.name
            )
        )

        while True:
            option = input("> ").lower()

            if option.startswith("/exit"):
                break

            if Commands.create_file(option, fs):
                continue

            if Commands.back():
                continue


    fs.current = folder