import json


def load_json(json_file):
    with open(json_file) as data:
        return json.load(data)


def dump_json(entries, json_file):
    with open(json_file, 'w') as handler:
        json.dump(entries, handler)


def write_in_txt(fname, content):
    with open(fname, 'w', encoding='utf-8') as handler:
        handler.write(content)
    print('Success')
