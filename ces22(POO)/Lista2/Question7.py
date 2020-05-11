'''
Author : Artur Assis Alves
Date   : 10/05/2020
Title  : Question 7
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

    def get_line_to(self, other):
        if other.x - self.x == 0:
            return 'Vertical line.'
        else:
            slope = (other.y - self.y)/(other.x - self.x)
            b     = self.y - self.x*slope
            return (slope, b)
    




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
    test(Point(4, 11).get_line_to(Point(6, 15)) == (2, 3))
    test(Point(4, 11).get_line_to(Point(6, 13)) == (1, 7))
    test(Point(3, 12).get_line_to(Point(3, 15)) == 'Vertical line.')
    slope = (7.0 - 23.04)/(3.45 - 1.3)
    b     = 23.04 - 1.3*slope
    test(Point(1.3, 23.04).get_line_to(Point(3.45, 7.0)) == (slope, b))



    
#Main:
if __name__=='__main__':
    test_suite()

