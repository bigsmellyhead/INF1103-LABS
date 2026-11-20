import csv
from inventory import Inventory
from product_factory import ProductFactory
from supplier import Supplier


def load_products(path: str, inventory: Inventory, supplier: Supplier) -> None:
    loaded: int = 0  # how many products were added
    try:
        file = open(path, newline="")
    except FileNotFoundError:
        print(f"Products file not found: {path}")
    else:
        with file:
            reader = csv.reader(file)
            next(reader, None)  # skip the header row
            for row in reader:
                try:
                    product_type, product_id, name, price, stock, extra = row
                    product = ProductFactory.create(product_type, product_id, name,
                                                    float(price), int(stock), supplier, float(extra))
                    if inventory.add_product(product):
                        loaded += 1
                    else:
                        print(f"Skipping row {row}: duplicate product ID.")
                except ValueError as e:
                    print(f"Skipping row {row}: {e}")
        print(f"{loaded} products loaded.")
    finally:
        print("Load attempt finished.")