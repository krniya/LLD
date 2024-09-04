from .vehicle import Vehicle
from .vehicle_type import VehicleType


class Car(Vehicle):
    def __init__(self, vehicle_number, color):
        super().__init__(VehicleType.CAR, vehicle_number, color)
