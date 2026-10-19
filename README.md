RS Explorer
A terminal-based virtual file explorer built with Python and Rich.

RS Explorer simulates a small file system inside the running program. Files and folders are stored in memory only: the project does not create, edit, or delete files on your actual computer, and its virtual contents are lost when the application closes.
Features
- Create virtual files with content.
- Create virtual folders.
- List the contents of the current virtual directory.
- Open folders and move back to their parent directory.
- Open files and view their contents.
- Edit a file's content, rename a file, or delete a file from the file-action prompt.
- Built-in command help.
- Rich-powered terminal tables and panels.
- Modular code split into command handlers and file-system logic.
Requirements
- Python 3.9 or newer is recommended.
- The rich package listed in requirements.txt.
Installation
Clone the repository and enter its directory:
git clone https://github.com/ricardodecarvalholorenzib/RS-Explorer.git
cd RS-Explorer
Install dependencies:
pip install -r requirements.txt
Start RS Explorer:
python __main__.py
Platform note: the current terminal-clear utility uses cls, which is intended for Windows. Cross-platform terminal clearing is a planned improvement.

Commands
Command names are shown in lowercase. File names and content preserve the case you type; keep the command itself in lowercase.
Command	What it does
/createfile --<file_name> --<content>	Creates a virtual file containing the supplied text.
/createfolder --<folder_name>	Creates a virtual folder in the current directory.
/openfile --<file_name>	Displays a virtual file's content and opens the file-action prompt.
/openfolder --<folder_name>	Enters a folder in the current virtual file system.
/back	Returns to the parent folder. At the root, nothing changes.
/clear	Clears the terminal.
/help	Displays the built-in command reference.
/exit	Closes RS Explorer.


File actions
After running /openfile --<file_name>, RS Explorer displays the file and asks for an action. Use one of these commands at that prompt:
Command	What it does
/editfilecontent --<file_name>	Prompts for replacement content. Leaving the new content empty keeps the existing content.
/editfilename --<file_name>	Prompts for a new file name.
/deletefile --<file_name>	Deletes the virtual file from the current directory.
/back	Leaves the file-action prompt without changing the file.


The file-action commands operate on files in the current directory. The current argument parser is intentionally simple; names containing spaces or the -- separator may not work consistently in every command.
Example session
/createfolder --school
/openfolder --school
/createfile --notes.txt --Review math before Friday
/openfile --notes.txt
/editfilecontent --notes.txt
/back
/exit
Commands are processed in the current virtual directory. The example is illustrative; each command is entered at the prompt shown by the application, and /openfile has its own action prompt.
Earlier build vs. current build
Earlier build	Current build
Focused on creating and opening virtual files and folders.	Adds a clearer separation between command dispatch, file-system logic, and individual operations.
Mostly used at the root directory.	Supports moving into folders and returning to a parent directory.
File interaction was limited.	Opened files can be edited, renamed, or deleted through the file-action prompt.
Help and feature documentation were limited.	Includes an expanded command reference and a roadmap that reflects the current state of the project.
Simple terminal output.	Uses Rich tables and panels to make directory listings and messages easier to read.


Project structure
RS-Explorer/
├── __main__.py
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
- core/ — virtual file and folder models, plus file-system operations.
- cmd/ — terminal utilities and slash-command dispatch.
- control/ — handlers for creating, opening, editing, renaming, and deleting virtual items.
- assistance/ — built-in help interface.
- __main__.py — application entry point and directory listing.
How the virtual file system works
The FileSystem owns a root folder and tracks the folder currently being viewed. Each folder stores its child files and folders; folders also retain a reference to their parent, which enables /back navigation.
FileSystem
└── root
    ├── File
    └── Folder
        ├── File
        └── Folder
This is an in-memory model, not a wrapper around the operating system's real file system. At this stage, RS Explorer does not save virtual data between sessions.
Roadmap
The project is evolving gradually. The next goals are focused on reliability before adding lots of extra features.
Completed in the current build
- [x] In-memory virtual file system.
- [x] Create files and folders.
- [x] List the current directory.
- [x] Open files and view content.
- [x] Navigate into folders and return with /back.
- [x] Edit file content.
- [x] Rename and delete files.
- [x] Built-in help and Rich terminal output.
- [x] Separate command handlers into modules.
Next milestones
1. Input validation: prevent duplicate names, improve missing-argument messages, and make command parsing predictable.
2. Persistence: save and load the virtual file system using JSON, with checks for invalid or damaged save data.
3. Better file and folder operations: rename, delete, move, and copy folders as well as files.
4. Search and navigation: add tree view, find-by-name, and clearer current-directory information.
5. Reliability: add automated tests for file creation, editing, deletion, and folder navigation.
6. Polish: support terminal clearing across operating systems and improve feedback for invalid commands.
Learning goals
RS Explorer is a learning project for practicing Python classes and objects, data structures, modular design, command parsing, terminal interfaces, and incremental software development.
License
No license has been added to this repository yet. Unless a license is added, reuse and redistribution are not automatically granted.
