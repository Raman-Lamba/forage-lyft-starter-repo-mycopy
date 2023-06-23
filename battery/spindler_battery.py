# from datetime import timedelta
# from objects.battery import Battery
#
# class SpindlerBattery(Battery):
#
#     def __init__(self,last_service_date):
#         super().__init__(last_service_date,timedelta(years = 2))
#         self._last_service_date = last_service_date
#         self._service_interval = timedelta(years=2)
#
#     def needs_service(self):
#         return Battery.needs_service

from objects.battery import Battery
from datetime import timedelta


class SpindlerBattery(Battery):
    def __init__(self, last_service_date):
        service_interval = timedelta(days=3 * 365)  # Equivalent of 3 years in days
        super().__init__(last_service_date, service_interval)
        self._last_service_date = last_service_date
        self._service_interval = service_interval

    def needs_service(self):
        res = super().needs_service()
        return res