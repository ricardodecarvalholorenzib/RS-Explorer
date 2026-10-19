def create_folder_command(option, fs):
    args = option.split("--")

    if len(args) < 2:
        print("Use: /createfile --file_name")

    else:
        name = args[1].strip()
        fs.create_folder(name)