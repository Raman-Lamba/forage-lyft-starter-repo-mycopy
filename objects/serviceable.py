from abc import ABC, abstractmethod


class Serviceable(ABC):
    # abstract class for a serviceable object
    @abstractmethod
    def needs_service(self):
        pass  # determines if the object needs service
