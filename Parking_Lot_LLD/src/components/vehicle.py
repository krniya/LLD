from abc import ABC


class Vehicle(ABC):
    def __init__(self, vehicle_type, vehicle_number, color):
        self.vehicle_type = vehicle_type
        self.vehicle_number = vehicle_number
        self.color = color

    def get_vehicle_type(self):
        return self.vehicle_type

    def get_vehicle_number(self):
        return self.vehicle_number

    def get_color(self):
        return self.color
