#product.py - to represent one product

from abc import ABC, abstractmethod

class Product(ABC):

    def __init__(self, product_id, name, price, stock):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock

    def get_product_id(self):
        return self.__product_id

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_stock(self):
        return self.__stock

    def update_stock(self, quantity):
        if quantity < 0:
            raise ValueError("Stock cannot be negative.")
        self.__stock = quantity

    def display_information(self):
        print(f"ID: {self.__product_id}\nName: {self.__name}\nPrice: ${self.__price:.2f}\nStock: {self.__stock}")

@abstractmethod
def get_fulfilment_info(self):
    pass