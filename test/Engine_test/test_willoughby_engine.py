import unittest
from datetime import datetime, timedelta

from engine.willoughby_engine import WilloughbyEngine


class TestCapuletEngine(unittest.TestCase):
    def test_should_be_serviced(self):
        curr_mileage = 60001
        l_s_m = 0
        engine1 = WilloughbyEngine(curr_mileage, l_s_m)
        self.assertTrue(engine1.needs_service())
    def test_shouldnot_be_serviced(self):
        current_mileage = 60000
        last_service_mileage = 0
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())

if __name__ == '__main__':
    unittest.main()