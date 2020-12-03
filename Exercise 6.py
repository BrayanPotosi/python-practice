# Exercise 6

# Ask the user for a string and print out whether this string is a palindrome or not.
# (A palindrome is a string that reads the same forwards and backwards.)

from unicodedata import normalize


def run():

    word = str(input('Por favor ingrese una palabra o frase : ')).lower().replace(' ', '')
    word = normalize_word(word)

    check_word(word)


def check_word(word):

    reverse_word = word[::-1]

    if word == reverse_word:
        print('Es palindromo')
    else:
        print('No es un palindromo')


def normalize_word(word):

    word = normalize('NFKD', word).encode('ASCII', 'ignore')

    return word


if __name__ == '__main__':
    run()
