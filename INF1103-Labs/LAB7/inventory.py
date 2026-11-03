#inventory.py - to collect product objects

from product import Product

class Inventory:

    def __init__(self):
        self.__products = []

    def add_product(self, product):
        if self.search_product(product.get_product_id()) is not None:
            return False
        self.__products.append(product)
        return True

    def search_product(self, product_id):
        for product in self.__products:
            if product.get_product_id().lower() == product_id.lower():
                return product
        return None

    def display_all(self):
        print("\nCurrent Inventory")
        for product in self.__products:
            print("-" * 47)
            product.display_information()
            print("-" * 47)

    def get_all_products(self):
        return list(self.__products)