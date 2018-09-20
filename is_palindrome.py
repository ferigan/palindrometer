'''
Prompt for a word and chack if it's a palindrome

Ignores spaces and non-alpha characters in the comparision
'''

def is_palindrome(word):
    fpos = 0
    rpos = len(word) - 1

    while rpos > len(word) / 2 - 1:

        if not word[fpos].isalpha():
            fpos += 1
            continue

        if not word[rpos].isalpha():
            rpos += 1
            continue

        if (word[fpos]) != (word[rpos]):
            return False

        fpos += 1
        rpos -= 1

    return True

print('-=[ P A L I N D R O M E T E R ]+-\n')
word = input('Enter your word: ')

response = is_palindrome(word.replace(' ','').lower())

if response:
    print(word, 'is a palindrome')
else:
    print(word, 'is not a palindrome')
