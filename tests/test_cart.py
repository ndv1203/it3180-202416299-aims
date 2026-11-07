import unittest
from aims.cart import Cart
from aims.dvd import DigitalVideoDisc


class TestCart(unittest.TestCase):
    def test_add_dvd_until_full(self):
        cart = Cart()
        for i in range(20):
            self.assertTrue(cart.add_dvd(DigitalVideoDisc(f"DVD {i}")))
        self.assertFalse(cart.add_dvd(DigitalVideoDisc("DVD 21")))

    def test_remove_dvd(self):
        cart = Cart()
        dvd = DigitalVideoDisc("The Lion King", cost=19.95)
        cart.add_dvd(dvd)
        self.assertTrue(cart.remove_dvd(dvd))
        self.assertFalse(cart.remove_dvd(dvd))

    def test_total_cost_with_discount(self):
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("Test DVD", cost=100.0))
        self.assertAlmostEqual(cart.total_cost_with_discount(20), 80.0)

    def test_discount_invalid_percent(self):
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("Test DVD", cost=100.0))
        with self.assertRaises(ValueError):
            cart.total_cost_with_discount(150)

    def test_sort_by_title(self):
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("Star Wars", cost=24.95))
        cart.add_dvd(DigitalVideoDisc("Aladdin", cost=18.99))
        cart.sort_by_title()
        self.assertEqual([d.title for d in cart.items], ["Aladdin", "Star Wars"])

    def test_sort_by_cost(self):
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("Aladdin", cost=18.99))
        cart.add_dvd(DigitalVideoDisc("Star Wars", cost=24.95))
        cart.sort_by_cost()
        self.assertEqual([d.title for d in cart.items], ["Star Wars", "Aladdin"])


if __name__ == "__main__":
    unittest.main()
