import hashlib
import zlib


class Database:
    _instance = None

    def __init__(self, objects_path):
        self.objects_path = objects_path

    def store(self, object):
        to_hash = object.type.encode('utf-8') + b' ' + \
            str(len(object)).encode('utf-8') + \
            b'\0' + str(object).encode("utf-8")

        hash = hashlib.sha1(to_hash).hexdigest()
        object.hash = hash

        self.write_object(hash, to_hash)

    def write_object(self, hash, content):

        # Create a directory for the object
        directory = self.objects_path / f'{hash[:2]}'
        directory.mkdir(parents=True, exist_ok=True)

        # Create a file with the remaining hash
        file = directory / hash[2:]

        # Compress the file to save space
        content = zlib.compress(content)

        # Dump the compressed content in that file
        file.write_bytes(content)

    def __new__(cls, path):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
        return cls._instance
