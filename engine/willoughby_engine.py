from abc import ABC

from objects.car import Car


class WilloughbyEngine(Car, ABC):
    def __init__(self,  current_mileage, last_service_mileage):
        super().__init__(last_service_mileage)
        self._current_mileage = current_mileage
        self._service_interval = 60000
        self._last_service_mileage = last_service_mileage

    # def engine_should_be_serviced(self):
    #     return self.current_mileage - self.last_service_mileage > 60000
    def needs_service(self):
        result = False
        if(self._current_mileage % self._service_interval) >= 0:
            self._last_service_mileage= self._current_mileage
            result = True
        return result