import os


class Workspace:
    IGNORE_FILES = [".", "..", ".git"]
    _instance = None

    def __init__(self, path):
        self.path = path

    def list_files(self):
        file_list = []
        for root, dirs, files in os.walk(self.path):

            # TODO: Ignore folders starting with a dot, or folders that are in .sgitignore
            dirs[:] = [d for d in dirs if not (
                d.startswith('.') or d.startswith('..') or d.startswith('__'))]
            for file in files:
                file_list.append(os.path.join(root, file))
        return file_list

    def read_file(self, path):
        with open(path, 'r') as file:
            content = file.read()
            return content

        return None

    def __new__(cls, path):
        if cls._instance is None:
            cls._instance = super(Workspace, cls).__new__(cls)
        return cls._instance
