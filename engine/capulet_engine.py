from abc import ABC

from objects.car import Car


class CapuletEngine(Car, ABC):
    def __init__(self, current_mileage, last_service_mileage):
        self._current_mileage = current_mileage
        self._service_interval = 30000
        self._last_service_mileage = last_service_mileage

    # def engine_should_be_serviced(self):
    #     return self.current_mileage - self.last_service_mileage > 30000
    def needs_service(self):
        result = False
        if(self._current_mileage % self._service_interval) >= 0:
            result = True
            self._last_service_mileage = self._current_mileage
        return result
