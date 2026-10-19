from rich import box
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from cmd.cmd import clear


def help():
    console = Console()

    table = Table(
        title="RS Explorer — Command Help",
        border_style="blue",
        box=box.DOUBLE,
        show_lines=True,
        expand=True,
    )
    table.add_column("Command", style="green", justify="left", no_wrap=True)
    table.add_column("Description", style="white", justify="left")

    table.add_row("/createfile --<file_name> --<content>", "Create a virtual file with the supplied content.")
    table.add_row("/createfolder --<folder_name>", "Create a virtual folder in the current directory.")
    table.add_row("/openfile --<file_name>", "Display a file and open its action prompt.")
    table.add_row("/openfolder --<folder_name>", "Move into a virtual folder.")
    table.add_row("/back", "Return to the parent folder; at the root, stay where you are.")
    table.add_row("/clear", "Clear the terminal.")
    table.add_row("/help", "Display this command reference.")
    table.add_row("/exit", "Close RS Explorer.")

    console.print(table)
    console.print(
        Panel(
            "After opening a file, use one of these actions at the file prompt:\n"
            "[green]/editfilecontent --<file_name>[/] — replace its content\n"
            "[green]/editfilename --<file_name>[/] — rename the file\n"
            "[green]/deletefile --<file_name>[/] — delete the virtual file\n"
            "[green]/back[/] — leave the file prompt without changing it\n\n"
            "Virtual files and folders exist only while this program is running.",
            title="File actions and note",
            border_style="blue",
        )
    )

    input("\nPress ENTER to return to RS Explorer...")
    clear()
