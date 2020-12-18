# Exercise 16

# Write a password generator in Python. Be creative with how you generate passwords - strong passwords
# have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random,
# generating a new password every time the user asks for a new password.
# Include your run-time code in a main method.

# Extra:

# Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.

from random import randint, choice
from string import ascii_letters, digits, punctuation


def run():
    get_details_password()


def get_details_password():
    lvl_security = int(input('''
    Selecciona la complejidad de la contaseña
    1. Complejidad Media
    2. Complejidad Alta
    
    '''))

    generate_password(lvl_security)


def generate_password(option):

    if option > 0 and option < 3:

        words_standar = ["car", "door", "cow", "computer", "stanger", "netflix"]
        characters_hight = ascii_letters + digits + punctuation
        passw = []

        if option == 1:

            for i in range(randint(1, 2)):
                passw.append(choice(words_standar))
            print("".join(passw))
        else:

            for i in range(randint(15, 30)):
                passw.append(choice(characters_hight))
            print("".join(passw))

    else:
        print('Opcion fuera de rango')

        exit()


if __name__ == '__main__':
    run()
