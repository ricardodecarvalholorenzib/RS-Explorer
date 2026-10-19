from rich.console import Console
from rich.panel import Panel

from cmd.cmd import clear

console = Console()


def open_file_command(option, fs):
    clear()
    parts = option.split("--", 1)

    if len(parts) < 2 or not parts[1].strip():
        console.print(
            Panel(
                "Use: /openfile --file_name",
                title="Missing file name",
                border_style="red",
            )
        )
        input("Press ENTER to leave")
        clear()
        return

    name = parts[1].strip()
    file = fs.open_file(name)

    if file is None:
        console.print(
            Panel(
                f"No file named '{name}' was found in the current directory.",
                title="File not found",
                border_style="red",
            )
        )
        input("Press ENTER to leave")
        clear()
        return

    console.print(Panel(file.content or "(empty file)", title=file.name))
    console.print(
        "File actions: /editfilecontent --<file_name>, "
        "/editfilename --<file_name>, /deletefile --<file_name>, or /back"
    )
    action = input("> ").strip()
    action_lower = action.lower()

    if action_lower.startswith("/editfilecontent"):
        from control.edit import edit

        edit(action, fs)
    elif action_lower.startswith("/deletefile"):
        from control.delete import delete

        delete(action, fs)
    elif action_lower.startswith("/editfilename"):
        from control.rename import rename

        rename(action, fs)
    elif action_lower.startswith("/back") or not action:
        pass

    else:
        console.print(
            Panel(
                "Invalid file action. Use /editfilecontent, /editfilename, "
                "/deletefile, or /back.",
                title="Unknown file action",
                border_style="red",
            )
        )
        input("Press ENTER to leave")

    clear()
