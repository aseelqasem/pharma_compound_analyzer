import json
import os

DATA_FILE = os.path.join("data", "compounds.json")

def load_compounds():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_compounds(compounds):
    with open(DATA_FILE, "w") as f:
        json.dump(compounds, f, indent=4)
