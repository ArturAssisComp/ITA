'''
Author : Artur Assis Alves
Date   : 09/06/2020
Title  : Vehicle Factory
'''
import abc

#Classes:
class VehicleInterface ():
    ''' Interface class for products.'''
    def description(self):
        return '{0}{1}.'.format(self.engine.description, self.__class__.__name__.lower())


class Car (VehicleInterface):
    pass

class Truck (VehicleInterface):
    pass

class Boat (VehicleInterface):
    pass

class Ship (VehicleInterface):
    pass

class Bus (VehicleInterface):
    pass

class Motorcycle (VehicleInterface):
    pass

class Airplane(VehicleInterface):
    pass

class EngineInterface ():
    ''' Interface class for the vehicle's engine.'''
    @abc.abstractmethod
    def __init__(self):
        pass

class ElectricMotor (EngineInterface):
    def __init__(self):
        self.description = "Electric motor "

class CombustionEngine(EngineInterface):
    def __init__(self):
        self.description = "Combustion engine "

class HybridEngine(EngineInterface):
    def __init__(self):
        self.description = "Hybrid engine "

#Factory:
class VehicleCreatorInterface:
    ''' Factory class for creating vehicles.'''
    @classmethod
    @abc.abstractmethod
    def create_vehicle(cls, vehicle_type, motor_type):
        '''
        Create a vehicle. And return its object.
        INPUT:
            vehicle_type -> string ("car", "truck", "bus",  "motorcycle", "airplane", "boat", "ship")
            motor_type   -> string("electric", "combustion", "hybrid")
        OUTPUT:
            VehicleInterface
         '''
        pass
    @staticmethod
    def create_engine(vehicle, motor_type):
        if (motor_type == "electric"):
            vehicle.engine = ElectricMotor()
        if (motor_type == "combustion"):
            vehicle.engine = CombustionEngine()
        if (motor_type == "hybrid"):
            vehicle.engine = HybridEngine()


class TerrainVehicleCreator(VehicleCreatorInterface):
    @classmethod
    def create_vehicle(cls, vehicle_type, motor_type):
        vehicle_type = vehicle_type.lower()
        motor_type   = motor_type.lower()
        vehicle      = -1

        if (vehicle_type == "car"):
            vehicle = Car()
        if (vehicle_type == "truck"):
            vehicle = Truck()
        if (vehicle_type == "bus"):
            vehicle = Bus()
        if (vehicle_type == "motorcycle"):
            vehicle = Motorcycle()

        cls.create_engine(vehicle, motor_type)
        if vehicle != -1:
            return vehicle

class SeaVehicleCreator(VehicleCreatorInterface):
    @classmethod
    def create_vehicle(cls, vehicle_type, motor_type):
        vehicle_type = vehicle_type.lower()
        motor_type   = motor_type.lower()
        vehicle      = -1
        if (vehicle_type == "ship"):
            vehicle = Ship()
        if (vehicle_type == "boat"):
            vehicle = Boat()

        cls.create_engine(vehicle, motor_type)
        if vehicle != -1:
            return vehicle
class AirVehicleCreator(VehicleCreatorInterface):
    @classmethod
    def create_vehicle(cls, vehicle_type, motor_type):
        vehicle_type = vehicle_type.lower()
        motor_type   = motor_type.lower()
        vehicle      = -1

        if (vehicle_type == "airplane"):
            vehicle = Airplane()

        cls.create_engine(vehicle, motor_type)
        if vehicle != -1:
            return vehicle


if __name__=='__main__':
    barco_eletrico       = SeaVehicleCreator.create_vehicle("boat", "electric")
    navio_combustao      = SeaVehicleCreator.create_vehicle("ship", "combustion")
    aviao_eletrico       = AirVehicleCreator.create_vehicle("airplane", "electric")
    carro_hibrido        = TerrainVehicleCreator.create_vehicle("car", "hybrid")
    motocicleta_eletrica = TerrainVehicleCreator.create_vehicle("motorcycle", "electric")
    onibus_combustao     = TerrainVehicleCreator.create_vehicle("bus", "combustion")
    onibus_eletrico      = TerrainVehicleCreator.create_vehicle("bus", "electric")
    onibus_hibrido       = TerrainVehicleCreator.create_vehicle("bus", "hybrid")
    for vehicle_type in ("car", "truck", "bus",  "motorcycle", "airplane", "boat", "ship"):
        if (vehicle_type in ("car", "truck", "bus", "motorcycle")):
            type = "terrain"
        elif (vehicle_type in ("airplane")):
            type = "air"
        else:
            type = "sea"
        for motor_type in ("electric", "combustion", "hybrid"):
            if(type == "terrain"):
                vehicle = TerrainVehicleCreator.create_vehicle(vehicle_type, motor_type)
            elif(type == "sea"):
                vehicle = SeaVehicleCreator.create_vehicle(vehicle_type, motor_type)
            else: #type == "air"
                vehicle = AirVehicleCreator.create_vehicle(vehicle_type, motor_type)
            print ("Created vehicle : {}".format(vehicle.description()))
