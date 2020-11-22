# Exercise 2

# Ask the user for a number. Depending on whether the number is even or odd,
# print out an appropriate message to the user.
# Hint: how does an even / odd number react differently when divided by 2?

# Extras

# If the number is a multiple of 4, print out a different message.
# Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
# If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

def run():
    number = int(input('Ingrese un numero : '))
    check = int(input('Ingrese el divisor : '))

    verify(number, check)


def verify(number, check):

    if number % 2 == 0:
        print('el numero es par')

        if number % 4 == 0:
            print('El numero es multiplo de 4')

    else:
        print('el numero es impar')

    if number % check == 0:
        print('El numero se puede dividir en parte iguales')


if __name__ == '__main__':
    run()
