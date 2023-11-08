import hashlib
import utils


def calculate_header(size):
    return b"sgit " + utils.HEADER_SPLIT_CHAR + b''


def hash_object(object):
    content = None
    if utils.is_file_path(object):
        with open(object, 'rb') as file:
            content = file.read()
    else:
        content = object

    size = utils.calculate_size(content)
    header = calculate_header(size)

    to_hash = header + utils.CONTENT_AND_HEADER_SPLIT_CHAR + content

    return hashlib.sha1(to_hash).hexdigest(), content


def see_contents(hash):
    pass
