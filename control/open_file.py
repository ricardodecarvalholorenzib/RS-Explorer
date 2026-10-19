from rich.panel import Panel
from rich.console import Console
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

            option = input("> ").lower()
            
            if option.startswith("/editfilecontent"):
                from control.edit import edit
                edit(option, fs)

            if option.startswith("/deletefile"):
                from control.delete import delete
                delete(option, fs)

            if option.startswith("/editfilename"):
                from control.rename import rename
                rename(option, fs)

            else:
                console.print(Panel("Invalid command. Use /editfilecontent, /deletefile, or /editfilename.", title="Error", border_style="red"))
                input("Press ENTER to leave")

            clear()