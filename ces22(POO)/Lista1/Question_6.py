'''
Author: Artur Assis Alves
Date  : 07/04/2020
Title : Question 6
'''
import sys
import math
#Functions:

def is_prime (n):
    '''
    Returns True if the integer 'n' is a prime number. Otherwise, it returns False.
    To determine if 'n' is not a prime number, it is enough to check if at least one of the numbers
    from the list <2, 3, 4, ..., int(srqt(n))> divides 'n'.
    Input :
        n       -> integer

    Output:
        result  -> bool
    '''
    result = True
    if n == 1 or n == -1 or n == 0: #Special cases
        return False
    limit  = int(math.sqrt(abs(n))) #It does not support very large integers because it needs to convert it to float.
    for number in range(2, limit + 1):
        if n%number == 0: #'n' is not a prime number.
            result = False
            break
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
    test(is_prime(11))
    test(not is_prime(35))
    test(is_prime(19911121))
    test(not is_prime(1))
    test(not is_prime(-1))
    test(not is_prime(0))
    test(is_prime(2))
    test(is_prime(-2))
    test(is_prime(3))
    test(is_prime(-3))
    test(not is_prime(4))
    test(not is_prime(-4))
    test( is_prime(5))
    test( is_prime(-5))
    #Big prime numbers from http://www.primos.mat.br/2T_en.html
    test(is_prime(47055831617))
    test(not is_prime(47055831614))
    test(is_prime(47055808417))
    test(is_prime(46813264349))


#Main:
if __name__=='__main__':
    test_suite()
    #Birthday:
    '''
    (year) -> 4-digit integer from 1990 to 2020. (31 possibilities)
    (month) -> 2-digit integer from 01 to 12. (12 possibilities)
    (day) -> 2-digit integer from 01 to 30. (30 possibilities)
    (year)(month)(day) -> 8-digit integer from 19900101 to 20201230. (31*12*30 = 11160 possibilities)
    '''
    if is_prime(19940423):
        print('I was born in a prime day.')
    else:
        print('I was not born in a prime day.')
    birth_list = []
    for i in range(31): #year
        for j in range(12): #month
            for k in range(30):
                birth_list.append((1990+i)*10**4 + (1+j)*10**2 + (1+k))
    number_os_prime_numbers = 0
    for n in birth_list:
        if is_prime(n):
            number_os_prime_numbers += 1
    print('The total number of prime number in birth_list is {}'.format(number_os_prime_numbers))
    prob = number_os_prime_numbers/len(birth_list)
    print('The probability that a student has a prime number birthday is {:<.2%}'.format(prob))
    print('We expect that in a class of 100 students we have {} that was born in a prime day.'.format(int(prob*100)))




    
