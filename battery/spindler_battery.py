from datetime import timedelta
from objects.battery import Battery

class SpindlerBattery(Battery):

    def __init__(self,last_service_date):
        super().__init__(last_service_date,timedelta(years = 2))
        self._last_service_date = last_service_date
        self._service_interval = timedelta(years=2)

    def needs_service(self):
        return Battery.needs_service(self)