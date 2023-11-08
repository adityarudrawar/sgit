import os
from pathlib import Path

HEADER_SPLIT_CHAR = b'|@|'
CONTENT_AND_HEADER_SPLIT_CHAR = b'||@||'
DATABASE_DIR = '.sgit'
OBJECTS_DIR = 'objects'
CWD = os.getcwd()

# Create the parent directory
database_dir_path = Path(DATABASE_DIR)
database_dir_path.mkdir(parents=True, exist_ok=True)

# Create the subdirectory within the parent directory
objects_dir_path = database_dir_path / OBJECTS_DIR
objects_dir_path.mkdir(parents=True, exist_ok=True)

# Create the index file
index_file_path = database_dir_path / "index"
index_file_path.touch()


def is_file_path(arg):
    if isinstance(arg, str):
        return os.path.isfile(arg)

    return False


def calculate_size(content):
    return len(content)


def make_dir(arg):
    arg = CWD + arg

    if not os.path.exists(arg):
        os.makedirs(arg)

    return True


def store_object(hash: str, content: any):

    # Create a directory using the first two number of the hash
    directory = objects_dir_path / f'{hash[:2]}'
    directory.mkdir(parents=True, exist_ok=True)

    # Create a file with the remaining hash
    file = directory / hash[2:]

    # Dump the content in that file
    file.write_bytes(content)

    return True


if __name__ == '__main__':
    pass
