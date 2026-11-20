#inventory.py - to collect product objects

from product import Product


class Inventory:

    def __init__(self) -> None:
        self.products: list[Product] = []  # the inventory holds product references

    def add_product(self, product: Product) -> bool:
        if self.find_product(product.get_product_id()) is not None:
            return False
        self.products.append(product)
        return True

    def remove_product(self, product_id: str) -> bool:
        product = self.find_product(product_id)
        if product is None:
            return False
        self.products.remove(product)  # removes the reference only, not the product
        return True

    def find_product(self, product_id: str) -> Product | None:
        for product in self.products:
            if product.get_product_id().lower() == product_id.lower():
                return product
        return None

    def display_all(self) -> None:
        print("\nCurrent Inventory")
        for product in self.products:
            print("-" * 47)
            product.display_information()
            print("-" * 47)

    def get_all_products(self) -> list[Product]:
        return list(self.products)
