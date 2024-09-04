class ParkingLot:

    __instance = None

    def __init__(self):
        if ParkingLot.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            ParkingLot.__instance = self
            self.levels = []

    @staticmethod
    def get_instance():
        if ParkingLot.__instance is None:
            ParkingLot()
        return ParkingLot.__instance

    def add_level(self, level):
        self.levels.append(level)

    def get_levels(self):
        return self.levels

    def get_available_spots(self):
        available_spots = 0
        for level in self.levels:
            available_spots += level.get_available_spots()
        return available_spots

    def park_vehicle(self, vehicle):
        for level in self.levels:
            if level.vehicle_type == vehicle.vehicle_type and level.park_vehicle(
                vehicle
            ):
                return True
        return False

    def unpark_vehicle(self, vehicle):
        for level in self.levels:
            if level.unpark_vehicle(vehicle):
                return True
        return False

    def display_availability(self):
        for level in self.levels:
            level.display_availability()
