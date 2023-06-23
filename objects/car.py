from abc import ABC, abstractmethod
from objects.serviceable import Serviceable

class Car(Serviceable):
    def __init__(self,engine, battery,tires):
        # self.last_service_date = last_service_date
        self.engine = engine
        self.battery = battery
        self.tires = tires

    @abstractmethod
    def needs_service(self):
        return self.engine.need_service() or self.battery.need_service() or self.tires.needs_service()
