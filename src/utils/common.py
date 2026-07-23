import yaml
import joblib
import os
from pathlib import Path

def read_yaml(path: Path) ->dict:
    
    with open(path, "r") as file:
        return yaml.safe_load(file)

def save_object(file_path, obj):

    dir_path = os.path.dirname(file_path)
    os.makedirs(dir_path, exist_ok=True)
    joblib.dump(obj, file_path)
    