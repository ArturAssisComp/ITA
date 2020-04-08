'''
Author: Artur Assis Alves
Date  : 07/04/2020
Title : Question 10
'''
import sys

#Functions:

def  add_complex(num1, num2):
    '''
    Add the complex numbers 'num1' and 'num2'. Returns the answer as a complex number.
     
    Input :
        num1   -> Complex()
        num2   -> Complex()

    Output:
        result -> Complex()
    '''
    result = Complex()
    result.t = (num1.t[0] + num2.t[0], num1.t[1] + num2.t[1])
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
    test(add_complex(A, A).t == A.t)
    test(add_complex(A, B).t == B.t)
    test(add_complex(B, A).t == B.t)
    test(add_complex(B, C).t == add_complex(C, B).t) 
    test(add_complex(add_complex(B, C), E).t == add_complex(add_complex(E, C), B).t and add_complex(add_complex(B, C), E).t == add_complex(add_complex(E, B), C).t)
    test(add_complex(C, D).t == A.t)
  
    
#Classes:
class Complex():
    '''
    Class of complex numbers.

    Attributes:
        t -> tuple of floats (real part of the number, imaginary part of the number)
    '''
    #Method:
    def print(num):
        print('{0:+.2f}{1:+.2f}i'.format(float(num.t[0]), float(num.t[1])))
        

#Main:
if __name__=='__main__':
    A = Complex()
    A.t = (0, 0)
    B = Complex()
    B.t = (2,3)
    C = Complex()
    C.t = (3,4)
    D = Complex()
    D.t = (-3, -4)
    E = Complex()
    E.t = (1, -4)
    test_suite() #Tests were executed using integers to avoid problems with float representation.
