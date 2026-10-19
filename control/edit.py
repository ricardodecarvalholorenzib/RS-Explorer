from rich.panel import Panel
from rich.console import Console
from cmd.cmd import clear

console = Console()

def edit(option, fs):
    clear()

    args = option.split()

    if len(args) < 2:
        console.print(Panel("Use: /editfilecontent --file_name", title="Error", border_style="red"))
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

            input("Press ENTER to leave")
            clear()

        else:
            console.print(Panel(file.content, title=file.name))

            new_content = input("Type the new content for the file (or leave empty to keep current content): ")

            if new_content:
                file.content = new_content
                console.print(Panel("File content updated successfully!", style="green", title="Success", border_style="green"))
                input("Press ENTER to leave")
                clear()

            else:
                console.print(Panel("File content remains unchanged.", style="yellow", title="Info", border_style="yellow"))
                input("Press ENTER to leave")
                clear()

            clear()