from abc import ABC
from objects.serviceable import Serviceable


class Engine(Serviceable, ABC):
    """abstract class for engine"""
