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
