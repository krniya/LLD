from .vehicle import Vehicle
from .vehicle_type import VehicleType


class Truck(Vehicle):
    def __init__(self, vehicle_number, color):
        super().__init__(VehicleType.TRUCK, vehicle_number, color)
