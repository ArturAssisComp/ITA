'''
Author: Artur Assis Alves
Date  : 07/04/2020
Title : Question 4
'''
import sys

#Functions:

def sum_up2even (List):
    '''
    Sum all the elements in the list 'List' up to but not including the first even number (Is does
    not support float numbers).

    Input :
        List    -> list (list of integers)

    Output:
        result  -> integer or None if no number was added to result.
    '''
    result = None
    for number in List:
        if number%2 == 0:
            break
        else:
            if result == None:
                result  = number
            else:
                result += number
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
    test(sum_up2even([]) == None)
    test(sum_up2even([2]) == None)
    test(sum_up2even([-4]) == None)
    test(sum_up2even([0]) == None)
    test(sum_up2even([2, 3, 4, 5, 6]) == None)
    test(sum_up2even([1, 3, 5, 7, 9]) == 25)
    test(sum_up2even([27]) == 27)
    test(sum_up2even([27, 0]) == 27)
    test(sum_up2even([-3]) == -3)



#Main:
if __name__=='__main__':
    test_suite()

