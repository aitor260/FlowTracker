import json

def write_json(path, data):
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)

def read_json(path):
    try:
        with open(path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []