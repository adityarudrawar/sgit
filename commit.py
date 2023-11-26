class Commit:
    def __init__(self, parent, tree_hash, author, message):
        self.tree_hash = tree_hash
        self.author = author
        self.message = message
        self.type = "commit"
        self.lines = ""
        self.parent = parent
        self.hash = None

    def __str__(self):
        lines = ["tree " + self.tree_hash,
                 "parent " + self.parent if self.parent != None else "",
                 "author " + str(self.author),
                 "committer " + str(self.author), "", self.message]

        self.lines = "\n".join(lines)
        return self.lines

    def __len__(self):
        return len(self.lines)
