from battery import nubbin_battery, spindler_battery
from engine import capulet_engine, willoughby_engine, sternman_engine
from tires import carrigan_tires, octoprime_tires
from objects import car

class CarFactory:
    """A factory for cars"""

    @classmethod
    def create_calliope(cls, last_service_date, current_mileage, last_service_mileage, tire_status):
        """Creates a Calliope car"""
        engine = capulet_engine.CapuletEngine(last_service_mileage, current_mileage)
        battery = spindler_battery.SpindlerBattery(last_service_date)
        tires = carrigan_tires.CarriganTires(tire_status)
        car1 = car.Car(engine, battery, tires)
        return car1

    @classmethod
    def create_glissade(cls, last_service_date, current_mileage, last_service_mileage, tire_status):
        """Creates a Glissade car"""
        engine = willoughby_engine.WilloughbyEngine(
            last_service_mileage, current_mileage)
        battery = spindler_battery.SpindlerBattery(last_service_date)
        tires = carrigan_tires.CarriganTires(tire_status)
        car1 = car.Car(engine, battery, tires)
        return car1

    @classmethod
    def create_palindrome(cls, last_service_date, warning_light_on, tire_status):
        """Creates a Palindrome car"""
        engine = sternman_engine.SternmanEngine(warning_light_on)
        battery = spindler_battery.SpindlerBattery(last_service_date)
        tires = octoprime_tires.OctoprimeTires(tire_status)
        car1 = car.Car(engine, battery, tires)
        return car1

    @classmethod
    def create_rorschach(cls, last_service_date, current_mileage, last_service_mileage, tire_status):
        """Creates a Rorschach car"""
        engine = willoughby_engine.WilloughbyEngine(
            last_service_mileage, current_mileage)
        battery = nubbin_battery.NubbinBattery(last_service_date)
        tires = octoprime_tires.OctoprimeTires(tire_status)
        car1 = car.Car(engine, battery, tires)
        return car1

    @classmethod
    def create_thovex(cls, last_service_date, current_mileage, last_service_mileage, tire_status):
        """Creates a Thovex car"""
        engine = capulet_engine.CapuletEngine(last_service_mileage, current_mileage)
        battery = nubbin_battery.NubbinBattery(last_service_date)
        tires = carrigan_tires.CarriganTires(tire_status)
        car1 = car.Car(engine, battery, tires)
        return car1
