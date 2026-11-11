from product import Product
from order_line import OrderLine


class Order:

    def __init__(self, order_id: str) -> None:
        self.__order_id: str = order_id
        self.__order_lines: list[OrderLine] = []

    def get_order_id(self) -> str:
        return self.__order_id

    def get_order_lines(self) -> list[OrderLine]:
        return list(self.__order_lines)

    def add_order_line(self, product: Product, quantity: int) -> None:
        order_line = OrderLine(product, quantity) 
        self.__order_lines.append(order_line)

    def remove_order_line(self, product_id: str) -> bool:
        for line in self.__order_lines:
            if line.get_product().get_product_id().lower() == product_id.lower():
                self.__order_lines.remove(line)
                return True
        return False

    def calculate_total(self) -> float:
        total: float = 0.0
        for line in self.__order_lines:
            total += line.calculate_subtotal()
        return total

    def display_order(self) -> None:
        print(f"\nOrder {self.__order_id}")
        for line in self.__order_lines:
            name = line.get_product().get_name()
            print(f"{name} x {line.get_quantity()} = ${line.calculate_subtotal():.2f}")
        print(f"Total: ${self.calculate_total():.2f}")
