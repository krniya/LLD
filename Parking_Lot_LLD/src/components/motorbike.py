from .vehicle import Vehicle
from .vehicle_type import VehicleType


class Motorbike(Vehicle):
    def __init__(self, vehicle_number, color):
        super().__init__(VehicleType.MOTORBIKE, vehicle_number, color)
