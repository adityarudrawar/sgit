class Refs:
    _instance = None

    def __init__(self, path):
        self.path = path

    def update_head(self, hash):
        with open(self.path, "w") as file:
            file.write(hash)

    def read_head(self):
        with open(self.path, "r") as file:
            return file.read()

    def __new__(cls, path):
        if cls._instance is None:
            cls._instance = super(Refs, cls).__new__(cls)
        return cls._instance
