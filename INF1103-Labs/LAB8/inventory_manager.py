import json
import os
from product import Product
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from inventory import Inventory
from supplier import Supplier

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILENAME = os.path.join(BASE_DIR, "inventory.json")

# Supplier object examples to supply to the product
SUPPLIERS: dict[str, Supplier] = {
    "S001": Supplier("S001", "Josh Tech LOL", "josh@tech.lol"),
    "S002": Supplier("S002", "One Piece IS REAL", "one@piece.is.real"),
}


def product_to_dict(product: Product) -> dict:
    """Converts product object to a dictionary, including the type and attributes"""
    data = {
        "id": product.get_product_id(),
        "name": product.get_name(),
        "price": product.get_price(),
        "stock": product.get_stock(),
        "supplier_id": product.get_supplier().get_supplier_id()
    }
    if isinstance(product, PhysicalProduct):
        data["type"] = "physical"
        data["weight"] = product.get_weight()
    elif isinstance(product, DigitalProduct):
        data["type"] = "digital"
        data["download_size"] = product.get_download_size()
    return data


def dict_to_product(item: dict, suppliers: dict[str, Supplier]) -> Product | None:
    """Uses the saved type to create the correct subclass. Returns None if type is unknown or missing."""
    supplier = suppliers.get(item.get("supplier_id"))
    if supplier is None:
        return None
    product_type = item.get("type")
    if product_type == "physical":
        return PhysicalProduct(item["id"], item["name"], item["price"], item["stock"], supplier, item["weight"])
    if product_type == "digital":
        return DigitalProduct(item["id"], item["name"], item["price"], item["stock"], supplier, item["download_size"])
    return None


def load_inventory():
    inventory = Inventory()
    if os.path.exists(FILENAME):
        try:
            with open(FILENAME, "r") as file:
                print("inventory.json found.")
                data = json.load(file)
            for item in data:
                product = dict_to_product(item, SUPPLIERS)
                if product is None:
                    print(f"Skipping product {item.get('id')}: missing or unknown 'type' or supplier_id.")
                else:
                    inventory.add_product(product)
            print("Inventory loaded successfully.")
        except json.JSONDecodeError:
            print("Error reading inventory file. Starting with empty inventory.")
    return inventory

def save_inventory(inventory, exit_mode=False):
    """Save the current inventory list to inventory.json."""
    if exit_mode:
        print("\nSaving inventory before exit...")
    else:
        print("\nSaving inventory...")

    data = [product_to_dict(product) for product in inventory.get_all_products()]

    try:
        with open(FILENAME, "w") as file:
            json.dump(data, file, indent=4)
        if exit_mode:
            print("Inventory saved successfully.")
        else:
            print("Inventory saved successfully to inventory.json.")
    except Exception as e:
        print(f"Error saving inventory: {e}")

def add_product(inventory):
    """Add a new product dictionary to the inventory list."""
    print("\nAdd New Product")
    prod_id = input("Product ID: ").strip()

    if inventory.find_product(prod_id) is not None:
        print("Error: Product ID already exists!")
        return

    name = input("Product Name: ").strip()
    try:
        price = float(input("Price: "))
        stock = int(input("Stock Quantity: "))
    except ValueError:
        print("Invalid input for price or stock.")
        return

    print("\nAvailable Suppliers")
    for supplier_id, supplier in SUPPLIERS.items():
        print(f"{supplier_id}: {supplier.get_name()}")
    supplier = SUPPLIERS.get(input("Choose supplier ID: ").strip())
    if supplier is None:
        print("Invalid supplier ID.")
        return

    print("\nProduct Type")
    print("1. Physical")
    print("2. Digital")
    choice = input("Choose type: ").strip()

    try:
        if choice == "1":
            weight = float(input("Weight (kg): "))
            product = PhysicalProduct(prod_id, name, price, stock, supplier, weight)
        elif choice == "2":
            download_size = float(input("Download Size (MB): "))
            product = DigitalProduct(prod_id, name, price, stock, supplier, download_size)
        else:
            print("Invalid product type.")
            return
    except ValueError:
        print("Invalid input for weight or download size.")
        return

    inventory.add_product(product)
    print("Product added successfully!")

def update_stock(inventory):
    """Update the stock level of an existing product."""
    print("\nUpdate Stock")
    prod_id = input("Enter Product ID: ").strip()

    product = inventory.find_product(prod_id)
    if product is None:
        print("Product not found.")
        return

    print("\nProduct Found:")
    print(f"Name: {product.get_name()}")
    print(f"Current Stock: {product.get_stock()}")
    try:
        new_stock = int(input("\nNew Stock Quantity: "))
        product.update_stock(new_stock)
        print("\nStock updated successfully!")
    except ValueError:
        print("Invalid stock quantity entered.")

def search_product(inventory):
    """Search for a product by ID."""
    print("\nSearch Product")
    prod_id = input("Enter Product ID: ").strip()

    product = inventory.find_product(prod_id)
    if product is None:
        print("\nProduct not found.")
        return

    print("\nProduct Found")
    print("-" * 47)
    product.display_information()
    print("-" * 47)

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
            inventory.display_all()
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