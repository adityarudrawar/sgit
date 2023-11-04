import hashlib
import sys

def calculate_sha1_and_size(file_path):
    try:
        with open(file_path, 'rb') as file:
            contents = file.read()
            file_size = len(contents)
            sha1_hash = hashlib.sha1(contents).hexdigest()

        return sha1_hash, file_size

    except FileNotFoundError:
        return "FILE NOT FOUND"  # File not found
    except Exception as e:
        return str(e)  # Error reading file


if __name__ == '__main__':
    print("SGIT STARTED")

    while(True):
