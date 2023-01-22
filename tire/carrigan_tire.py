from .tire import Tire

class CarriganTire(Tire):
    def __init__(self, wear_array):
        self.wear_array = wear_array

    def needs_service(self):
        for x in self.wear_array:
            if x >= 0.9:
                return True
        return False