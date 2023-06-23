import unittest
from datetime import date, timedelta
from objects.battery import Battery
from battery.spindler_battery import SpindlerBattery


class TestNubbinBattery(unittest.TestCase):
    def test_needs_service_false(self):
        last_service_date = date(2016,1, 25)
        battery = SpindlerBattery(last_service_date)
        # current_date = date(2020, 5, 15)
        # battery.current_date = current_date
        self.assertTrue(battery.needs_service())

    def test_needs_service_boundary(self):
        last_service_date = date(2022, 1, 10)
        battery = SpindlerBattery(last_service_date)
        # current_date = date(2020,5,15)
        # battery.current_date = current_date
        self.assertFalse(battery.needs_service())


if __name__ == '__main__':
    unittest.main()