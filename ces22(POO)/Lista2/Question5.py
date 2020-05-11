'''
Author : Artur Assis Alves
Date   : 10/05/2020
Title  : Question 5
'''
import string, sys

#Classes:
class Point:
    ''' Represents the cartesian coordinates of a point. '''
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return '({0}, {1})'.format(self.x, self.y)

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)

    def reflect_x(self):
        return Point(self.x, -self.y)
        
    




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
    test(Point(12, 3).reflect_x() == Point(12, -3))
    test(Point(12, 3.04).reflect_x() == Point(12, -3.04))
    test(Point(12, 0).reflect_x() == Point(12, 0))
    test(Point(1, 3).reflect_x() != Point(12, -3))
    test(Point().reflect_x() == Point())
    test(Point(0, 0.0).reflect_x() == Point(0, 0))
    
#Main:
if __name__=='__main__':
    test_suite()

