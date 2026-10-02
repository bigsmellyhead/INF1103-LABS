import json
import os

FILENAME = "inventory.json"

def load_inventory():
    """Checks whether inventory.json exists. Loads it if present, otherwise begins with an empty inventory."""
    if os.path.exists(FILENAME):
        try:
            with open(FILENAME, "r") as file:
                print("inventory.json found.")
                print("Inventory loaded successfully.")
                return json.load(file)
        except json.JSONDecodeError:
            print("Error reading inventory file. Starting with empty inventory.")

    # Begin with an empty inventory if file does not exist
    return []