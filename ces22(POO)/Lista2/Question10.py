'''
Author : Artur Assis Alves
Date   : 10/05/2020
Title  : Question 10
'''
import sys

#Decorators:
def debugging(f):
    ''' Decorator that shows the line and the arguments of the function which is being debugged. '''
    def decorator_function(*args, **kwargs):
        linenum = sys._getframe(1).f_lineno # Get the caller's line number.
        print('Calling '+f.__name__+' at line '+str(linenum)+' with input :'+str(args)+ ' and '+str(kwargs))
        return f(*args, **kwargs)
    return decorator_function

def is_integer(f):
    ''' Decorator that verifies if the arguments of a function are integer. If they are not, it returns None. '''
    def decorator_function(*args, **kwargs):
        for i in args:
            if not(isinstance(i, int)):
                print('The arguments must be integers.')
                return None
        for i in kwargs:
            if not(isinstance(i, int)):
                print('The arguments must be integers.')
                return None
        return f(*args, **kwargs)
    return decorator_function

#Methods
@debugging
def adder(*args):
    result = 0
    for i in args:
        result += i
    return result

@is_integer
def integer_adder(*args):
    result = 0
    for i in args:
        result += i
    return result
    
#Main:
if __name__=='__main__':
    print('1+2+3 = {}\n'.format(adder(1, 2, 3)))
    print('2+3.5 = {}\n'.format(adder(2, 3.5)))

    print('1+2+3 = {}\n'.format(integer_adder(1, 2, 3)))
    print('2+3.5 = {}\n'.format(integer_adder(2, 3.5)))
    
