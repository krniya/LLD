from components.vehicle_type import VehicleType
from components.car import Car
from components.motorbike import Motorbike
from components.truck import Truck
from components.level import Level
from components.parking_lot import ParkingLot


def run():
    parking_lot = ParkingLot.get_instance()
    parking_lot.add_level(Level(1, 10, VehicleType.CAR))
    parking_lot.add_level(Level(2, 10, VehicleType.TRUCK))
    parking_lot.add_level(Level(3, 10, VehicleType.MOTORBIKE))
    print(parking_lot.display_availability())

    car = Car("BR43-1223", "Red")
    truck = Truck("BR43-4356", "Black")
    motor_bike = Motorbike("BR43-7654", "Blue")

    parking_lot.park_vehicle(car)
    parking_lot.park_vehicle(truck)
    parking_lot.park_vehicle(motor_bike)
    print(parking_lot.display_availability())


if __name__ == "__main__":
    run()
