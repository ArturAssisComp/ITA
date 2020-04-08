'''
Author: Artur Assis Alves
Date  : 07/04/2020
Title : Question 5
'''
import sys

#Functions:

def count_up2sam (List):
    '''
    Counts how many words (not empty and not white space sequence of characters in a string) occur in the list 'List' up to and including the first
    occurrence of the word “sam”.

    Input :
        List    -> list (list of items that can be words)

    Output:
        result  -> integer
    '''
    result = 0
    for item in List:
        if not isinstance(item, str): #item is not a word.
            continue
        else:
            word = item #item is a word.
            if word == 'sam':
                result += 1
                break
            test_word = word.strip() #eliminates white spaces words.
            if len(test_word) == 0: #item is an white space word.
                continue
            else: #item is a valid word.
                result += 1
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
    test(count_up2sam([]) == 0)
    test(count_up2sam([' ', '   ']) == 0)
    test(count_up2sam([2, 3, 4, 6]) == 0)
    test(count_up2sam([-4, 3.45, [1,2,3], {1,2,3}, {1:1, 'sam':12}]) == 0)
    test(count_up2sam([1, 2, 3, 4, 5, ['sam'], 'sam']) == 1)
    test(count_up2sam([2, 3, 'joao', 4, 5, 6, 'sAm', 'saM', 'Sam', 'sam ']) == 5)
    test(count_up2sam(['   ', '  12 wewe ' , '#%$#@%´´~~', '[]/;~´[', 'sam']) == 4) 
    test(count_up2sam(['joao', 'maria', 'jose']) == 3)
    test(count_up2sam(['sam','joao', 'maria']) ==1)
    test(count_up2sam(['joao', 'sam', 'maria', 'sam']) == 2)
    test(count_up2sam([' sam', 'sam   ', 'sam' ]) == 3)



#Main:
if __name__=='__main__':
    test_suite()

