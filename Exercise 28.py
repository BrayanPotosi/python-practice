# Exercise 28

# Implement a function that takes as input three variables,
#  and returns the largest of the three. Do this without using the Python max() function!

# The goal of this exercise is to think about some internals that Python normally takes care of for us.
#  All you need is some variables and if statements!

def run():
    first_number = int(input('Ingresa el primer numero : '))
    second_number = int(input('Ingresa el segundo numero : '))
    third_number = int(input('Ingresa el tercer numero : '))

    max_of_number(first_number, second_number, third_number)


def max_of_number(first_number, second_number, third_number):
    
    if first_number > second_number and first_number > third_number:
        print(f'El numero mayor es el numero {first_number}')
    
    elif second_number > first_number and second_number > third_number:
        print(f'El numero mayor es el numero {second_number}')

    else: 
        print(f'El numero mayor es el numero {third_number}')

if __name__ == "__main__":
    run()