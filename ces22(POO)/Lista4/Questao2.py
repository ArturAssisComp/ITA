'''
Author : Artur Assis Alves
Date   : 09/06/2020
Title  : Pizzaria
'''

BASE_COST = 1

#Classes:
class PizzaInterface:
    def get_description(self):
        return self.__class__.__name__.lower()
    def get_cost(self):
        return self.__class__.cost

class Dough(PizzaInterface):
    cost = 10*BASE_COST

class Decorator(PizzaInterface):
    def __init__(self , pizza_component):
        self.component = pizza_component
    def get_cost(self):
        return self.component.get_cost() + PizzaInterface.get_cost(self)
    def get_description(self):
        return self.component.get_description() + ', ' +PizzaInterface.get_description(self)

class Tomato (Decorator):
    cost = 2*BASE_COST
    def __init__(self, pizza_component):
        super().__init__( pizza_component)

class Cheese (Decorator):
    cost = 5*BASE_COST
    def __init__(self, pizza_component):
        super().__init__( pizza_component)

class Onion (Decorator):
    cost = 0.5*BASE_COST
    def __init__(self, pizza_component):
        super().__init__( pizza_component)

class Bacon (Decorator):
    cost = 2*BASE_COST
    def __init__(self, pizza_component):
        super().__init__( pizza_component)

class Chili (Decorator):
    cost = 0.5*BASE_COST
    def __init__(self, pizza_component):
        super().__init__( pizza_component)

class Garlic (Decorator):
    cost = 1*BASE_COST
    def __init__(self, pizza_component):
        super().__init__( pizza_component)

class Calabresa (Decorator):
    cost = 3*BASE_COST
    def __init__(self, pizza_component):
        super().__init__( pizza_component)

class Pepperoni (Decorator):
    cost = 4*BASE_COST
    def __init__(self, pizza_component):
        super().__init__( pizza_component)

class TomatoSauce (Decorator):
    cost = 2*BASE_COST
    def __init__(self, pizza_component):
        super().__init__( pizza_component)

class Egg (Decorator):
    cost = 1.5*BASE_COST
    def __init__(self, pizza_component):
        super().__init__( pizza_component)

class BellPepper(Decorator):
    cost = 2.5*BASE_COST
    def __init__(self, pizza_component):
        super().__init__( pizza_component)

if __name__=='__main__':
    portuguesa = BellPepper(Egg(Tomato(TomatoSauce(Cheese(Dough())))))
    calabresa  = Calabresa(Chili(TomatoSauce(Cheese(Dough()))))
    pepperoni  = Pepperoni(Chili(TomatoSauce(Cheese(Dough()))))
    margherita = TomatoSauce(Cheese(Dough()))
    dictionary = {"portuguesa":portuguesa, "calabresa":calabresa, "pepperoni":pepperoni, "margherita":margherita}
    for i in dictionary:
        print("{0:<11} pizza components : {1}.".format(i.capitalize(), dictionary[i].get_description()))
        print("{0:<11} pizza cost       : R${1:.2f}.".format(i.capitalize(), dictionary[i].get_cost()))
