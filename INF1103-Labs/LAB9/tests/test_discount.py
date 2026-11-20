import unittest
from order import Order
from physical_product import PhysicalProduct
from supplier import Supplier
from discount_strategy import DiscountStrategy
from percentage_discount import PercentageDiscount
from bulk_discount import BulkDiscount
from student_discount import StudentDiscount

SUPPLIER = Supplier("S001", "Test Supplier", "test@example.com")


def make_order(price: float, discount=None) -> Order:
    order = Order("O1", discount)
    order.add_order_line(PhysicalProduct("P1", "Item", price, 10, SUPPLIER, 1.0), 1)
    return order


class HalfOff(DiscountStrategy):  # a new strategy, defined without changing Order
    def apply(self, total: float) -> float:
        return total / 2


class TestDiscounts(unittest.TestCase):

    def test_no_discount_by_default(self):
        self.assertAlmostEqual(make_order(250).calculate_total(), 250)

    def test_percentage_discount(self):
        self.assertAlmostEqual(make_order(100, PercentageDiscount(10)).calculate_total(), 90)

    def test_bulk_discount_at_and_below_threshold(self):
        self.assertAlmostEqual(make_order(250, BulkDiscount(200, 20)).calculate_total(), 230)
        self.assertAlmostEqual(make_order(200, BulkDiscount(200, 20)).calculate_total(), 180)
        self.assertAlmostEqual(make_order(199, BulkDiscount(200, 20)).calculate_total(), 199)

    def test_set_discount_changes_strategy(self):
        order = make_order(250, BulkDiscount(200, 20))
        self.assertAlmostEqual(order.calculate_total(), 230)
        order.set_discount(PercentageDiscount(10))
        self.assertAlmostEqual(order.calculate_total(), 225)

    def test_student_discount(self):
        self.assertAlmostEqual(make_order(100, StudentDiscount()).calculate_total(), 95)

    def test_new_strategy_without_changing_order(self):
        self.assertAlmostEqual(make_order(100, HalfOff()).calculate_total(), 50)

    def test_invalid_percentage_rejected(self):
        with self.assertRaises(ValueError):
            PercentageDiscount(150)


if __name__ == "__main__":
    unittest.main()