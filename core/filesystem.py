class File:
    def __init__(self, name):
        self.name = name
        self.content = ""


class Folder:
    def __init__(self, name, parent=None):
        self.name = name
        self.children = []
        self.parent = parent


class FileSystem:
    def __init__(self):
        self.root = Folder("/")
        self.current = self.root

    def create_folder(self, name):
        folder = Folder(name, self.current)
        self.current.children.append(folder)

    def create_file(self, name, content):
        file = File(name)
        file.content = content

        self.current.children.append(file)

    def delete_file(self, name):
        for item in self.current.children:
            if isinstance(item, File) and item.name == name:
                self.current.children.remove(item)
                return True
        return False

    def open_file(self, name):
        for item in self.current.children:

            if isinstance(item, File) and item.name == name:
                return item

    def open_folder(self, name):
        for item in self.current.children:

            if isinstance(item, Folder) and item.name == name:
                return item

        return None