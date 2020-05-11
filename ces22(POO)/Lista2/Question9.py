'''
Author : Artur Assis Alves
Date   : 10/05/2020
Title  : Question 9
'''
import abc, sys



#Classes:


class Shape:
    geometric_type = 'Generic Shape'

    def area(self):
        raise self.NotImplementedError

    def get_geometric_type(self):
        return self.geometric_type

class Plotter:
    def plot(self, ratio, topleft):
        #Plotting logic.
        print('Plotting at {}, ratio {}.'.format(topleft, ratio))

class Polygon(Shape, Plotter):
    geometric_type = 'Polygon'

class RegularPolygon(Polygon):
    geometric_type = 'Regular Polygon'

    def __init__(self, side):
        self.side = side

class RegularHexagon(RegularPolygon):
    geometric_type = 'RegularHexagon'

    def area(self):
        return 1.5*((3**0.5)*(self.side**2))

class Square(RegularPolygon):
    geometric_type = 'Square'

    def area(self):
        return self.side*self.side

    
#Main:
if __name__=='__main__':
        square          = Square(10)
        regular_hexagon = RegularHexagon(10)
        regular_polygon = RegularPolygon(10)
        polygon         = Polygon()
        plotter         = Plotter()
        shape           = Shape()

        print('Shape')
        print(shape.__class__.mro())
        
        print('\nPlotter')
        print(plotter.__class__.mro())

        print('\nPolygon')
        print(polygon.__class__.mro())
        
        print('\nRegularPolygon')
        print(regular_polygon.__class__.mro())

        print('\nSquare')
        print(square.__class__.mro())

        print('\nRegularHexagon')
        print(regular_hexagon.__class__.mro())
        






        
