'''
Author : Artur Assis Alves
Date   : 08/06/2020
Title  : Simulador de Estradas
'''
import abc

#Classes:
class VehicleInterface ():
    ''' Interface class for vehicles.'''
    def __init__(self, engine_class):
        self.engine = engine_class
    def description(self):
        return '{0}{1}.'.format(self.engine.description, self.__class__.__name__.lower())


class Car (VehicleInterface):
    pass

class Truck (VehicleInterface):
    pass

class Boat (VehicleInterface):
    pass

class Bus (VehicleInterface):
    pass

class Motorcycle (VehicleInterface):
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




if __name__=='__main__':
    for j in (ElectricMotor(), CombustionEngine(), HybridEngine()):
        for i in (Car(j), Truck(j), Boat(j), Bus(j), Motocycle(j)):
            print(i.description())
