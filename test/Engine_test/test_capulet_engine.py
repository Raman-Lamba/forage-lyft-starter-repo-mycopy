import unittest
from datetime import datetime, timedelta

from engine.capulet_engine import CapuletEngine


class TestCapuletEngine(unittest.TestCase):
    def test_should_be_serviced(self):
        curr_mileage = 30001
        l_s_m = 0
        engine1 = CapuletEngine(curr_mileage, l_s_m)
        self.assertTrue(engine1.needs_service())
    def test_shouldnot_be_serviced(self):
        current_mileage = 30000
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())

if __name__ == '__main__':
    unittest.main()