from abc import ABC, abstractmethod
from engine import CapuletEngine, SternmanEngine, WilloughbyEngine
from .car import Car
from battery import NubbinBattery, SpindlerBattery

class CarFactory:
    
    
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        new_battery = SpindlerBattery(last_service_date, current_date)
        new_engine = CapuletEngine(last_service_mileage, current_mileage)
        return Car(new_battery, new_engine)

    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
        new_battery = SpindlerBattery(last_service_date, current_date)
        new_engine = WilloughbyEngine(last_service_mileage, current_mileage)
        return Car(new_battery, new_engine)

    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light):
        new_battery = SpindlerBattery(last_service_date, current_date)
        new_engine = SternmanEngine(warning_light)
        return Car(new_battery, new_engine)

    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        new_battery = NubbinBattery(last_service_date, current_date)
        new_engine = WilloughbyEngine(last_service_mileage, current_mileage)
        return Car(new_battery, new_engine)

    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        new_battery = NubbinBattery(last_service_date, current_date)
        new_engine = CapuletEngine(last_service_mileage, current_mileage)
        return Car(new_battery, new_engine)
        



        
