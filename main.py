import utils
import hashing

if __name__ == '__main__':
    print("SGIT STARTED")

    commands = ["sgit hash-object README.md", "sgit add-to-index README.md"]
    for command_input in commands:
        print("WAITING FOR YOUR COMMAND")

        command_and_args = command_input.split(" ")
        command = command_and_args[1]
        args = command_and_args[2:]

        if command == 'init':
            utils.init_sgit()
        elif command == 'hash-object':
            sha1_hash, content = hashing.hash_object(args[0])
            utils.store_object(sha1_hash, content)
        elif command == 'add-to-index':
            pass
        elif command == 'store-to-db':
            pass
        elif command == 'add':
            pass
        elif command == 'create-tree':
            pass
        elif command == '':
            pass
        elif command == 'unhash-object':
            pass
        break
