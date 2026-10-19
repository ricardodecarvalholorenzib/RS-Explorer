from rich.console import Console
from rich.panel import Panel
from cmd.cmd import clear

class Commands:
    def __init__(self, fs):
        self.fs = fs
        self.console = Console()

    def get_option(self):
        return input("> ").strip()

    def create_file(self, option):
        if option.startswith("/createfile"):
            from control.create_file import create_file_command

            create_file_command(option, self.fs)
            clear()
            return True

        return False

    def open_file(self, option):
        if option.startswith("/openfile"):
            from control.open_file import open_file_command

            open_file_command(option, self.fs)
            return True

        return False

    def clear_screen(self, option):
        if option.startswith("/clear"):
            clear()
            return True

        return False

    def create_folder(self, option):
        if option.startswith("/createfolder"):
            from control.create_folder import create_folder_command

            create_folder_command(option, self.fs)
            clear()
            return True

        return False

    def show_help(self, option):
        if option.startswith("/help"):
            from assistance.help import help

            help()
            clear()
            return True

        return False

    def open_folder(self, option):
        if option.startswith("/openfolder"):
            from control.open_folder import open_folder_command

            open_folder_command(option, self.fs)
            clear()
            return True

        return False

    def back(self, option):
        if option.startswith("/back"):
            if self.fs.current.parent is not None:
                self.fs.current = self.fs.current.parent
                return True

            return True

        return False

    def exit(self, option):
        return option.startswith("/exit")

    def error(self, option):
        self.console.print(
            Panel(
                f"\n[bright_red]Error[/]: [red]cannot find command '{option}'. "
                "Use '/help' to see all the available commands[/]",
                style="#FF5C40",
                title="Error",
                border_style="red"
            )
        )
