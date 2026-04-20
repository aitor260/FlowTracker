import json
from pathlib import Path

def write_json(path, data):
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)

def read_json(path):
    try:
        with open(path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def create_project_structure():
    root = Path.cwd()

    project_dir = root / ".ft_project"
    data_dir = project_dir / "data"
    
    data_dir.mkdir(parents=True, exist_ok=True)

    (project_dir / "ft_project.json").touch(exist_ok=True)
    return 0