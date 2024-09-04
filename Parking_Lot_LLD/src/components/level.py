from .vehicle_type import VehicleType
from .parking_spot import ParkingSpot


class Level:
    def __init__(self, level_id, num_spots, vehicle_type):
        self.level_id = level_id
        self.num_spots = num_spots
        self.vehicle_type = vehicle_type
        self.parking_spots = [ParkingSpot(i, vehicle_type) for i in range(num_spots)]

    def get_level_id(self):
        return self.level_id

    def get_num_spots(self):
        return self.num_spots

    def get_parking_spots(self):
        return self.parking_spots

    def park_vehicle(self, vehicle):
        for spot in self.parking_spots:
            if spot.is_available():
                spot.park_vehicle(vehicle)
                return True
        return False

    def get_vehicle_type(self):
        return self.vehicle_type

    def unpark_vehicle(self, vehicle):
        for spot in self.parking_spots:
            if spot.get_vehicle() == vehicle:
                spot.unpark_vehicle()
                return True
        return False

    def display_availability(self):
        print(f"Level {self.level_id} Availability:")
        for spot in self.parking_spots:
            print(
                f"Spot {spot.get_spot_number()}: {'Available' if spot.is_available() else 'Occupied'}"
            )
