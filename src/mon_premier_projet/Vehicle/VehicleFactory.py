from mon_premier_projet.Vehicle.Vehicle import *
from mon_premier_projet.Vehicle.Car import *
from mon_premier_projet.Vehicle.Truck import *
from mon_premier_projet.Vehicle.Bike import *

class VehicleFactory:
    @staticmethod
    def create_vehicle(vehicle_type: str):
        if vehicle_type == "car":
            return Car()
        elif vehicle_type == "bike":
            return Bike()
        elif vehicle_type == "truck":
            return Truck()
        else:
            raise ValueError("Vehicle type must be car, bike, truck")
