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

def save_inventory(inventory, exit_mode=False):
    """Save the current inventory list to inventory.json."""
    if exit_mode:
        print("\nSaving inventory before exit...")
    else:
        print("\nSaving inventory...")

    try:
        with open(FILENAME, "w") as file:
            json.dump(inventory, file, indent=4)
        if exit_mode:
            print("Inventory saved successfully.")
        else:
            print("Inventory saved successfully to inventory.json.")
    except Exception as e:
        print(f"Error saving inventory: {e}")
        
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

def update_stock(inventory):
    """Update the stock level of an existing product."""
    print("\nUpdate Stock")
    prod_id = input("Enter Product ID: ").strip()

    for item in inventory:
        if item['id'].lower() == prod_id.lower():
            print(f"\nProduct Found:")
            print(f"Name: {item['name']}")
            print(f"Current Stock: {item['stock']}")
            try:
                new_stock = int(input("\nNew Stock Quantity: "))
                item['stock'] = new_stock
                print("\nStock updated successfully!")
            except ValueError:
                print("Invalid stock quantity entered.")
            return

    print("Product not found.")

def search_product(inventory):
    """Search for a product by ID."""
    print("\nSearch Product")
    prod_id = input("Enter Product ID: ").strip()

    found = False
    for item in inventory:
        if item['id'].lower() == prod_id.lower():
            print("\nProduct Found")
            print("-" * 47)
            print(f"ID: {item['id']}\nName: {item['name']}\nPrice: ${item['price']:.2f}\nStock: {item['stock']}")
            print("-" * 47)
            found = True
            break

    if not found:
        print("\nProduct not found.")

def main():
    print("===================================================")
    print("INVENTORY MANAGEMENT SYSTEM")
    print("===================================================")
    print()

    inventory = load_inventory()

    while True:
        print("\nMENU")
        print("1. Display All Products")
        print("2. Add Product")
        print("3. Update Stock")
        print("4. Search Product")
        print("5. Save Inventory")
        print("6. Exit")

        choice = input("\nEnter option: ").strip()

        if choice == "1":
            display_all(inventory)
        elif choice == "2":
            add_product(inventory)
        elif choice == "3":
            update_stock(inventory)
        elif choice == "4":
            search_product(inventory)
        elif choice == "5":
            save_inventory(inventory, exit_mode=False)
        elif choice == "6":
            save_inventory(inventory, exit_mode=True)
            print("\nThank you for using Inventory Management System.")
            print("Program terminated.")
            break
        else:
            print("\nInvalid option. Please choose between 1 and 6.")

if __name__ == "__main__":
    main()