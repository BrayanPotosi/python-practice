# Exercise 4

# Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
# (If you don’t know what a divisor is, it is a number that divides evenly into another number.
# For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

def run():
    user_num = int(input('Ingrese un numero : '))

    divisors(user_num)


def divisors(user_num):

    list_divisors = []
    for i in range(user_num):
        if user_num % (i + 1) == 0:
            list_divisors.append(i + 1)

    print(f'Lista de divisores de {user_num} : {list_divisors}')


if __name__ == '__main__':
    run()
