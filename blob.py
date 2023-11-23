class Blob:
    def __init__(self, content):
        self.content = content
        self.type = "blob"
        self.hash = None

    def __str__(self):
        return str(self.content)

    def __len__(self):
        return len(self.content)
