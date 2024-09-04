class ParkingSpot:
    def __init__(self, spot_number, vehicle_type):
        self.spot_number = spot_number
        self.vehicle_type = vehicle_type
        self.is_occupied = False
        self.vehicle = None

    def is_occupied(self):
        return self.is_occupied

    def get_vehicle(self):
        return self.vehicle

    def unpark_vehicle(self):
        self.is_occupied = False
        self.vehicle = None

    def get_spot_number(self):
        return self.spot_number

    def is_available(self):
        return not self.is_occupied

    def get_vehicle_type(self):
        return self.vehicle_type

    def park_vehicle(self, vehicle):
        if self.is_available() and vehicle.get_vehicle_type() == self.vehicle_type:
            self.parked_vehicle = vehicle
            self.is_occupied = True
        else:
            raise ValueError("Invalid vehicle type or spot already occupied.")
