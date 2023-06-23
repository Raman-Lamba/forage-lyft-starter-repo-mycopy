# from datetime import timedelta
# from dateutil.relativedelta import relativedelta
# from objects.battery import Battery
#
#
# class NubbinBattery(Battery):
#
#     def __init__(self, last_service_date):
#         service_interval = relativedelta(years = 4)
#         super().__init__(last_service_date,relativedelta(years = 4))
#         self._last_service_date = last_service_date
#         self._service_interval = service_interval
#
#     def needs_service(self):
#         return Battery.needs_service()

# from objects.battery import Battery
# from datetime import timedelta
#
#
# class NubbinBattery(Battery):
#     def __init__(self, last_service_date):
#         super().__init__(last_service_date, timedelta(years=4))
#         self._last_service_date = last_service_date
#         self._service_interval = timedelta(years=4)
#
#     def needs_service(self):
#         return super().needs_service()
from objects.battery import Battery
from datetime import timedelta


class NubbinBattery(Battery):
    def __init__(self, last_service_date):
        service_interval = timedelta(days=4 * 365)  # Equivalent of 4 years in days
        super().__init__(last_service_date, service_interval)
        self._last_service_date = last_service_date
        self._service_interval = service_interval

    def needs_service(self):
        res = super().needs_service()
        return res