import unittest
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from product_factory import ProductFactory
from supplier import Supplier

SUPPLIER = Supplier("S001", "Test Supplier", "test@example.com")


class TestProductFactory(unittest.TestCase):

    def test_creates_physical(self):
        p = ProductFactory.create("physical", "P1", "Lamp", 25.0, 10, SUPPLIER, 2.5)
        self.assertIsInstance(p, PhysicalProduct)

    def test_creates_digital(self):
        d = ProductFactory.create("digital", "D1", "App", 9.9, 5, SUPPLIER, 120)
        self.assertIsInstance(d, DigitalProduct)

    def test_unknown_type_raises(self):
        with self.assertRaisesRegex(ValueError, "Unknown product type: service"):
            ProductFactory.create("service", "S1", "Install", 30.0, 5, SUPPLIER, 0)


if __name__ == "__main__":
    unittest.main()