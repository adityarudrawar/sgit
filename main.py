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
        else:
            print("Not a valid command")
