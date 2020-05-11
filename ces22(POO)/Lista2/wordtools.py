'''
Author : Artur Assis Alves
Date   : 06/05/2020
Title  : wordtools
'''
import string, sys


def cleanword (word):
    for char in string.punctuation + string.digits:
        word = word.replace(char, '')
    return word

def has_dashdash(word):
    return '--' in word

def extract_words(word):
    for char in string.punctuation + string.digits:
        word = word.replace(char, ' ')
    word_list = word.split()
    for i in range(len(word_list)):
        if not word_list[i].islower():
            word_list[i] = word_list[i].lower()
    return word_list

def wordcount(word, word_list):
    return word_list.count(word)

def wordset(word_list):
    word_list = list(set(word_list))
    word_list.sort()
    return word_list

def longestword(word_list):
    max_len = 0
    for i in word_list:
        i_len = len(i)
        if i_len > max_len:
            max_len = i_len
    return max_len



def test(did_pass):
    ''' Print the result of a test.'''
    linenum = sys._getframe(1).f_lineno # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} is OK.".format(linenum)
    else:
        msg = "Test at line {0} FAILED.".format(linenum)
    print(msg)


def test_suite():
    '''
    Run the suite of tests for code in this module (this file).'''
    test(cleanword("what?") == "what")
    test(cleanword("'now!'") == "now")
    test(cleanword("?+='w-o-r-d!,@$()'") == "word")

    test(has_dashdash("distance--but"))
    test(not has_dashdash("several"))
    test(has_dashdash("spoke--"))
    test(has_dashdash("distance--but"))
    test(not has_dashdash("-yo-yo-"))

    test(extract_words("Now is the time! 'Now', is the time? Yes, now.") == ['now','is','the','time','now','is','the','time','yes','now'])
    test(extract_words("she tried to curtsey as she spoke--fancy") == ['she','tried','to','curtsey','as','she','spoke','fancy'])

    test(wordcount("now", ["now","is","time","is","now","is","is"]) == 2)
    test(wordcount("is", ["now","is","time","is","now","the","is"]) == 3)
    test(wordcount("time", ["now","is","time","is","now","is","is"]) == 1)
    test(wordcount("frog", ["now","is","time","is","now","is","is"]) == 0)

    test(wordset(["now", "is", "time", "is", "now", "is", "is"]) == ["is", "now", "time"])
    test(wordset(["I", "a", "a", "is", "a", "is", "I", "am"]) == ["I", "a", "am", "is"])
    test(wordset(["or", "a", "am", "is", "are", "be", "but", "am"]) == ["a", "am", "are", "be", "but", "is", "or"])

    test(longestword(["a", "apple", "pear", "grape"]) == 5)
    test(longestword(["a", "am", "I", "be"]) == 2)
    test(longestword(["this","supercalifragilisticexpialidocious"]) == 34)
    test(longestword([ ]) == 0)
    
#Main:
if __name__=='__main__':
    test_suite()
