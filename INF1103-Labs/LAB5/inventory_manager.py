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

def display_all(inventory):
    """Display all products currently in the inventory."""
    print("\nCurrent Inventory")
    for item in inventory:
        print(f"ID: {item['id']} | Name: {item['name']} | Price: ${item['price']:.2f} | Stock: {item['stock']}")

def add_product(inventory):
    """Add a new product dictionary to the inventory list."""
    print("\nAdd New Product")
    prod_id = input("Product ID: ").strip()

    for item in inventory:
        if item['id'].lower() == prod_id.lower():
            print("Error: Product ID already exists!")
            return

    name = input("Product Name: ").strip()
    try:
        price = float(input("Price: "))
        stock = int(input("Stock Quantity: "))
    except ValueError:
        print("Invalid input for price or stock.")
        return

    new_product = {
        "id": prod_id,
        "name": name,
        "price": price,
        "stock": stock
    }
    inventory.append(new_product)
    print("Product added successfully!")