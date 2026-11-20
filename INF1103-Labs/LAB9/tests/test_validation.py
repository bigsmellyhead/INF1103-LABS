import csv
import io
import os
import tempfile
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch
from inventory import Inventory
from order_line import OrderLine
from physical_product import PhysicalProduct
from input_helpers import get_positive_float
from product_loader import load_products
from supplier import Supplier

SUPPLIER = Supplier("S001", "Test Supplier", "test@example.com")


class TestValidation(unittest.TestCase):

    def test_zero_price_rejected(self):
        with self.assertRaises(ValueError):
            PhysicalProduct("P1", "Lamp", 0, 10, SUPPLIER, 1.0)

    def test_negative_stock_rejected(self):
        with self.assertRaises(ValueError):
            PhysicalProduct("P1", "Lamp", 10, -1, SUPPLIER, 1.0)

    def test_zero_order_quantity_rejected(self):
        product = PhysicalProduct("P1", "Lamp", 10, 5, SUPPLIER, 1.0)
        with self.assertRaises(ValueError):
            OrderLine(product, 0)

    def test_input_helper_retries_until_valid(self):
        with patch("builtins.input", side_effect=["abc", "-5", "12.50"]), redirect_stdout(io.StringIO()):
            self.assertEqual(get_positive_float("Price: "), 12.5)

    def test_missing_file_does_not_crash(self):
        with redirect_stdout(io.StringIO()) as out:
            load_products("does_not_exist.csv", Inventory(), SUPPLIER)
        self.assertIn("not found", out.getvalue())

    def test_bad_rows_skipped_good_rows_load(self):
        rows = [
            ["product_type", "product_id", "name", "price", "stock_quantity", "extra"],
            ["physical", "P001", "Lamp", "25.00", "10", "2.5"],
            ["service", "S001", "Install", "30.00", "5", "0"],
            ["physical", "P002", "Chair", "abc", "3", "12"],
            ["digital", "D001", "App", "49.90", "100", "120"],
        ]
        with tempfile.NamedTemporaryFile("w", suffix=".csv", delete=False, newline="") as f:
            csv.writer(f).writerows(rows)
            path = f.name
        try:
            inventory = Inventory()
            with redirect_stdout(io.StringIO()):
                load_products(path, inventory, SUPPLIER)
            self.assertEqual(len(inventory.get_all_products()), 2)
        finally:
            os.remove(path)


if __name__ == "__main__":
    unittest.main()