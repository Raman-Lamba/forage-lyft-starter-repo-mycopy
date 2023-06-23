from abc import ABC

from objects.serviceable import Serviceable

class Tires(Serviceable,ABC):
    def __init__(self,tire_status):
        self.tire_status = tire_status

