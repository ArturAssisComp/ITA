'''
Author : Artur Assis Alves
Date   : 10/05/2020
Title  : Question 6
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

    def slope_from_origin(self):
	''' Returns the slope of the line from Point(0, 0) to object self. '''
        #OBS: Esse método falha nos pontos onde x é zero.
	if self == Point(0, 0):
            return "Origin."
        elif self.x == 0:
            return "Vertical line."
        return self.y/self.x
    




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
    test(Point(4, 10).slope_from_origin() == 2.5)
    test(Point(4, 0).slope_from_origin() == 0)
    test(Point(0, 0).slope_from_origin() == "Origin.")
    test(Point(0, 3).slope_from_origin() == "Vertical line.")

    
#Main:
if __name__=='__main__':
    test_suite()

