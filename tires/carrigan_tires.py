from objects.tires import Tires

class CarriganTires(Tires):
    def __init__(self,tire_status):
        self.tire_status = tire_status

    def needs_service(self):
        result = False
        for x in self.tire_status:
            if x >= 0.9:
                result = True
                break
        return result
