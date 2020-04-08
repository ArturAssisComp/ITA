'''
Author: Artur Assis Alves
Date  : 07/04/2020
Title : Question 7
'''
import sys

#Functions:

def sum_of_squares (xs):
    '''
    Returns the sum of the squares of the numbers in the list 'xs'.
    Input :
        xs       -> list (list of integers)

    Output:
        result  -> integer
    '''
    result = 0
    for number in xs:
        result += number**2
    return result
        

def test(did_pass):
    ''' Print the result of a test.
    OBS: Função retirada dos slides Python 1.pptx.
    '''
    linenum = sys._getframe(1).f_lineno # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} is OK.".format(linenum)
    else:
        msg = "Test at line {0} FAILED.".format(linenum)
    print(msg)


def test_suite():
    '''
    Run the suite of tests for code in this module (this file).
    OBS: Função retirada dos slides Python 1.pptx.
    '''
    test(sum_of_squares([2, 3, 4]) == 29)
    test(sum_of_squares([ ]) == 0)
    test(sum_of_squares([2, -3, 4]) == 29)
    

#Main:
if __name__=='__main__':
    test_suite()
        
