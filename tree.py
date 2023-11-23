import binascii

MODE = '100644'


class Tree:
    def __init__(self, entries):
        self.entries = entries
        self.hash = None
        self.type = "tree"

    def __str__(self):
        entries = sorted(self.entries, key=lambda x: x.name)

        formatted_entries = [
            MODE + ' ' + entry.name + '\0' +
            str(hex_string_to_bytes(entry.hash))

            for entry in entries
        ]
        self.entries = "".join(formatted_entries)
        return self.entries

    def __len__(self):
        return len(self.entries)


def hex_string_to_bytes(hex_string):
    # Check if the input is a valid hexadecimal string
    if len(hex_string) % 2 != 0 or not all(c in '0123456789abcdefABCDEF' for c in hex_string):
        raise ValueError("Invalid hexadecimal string")

    # Iterate through the string, extract pairs of digits, and convert them to bytes
    byte_list = [int(hex_string[i:i+2], 16).to_bytes(1, byteorder='big')
                 for i in range(0, len(hex_string), 2)]

    # Concatenate the list of bytes into a bytes object
    result_bytes = b''.join(byte_list)

    return result_bytes
