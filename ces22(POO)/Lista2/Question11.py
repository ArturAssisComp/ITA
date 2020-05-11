'''
Author : Artur Assis Alves
Date   : 10/05/2020
Title  : Question 11
'''
import sys

#Methods

def add_even(*args):
    ''' Returns the sum of the even numbers from args. '''
    result = 0
    for i in args:
        if not(i%2):
            result += i
    return result


def adder(**kwargs):
    ''' Returns the sum of key-word arguments in string format.'''
    result = 0
    string = ''
    for i in kwargs:
        result += kwargs[i]
        if string != '':
            string = string + ' + ' + str(i)
        else: string = str(i)
    return string + ' = ' + str(result)
    
if __name__=='__main__':
    print('add_even(1, 2, 3, 4, 5, 6, 7) = {}'.format(add_even(1, 2, 3, 4, 5, 6, 7)))
    print(adder(a=1, b=23, pi=3.14))
