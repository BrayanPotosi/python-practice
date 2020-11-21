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
