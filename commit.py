class Commit:
    def __init__(self, tree_hash, author, message):
        self.tree_hash = tree_hash
        self.author = author
        self.message = message
        self.type = "commit"
        self.lines = ""
        self.hash = None

    def __str__(self):
        lines = ["tree " + self.tree_hash, "author " +
                 str(self.author), "committer " + str(self.author), "", self.message]

        self.lines = "\n".join(lines)
        return self.lines

    def __len__(self):
        return len(self.lines)
