# Exercise 1

# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.

# Extras

# Add on to the previous program by asking the user for another number
# and printing out that many copies of the previous message.
# Print out that many copies of the previous message on separate lines

from datetime import datetime


def run():
    name = str(input('Ingrese su nombre : '))
    age = int(input('Ingrese su edad : '))
    times = int(input('Cuantas veces desea imprimir la linea ? : '))
    years = 100

    calculate_year(name, age, times, years)


def calculate_year(name, age, times, years):

    if age > 0 and age < years:

        current_year = int(datetime.now().strftime('%Y'))
        birth_year = current_year - age
        final_date = birth_year + years

        for i in range(times):

            print(f'Hola { name }, en { final_date } tendras 100 años')

    else:
        print('Su edad no es valida, por favor intenta de nuevo')


if __name__ == '__main__':
    run()
