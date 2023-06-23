# from abc import ABC
# from datetime import datetime, timedelta
# from objects.serviceable import Serviceable
#
#
# class Battery(Serviceable, ABC):
#     # abstract class for a battery
#     def __int__(self, last_service_date, service_interval):
#         self._last_service_date = last_service_date
#         self._service_interval = service_interval
#
#     def needs_service(self):
#         # determines if car needs service
#         result = False
#         next_service_date = self._last_service_date + self._service_interval
#         if datetime.today().date() >= next_service_date:
#             result = True
#         return result

from abc import ABC
from datetime import datetime, timedelta
from objects.serviceable import Serviceable


class Battery(Serviceable, ABC):
    # abstract class for a battery
    def __init__(self, last_service_date, service_interval):
        self._last_service_date = last_service_date
        self._service_interval = service_interval

    def needs_service(self):
        # determines if car needs service
        # result = False
        next_service_date = self._last_service_date + self._service_interval
        if datetime.today().date() >= next_service_date:
            return True
        return False
