import unittest
from tire import CarriganTire

class TestCarriganTire(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        wear_array = [0.8, 0.9, 0.1, 0.3]

        tire = CarriganTire(wear_array)
        self.assertTrue(tire.needs_service())

    def test_battery_should_not_be_serviced(self):
        tire = [0.8, 0.89, 0.1, 0.3]

        tire = CarriganTire(tire)
        self.assertFalse(tire.needs_service())