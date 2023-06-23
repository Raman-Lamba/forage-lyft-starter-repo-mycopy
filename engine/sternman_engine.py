from abc import ABC

from objects.engine import Engine


class SternmanEngine(Engine):
    def __init__(self, warning_light_is_on):
        # super().__init_last_service_date)
        self._warning_light_is_on = warning_light_is_on

    # def engine_should_be_serviced(self):
    #     if self.warning_light_is_on:
    #         return True
    #     else:
    #         return False
    def needs_service(self):
        return self._warning_light_is_on