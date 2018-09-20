'''
Prompt for a word and chack if it's a palindrome

Ignores non-alpha characters in the comparision
'''

import re

def is_palindrome(word):
    fpos = 0

    ''' Remove non alpha and space characters and lowercase the input '''

    cleanword = re.sub(r'[^a-zA-Z]', '', word.lower())
    rpos = len(cleanword) - 1

    ''' We only need to check half of the string '''

    while rpos > len(cleanword) / 2 - 1:

        if (cleanword[fpos]) != (cleanword[rpos]):
            return [False, cleanword]

        fpos += 1
        rpos -= 1

    return [True, cleanword]

print('-=[ P A L I N D R O M E T E R ]+-\n')
word = input('Enter your word: ')

response, cleanword = is_palindrome(word)

if response:
    print(cleanword, 'is a palindrome')
else:
    print(cleanword, 'is not a palindrome')
