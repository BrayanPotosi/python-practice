# Exercise 11

# Ask the user for a number and determine whether the number is prime or not.
# (For those who have forgotten, a prime number is a number that has no divisors.).
# You can (and should!) use your answer to Exercise 4 to help you.
# Take this opportunity to practice using functions, described below.

from math import sqrt


def run():
    number = int(input('Ingresa un numero : '))
    check_number(number)


def is_prime(number):

    if number > 1:

        for i in range(2, int(sqrt(number))):
            if number % 2 == 0:
                return False

        return True

    else:
        print('No es primo')


def check_number(number):

    if is_prime(number):
        print(f'{number} Es primo')
    else:
        print(f'{number} No es primo')


if __name__ == '__main__':
    run()
