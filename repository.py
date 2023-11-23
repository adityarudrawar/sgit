import os
from pathlib import Path
from workspace import Workspace
from blob import Blob
from database import Database
from entry import Entry
from tree import Tree
from author import Author
from commit import Commit
import time

HEADER_SPLIT_CHAR = b'|@|'
CONTENT_AND_HEADER_SPLIT_CHAR = b'||@||'
SGIT_DIR = '.sgit'
OBJECTS_DIR = 'objects'
INDEX_FILE_NAME = 'index'
REF_DIR = 'ref'
HEAD_FILE_NAME = "HEAD"
CWD = os.getcwd()


class Repository:
    _instance = None

    def __init__(self):
        pass

    def init(self):
        # Create the parent directory
        self.SGIT_PATH = Path(SGIT_DIR)
        self.SGIT_PATH.mkdir(parents=True, exist_ok=True)

        # Create the subdirectory within the parent directory
        self.OBJECTS_PATH = self.SGIT_PATH / OBJECTS_DIR
        self.OBJECTS_PATH.mkdir(parents=True, exist_ok=True)

        self.REF_PATH = self.SGIT_PATH / REF_DIR
        self.REF_PATH.mkdir(parents=True, exist_ok=True)

        # Create the index file
        self.INDEX_PATH = self.SGIT_PATH / INDEX_FILE_NAME
        self.INDEX_PATH.touch()

        self.HEAD_PATH = self.SGIT_PATH / HEAD_FILE_NAME
        self.HEAD_PATH.touch()

        print("INITIALIZED AN EMPTY SGIT REPOSITORY")

    def commit(self):
        workspace = Workspace(CWD)
        database = Database(self.OBJECTS_PATH)

        entries = []

        for file in workspace.list_files():
            content = workspace.read_file(file)
            blob = Blob(content)

            database.store(blob)

            entries.append(Entry(file, blob.hash))

        tree = Tree(entries)
        database.store(tree)

        name = "Aditya Arun Rudrawar"
        email = "adirudrawar@gmail.com"
        author = Author(name, email, time.time())

        message = input("Commit message: ")

        commit = Commit(tree.hash, author, message)
        database.store(commit)

        with open(self.HEAD_PATH, "w") as file:
            file.write(commit.hash)

        print("[(root-commit) ", commit.hash, "]", " ", message)

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Repository, cls).__new__(cls)
        return cls._instance
