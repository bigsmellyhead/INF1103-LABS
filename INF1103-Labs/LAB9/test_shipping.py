from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from can_be_shipped import CanBeShipped

SUPPLIER = Supplier("S001", "Josh Tech LOL", "josh@tech.lol")


def test_shipping_cost_depends_on_weight():
    light = PhysicalProduct("P1", "Pen", 2.00, 100, SUPPLIER, 0.5)
    medium = PhysicalProduct("P2", "Laptop", 1200.00, 15, SUPPLIER, 2.0)
    heavy = PhysicalProduct("P3", "Desk", 300.00, 5, SUPPLIER, 10.0)

    print("Light (0.5 kg) shipping:", light.calculate_shipping_cost())
    print("Medium (2.0 kg) shipping:", medium.calculate_shipping_cost())
    print("Heavy (10.0 kg) shipping:", heavy.calculate_shipping_cost())

    assert light.calculate_shipping_cost() == 6.00
    assert medium.calculate_shipping_cost() == 9.00
    assert heavy.calculate_shipping_cost() == 25.00
    assert light.get_supplier() is SUPPLIER
    print("PASS: heavier products cost more to ship, and the supplier is stored")


def test_physical_product_is_shippable():
    chair = PhysicalProduct("P4", "Chair", 80.00, 8, SUPPLIER, 7.0)
    assert isinstance(chair, CanBeShipped)
    print("PASS: PhysicalProduct implements CanBeShipped")


def test_digital_product_is_not_shippable():
    ebook = DigitalProduct("D1", "eBook", 10.00, 999, SUPPLIER, 5.0)
    assert not isinstance(ebook, CanBeShipped)
    assert not hasattr(ebook, "calculate_shipping_cost")
    print("PASS: DigitalProduct is not shippable")


def test_interface_cannot_be_instantiated():
    try:
        CanBeShipped()
        print("FAIL: CanBeShipped was created directly")
    except TypeError as error:
        print("PASS: CanBeShipped cannot be instantiated:", error)


if __name__ == "__main__":
    test_shipping_cost_depends_on_weight()
    test_physical_product_is_shippable()
    test_digital_product_is_not_shippable()
    test_interface_cannot_be_instantiated()