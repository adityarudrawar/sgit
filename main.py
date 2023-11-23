import utils
import hashing
from repository import Repository

if __name__ == '__main__':
    print("SGIT STARTED")

    repository = Repository()

    commands = ["sgit init", "sgit commit"]
    for command_input in commands:

        command_and_args = command_input.split(" ")
        command = command_and_args[1]
        args = command_and_args[2:]

        if command == 'init':
            repository.init()
        elif command == 'commit':
            repository.commit()
        elif command == 'hash-object':
            sha1_hash, content = hashing.hash_object(args[0])
            utils.store_object(sha1_hash, content)
        elif command == 'add-to-index':
            repository.add_to_index(args[0])
        elif command == 'create-tree':
            repository.create_tree_from_index()
        elif command == 'create-tree':
            pass
        elif command == '':
            pass
        elif command == 'unhash-object':
            pass
