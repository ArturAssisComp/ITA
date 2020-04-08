'''
Author: Artur Assis Alves
Date  : 07/04/2020
Title : Question 9
'''
import sys

#Functions:

def is_palindrome (word):
    '''
    Returns True if the string 'word' is a palindrome. Returns False otherwise.
    
    Input :
        word       -> string

    Output:
        True/False -> bool
    '''
    for_word     = list(word)
    rev_word = for_word.copy()
    rev_word.reverse()
    if for_word == rev_word:
        return True
    else:
        return False
        

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
    test(is_palindrome("abba"))
    test(not is_palindrome("abab"))
    test(is_palindrome("tenet"))
    test(not is_palindrome("banana"))
    test(is_palindrome("straw warts"))
    test(is_palindrome("a"))
    test(is_palindrome("")) #"" is a palindrome.
    
#Main:
if __name__=='__main__':
    test_suite()
        
