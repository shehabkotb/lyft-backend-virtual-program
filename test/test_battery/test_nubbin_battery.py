import unittest
from datetime import datetime
from battery import NubbinBattery

class TestNubbinBattery(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today()
        last_service_date = today.replace(year=today.year - 5)

        battery = NubbinBattery(last_service_date, today)
        self.assertTrue(battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today()
        last_service_date = today.replace(year=today.year - 2)

        battery = NubbinBattery(last_service_date, today)
        self.assertFalse(battery.needs_service())