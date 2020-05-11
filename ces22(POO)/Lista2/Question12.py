'''
Author : Artur Assis Alves
Date   : 10/05/2020
Title  : Question 12
'''
import sys

'''
Questão 12: O exemplo de polimorfismo apresentado nesse arquivo consiste no uso das operações '+', '-', '*' e '==' para
pontos em um plano cartesiano. Apesar dos operadores serem sintaticamente os mesmos, têm significados distintos de acordo com a classe
dos objetos envolvidos (Duck Typing).
'''

#classes:

class Point:
    '''
    This class defines a point in 2 dimensions using cartesian coordinates.

    Attributes:
        x -> integer
        y -> integer
    '''
    #Initializing:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    #Method str and repr:
    def __str__(self):
        return '({0},{1})'.format(self.x, self.y)

    def __repr__(self):
        return 'P({0},{1})'.format(self.x, self.y)

    
    #Operations:
    def __add__(self, other):
        '''Defines the '+' operator as it is in math.'''
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        '''Defines the '-' operator as it is in math.'''
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, fl):
        '''Defines the operation of multiplying self by a float as it is in math.'''
        return Point(self.x*fl, self.y*fl)

    def __rmul__(self, fl):
        '''Defines the operation of multiplying self by a float as it is in math. This function
        is called when the float/integer is in the left side of the object Point(), thus, it supports
        this operation in both directions.'''
        return Point(self.x*fl, self.y*fl)

    def __neg__(self):
        '''Supports the minus unary operation.'''
        return Point(-self.x, -self.y)

    def __eq__(self, other):
        '''Defines the operation '==' as it is in math. By default, '!=' is implemented if __eq__ is already implemented.'''
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        ''' Defines a hash function that makes possible the use of Point() as key in dictionaries.'''
        return hash((self.x, self.y))

    def __bool__(self):
        '''A Point() returns False if it is P(0, 0), otherwise, returns True.'''
        if self.x == 0 and self.y == 0:
            return False
        else:
            return True
        
    def __len__(self):
        '''Returns the dimension 2.'''
        return 2

#Test methods:
def test(did_pass):
    ''' Print the result of a test.'''
    linenum = sys._getframe(1).f_lineno # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} is OK.".format(linenum)
    else:
        msg = "Test at line {0} FAILED.".format(linenum)
    print(msg)


def test_suite():
    '''
    Run the suite of tests for code in this module (this file).'''
    test(Point(4, 10) == Point(4, 10))
    test(Point(0, 3))
    test(Point(3, 4.6) == Point(1, 4.6) + Point(2, 0))
    test(not Point(0, 0))
    test(Point(2, 4)*7 == Point(14, 28))
    test(7*Point(2, 4) == Point(14, 28))

    
#Main:
if __name__=='__main__':
    test_suite()
