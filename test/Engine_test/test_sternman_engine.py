import unittest
from datetime import datetime, timedelta

from engine.sternman_engine import SternmanEngine


class TestCapuletEngine(unittest.TestCase):
    def test_should_be_serviced(self):
        warning_light_is_on = True
        engine1 = SternmanEngine(warning_light_is_on)
        self.assertTrue(engine1.needs_service())
    def test_shouldnot_be_serviced(self):
        warning_light_is_on = False
        engine1 = SternmanEngine(warning_light_is_on)
        self.assertFalse(engine1.needs_service())

if __name__ == '__main__':
    unittest.main()