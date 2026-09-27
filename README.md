# 📋 RS Explorer

> A lightweight virtual file explorer built in Python for the terminal.

RS Explorer is a personal project that simulates a file system directly inside the program.  
It does **not** create, modify, or delete real files and folders on the computer.

The project is being developed incrementally, with the goal of evolving from a simple virtual file manager into a more complete terminal-based explorer.

## ✨ Current Features

- 📄 Create virtual files
- 📁 Create virtual folders
- 📖 Open virtual files and display their contents
- 📋 Display files and folders in the current directory
- 🧹 Clear the terminal
- ❓ Built-in help command
- 🎨 Rich terminal interface
- 🧠 Object-oriented virtual file system

## 🖥️ Example

The explorer displays the current virtual directory using a Rich table:

```text
╔══════════════════════════════════════════╗
║              📋 RS Explorer              ║
╠══════════════════╦═══════════════════════╣
║    File Name     ║         Type          ║
╠══════════════════╬═══════════════════════╣
║     notes.txt    ║       📄 File         ║
║      school      ║      📁 Folder        ║
╚══════════════════╩═══════════════════════╝
```

Files and folders shown by RS Explorer exist only in the application's in-memory virtual file system.

## ⌨️ Commands

| Command | Description |
|---|---|
| `/createfile --<file_name> --<content>` | Creates a virtual file with content |
| `/openfile --<file_name>` | Opens a virtual file |
| `/createfolder --<folder_name>` | Creates a virtual folder |
| `/clear` | Clears the terminal |
| `/help` | Shows available commands |
| `/exit` | Closes RS Explorer |

### Example

```text
/createfile --notes.txt --Hello, world!
/createfolder --school
/openfile --notes.txt
```

## 🏗️ Project Structure

```text
RS-Explorer/
├── __main__.py
├── assistance/
│   └── help.py
├── cmd/
│   ├── __init__.py
│   └── cmd.py
├── control/
│   ├── __init__.py
│   ├── create_file.py
│   ├── create_folder.py
│   └── open_file.py
├── core/
│   ├── __init__.py
│   └── filesystem.py
├── requirements
└── README.md
```

### Architecture

- **`core/`** — contains the virtual file system and its data models.
- **`control/`** — handles user commands and connects them to the file system.
- **`assistance/`** — contains help and user assistance.
- **`cmd/`** — contains terminal-related utilities.
- **`__main__.py`** — application entry point.

## 🧩 How It Works

RS Explorer uses a simple tree structure:

```text
FileSystem
└── root (Folder)
    └── children
        ├── File
        ├── File
        └── Folder
            └── children
```

A `Folder` contains a list of `children`, which can contain both `File` and `Folder` objects.

This allows the project to simulate a file system without touching the real operating system.

## 🛠️ Technologies

- **Python**
- **Rich**

Rich is used to build the terminal interface, including tables and panels.

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/ricardodecarvalholorenzib/RS-Explorer.git
cd RS-Explorer
```

Install the dependency:

```bash
pip install rich
```

Run the project:

```bash
python __main__.py
```

> RS Explorer currently uses `cls` to clear the terminal, so the terminal utility is currently intended for Windows.

## 🗺️ Roadmap

The project is intentionally being developed in small versions.

### V0.1 — Core
- [x] Virtual file system
- [x] Create files
- [x] Create folders
- [x] Open files
- [x] List current directory
- [x] Help system
- [x] Rich interface

### Future Versions
- [ ] Navigate between folders
- [ ] Persistent virtual file system
- [ ] Delete files and folders
- [ ] Rename files and folders
- [ ] Copy and move items
- [ ] Search
- [ ] Text editor
- [ ] File metadata
- [ ] Themes and improved interface
- [ ] Trash/recycle system

## 🎯 Project Goal

RS Explorer is primarily a learning project focused on:

- Python classes and objects
- Data structures
- Modular project organization
- Command parsing
- Terminal interfaces
- Designing software that can evolve over multiple versions

The long-term goal is to turn this small prototype into a complete and polished virtual file explorer.

## 📄 License

This project does not currently include a license.
