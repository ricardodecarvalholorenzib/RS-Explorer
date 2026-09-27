class File:
    def __init__(self, name):
        self.name = name
        self.content = ""


class Folder:
    def __init__(self, name):
        self.name = name
        self.children = []


class FileSystem:
    def __init__(self):
        self.root = Folder("/")
        self.current = self.root

    def create_folder(self, name):
        folder = Folder(name)
        self.current.children.append(folder)

    def create_file(self, name, content):
        file = File(name)
        file.content = content

        self.current.children.append(file)

    def open_file(self, name):
        for item in self.current.children:

            if isinstance(item, File) and item.name == name:
                return item

        return None