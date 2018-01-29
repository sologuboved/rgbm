import json
from global_vars import *


def load_json(json_file):
    with open(json_file) as data:
        return json.load(data)


def dump_json(entries, json_file):
    with open(json_file, 'w') as handler:
        json.dump(entries, handler)


def prettyprint(books):
    index = 1
    for book in books:
        print(index)
        index += 1
        print(AUTHOR + ':', book[AUTHOR])
        print(TITLE + ':', book[TITLE])
        print()
