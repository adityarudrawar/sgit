class Author:
    def __init__(self, name, email, time):
        self.name = name
        self.email = email
        self.time = time

    def __str__(self):
        return self.name + " <" + self.email + "> " + str(int(self.time))
