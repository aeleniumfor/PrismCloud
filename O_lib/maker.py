import uuid
from os import path


def make_uuid(file_name):
    name = path.splitext(file_name)
    UUID = str(uuid.uuid4())[::-1]
    remake_file_name = UUID + name[1]
    return remake_file_name
