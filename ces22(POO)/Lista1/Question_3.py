'''
Author: Artur Assis Alves
Date  : 07/04/2020
Title : Question 3
'''

#Functions:

def sum_to(n):
    '''
    Returns the result of the sum 1+2+...+n. The formula
    (1 + n)*n/2 is used in this function. This formula is
    the sum of the first 'n' numbers of an arithmetic progression
    where the first element is '1' and the n-th is 'n'.

    Input :
        n  -> integer (must be a positive natural number)
        
    Output:
        int((1 + n)*n/2) -> integer 
    '''
    result = int(((1 + n)*n)/2)
    return result



#Main:
if __name__=='__main__':
    n = int(input('Positive integer : '))
    print('sum_to({0}) = {1}'.format(n, sum_to(n)))
