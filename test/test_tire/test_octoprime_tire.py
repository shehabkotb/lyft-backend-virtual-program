import unittest
from tire import OctoprimeTire

class TestOctoprimeTire(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        wear_array = [0.9, 0.9, 0.9, 0.3]

        tire = OctoprimeTire(wear_array)
        self.assertTrue(tire.needs_service())

    def test_battery_should_not_be_serviced(self):
        tire = [0.9, 0.9, 0.9, 0.2]

        tire = OctoprimeTire(tire)
        self.assertFalse(tire.needs_service())