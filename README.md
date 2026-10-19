# RS Explorer

> A terminal-based virtual file explorer built with Python and Rich.

RS Explorer simulates a small file system entirely in memory. No real files are created, edited, or deleted on your computer, and all virtual contents are lost when the application closes.

---

## Features

- Create virtual files with custom content and create virtual folders.
- List current directory contents with Rich formatting.
- Folder navigation (open folders and return to parent directory).
- File actions prompt: view, edit content, rename, or delete virtual files.
- Built-in command help system (/help).
- Rich-powered terminal tables and panels for clear output.
- Modular code architecture separating system logic, commands, and handlers.

---

## Requirements

- Python 3.9 or newer is recommended.
- Rich package listed in requirements.txt.

---

## Installation and Setup

1. Clone the repository and enter its directory:
   git clone [https://github.com/ricardodecarvalholorenzib/RS-Explorer.git](https://github.com/ricardodecarvalholorenzib/RS-Explorer.git)
   cd RS-Explorer

2. Install dependencies:
   pip install -r requirements.txt

3. Start RS Explorer:
   python main.py

> Platform Note: The current terminal-clear utility uses cls, which is intended for Windows. Cross-platform terminal clearing is a planned improvement.

---

## Command Reference

> Command names are shown in lowercase. File names and content preserve the case you type. The current argument parser is intentionally simple; names containing spaces or the -- separator may not work consistently in every command.

| Command | Description |
| :--- | :--- |
| /createfile --<file_name> --<content> | Creates a virtual file containing the supplied text. |
| /createfolder --<folder_name> | Creates a virtual folder in the current directory. |
| /openfile --<file_name> | Displays a virtual file's content and opens the file-action prompt. |
| /openfolder --<folder_name> | Enters a folder in the current virtual file system. |
| /back | Returns to the parent folder. At the root, nothing changes. |
| /clear | Clears the terminal screen. |
| /help | Displays the built-in command reference. |
| /exit | Closes RS Explorer. |

### File Actions
After running /openfile --<file_name>, use one of these commands at the prompt:

| Command | Description |
| :--- | :--- |
| /editfilecontent --<file_name> | Prompts for replacement content (leaving empty keeps existing content). |
| /editfilename --<file_name> | Prompts for a new file name. |
| /deletefile --<file_name> | Deletes the virtual file from the current directory. |
| /back | Leaves the file-action prompt without changing the file. |

---

## Example Session

/createfolder --school
/openfolder --school
/createfile --notes.txt --Review math before Friday
/openfile --notes.txt
/editfilecontent --notes.txt
/back
/exit

---

## Project Structure

RS-Explorer/
├── main.py
├── assistance/
│   └── help.py
├── cmd/
│   ├── __init__.py
│   ├── cmd.py
│   └── slash.py
├── control/
│   ├── __init__.py
│   ├── create_file.py
│   ├── create_folder.py
│   ├── delete.py
│   ├── edit.py
│   ├── open_file.py
│   ├── open_folder.py
│   ├── rename.py
│   └── view.py
├── core/
│   ├── __init__.py
│   └── filesystem.py
├── requirements.txt
└── README.md

- core/ — Virtual file and folder models, plus file-system operations.
- cmd/ — Terminal utilities and slash-command dispatch.
- control/ — Handlers for creating, opening, editing, renaming, and deleting virtual items.
- assistance/ — Built-in help interface.
- main.py — Application entry point and directory listing.

---

## Roadmap

- [x] In-memory virtual file system.
- [x] Create files and folders.
- [x] List, view, edit, rename, and delete files.
- [x] Navigate into folders and return with /back.
- [x] Built-in help and Rich terminal output.
- [ ] Input validation: Prevent duplicate names and handle missing arguments.
- [ ] Persistence: Save and load the virtual file system using JSON.
- [ ] Advanced operations: Rename, delete, move, and copy folders and files.
- [ ] Search and navigation: Add tree view and find-by-name features.
- [ ] Reliability: Automated tests for file and folder operations.
- [ ] Polish: Cross-platform terminal clearing and improved error feedback.

---

## Learning Goals

RS Explorer is a learning project for practicing:
- Python classes and Object-Oriented Programming (OOP).
- Data structures.
- Modular architecture design.
- Command parsing and terminal user interfaces.
- Incremental software development.

---

## License

No license has been added to this repository yet. Unless a license is added, reuse and redistribution rights are not automatically granted.
