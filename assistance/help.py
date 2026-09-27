def help():
    from rich.table import Table
    from rich import box
    from rich.console import Console
    from cmd.cmd import clear

    console = Console()

    table = Table(
        title="📋 RS Explorer",
        border_style="blue", 
        box=box.DOUBLE,
        show_lines=True,
        expand=True
    )

    table.add_column("Commands", style="green", justify="center")
    table.add_column("Description", style="dim", justify="left")

    table.add_row("/createfile --<file_name> --<content>", "Create a new file with the specified name and content")
    table.add_row("/openfile --<file_name>", "Open the file with the specified name and content inside")
    table.add_row("/clear", "Clear the screen")
    table.add_row("/createfolder --<folder_name>", "Create a new folder with the specified name")
    table.add_row("/help", "Show all available commands")
    table.add_row("/exit", "Close the program")

    console.print(table)

    input("\nPress ENTER to leave")
    clear()