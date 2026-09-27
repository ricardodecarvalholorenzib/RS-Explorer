from core.filesystem import FileSystem

def create_file_command(option, fs):
    args = option.split("--")

    if len(args) < 3:
        print("Use: /createfile --file_name --content")

    else:
        name = args[1].strip()
        content = args[2].strip()

        fs.create_file(name, content)