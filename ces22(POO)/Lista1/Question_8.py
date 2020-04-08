'''
Author: Artur Assis Alves
Date  : 07/04/2020
Title : Question 8
'''


#Functions:

def table (n):
    '''
    Returns a table of multiplication with n**2 numbers.
    Input :
        n -> integer

    Output:
        None
    '''
    line1 = ' '*5 
    for i in range(1, n+1):
        line1 = line1 + '{:>4}'.format(i)
    print(line1)
    print('  :' + '-'*(len(line1) - 3))
    for line_n in range(1, n + 1):
        line = '{:>2}:  '.format(line_n)
        for col_n in range(1, n + 1):
            line = line + '{:>4}'.format(line_n*col_n)
        print(line)
    print('\n\n')

    

#Main:
if __name__=='__main__':
    table(12)

        
