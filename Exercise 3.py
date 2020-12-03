# Exercise 3

# Take a list, say for example this one:
#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list that are less than 5.

# Extras

# Instead of printing the elements one by one, make a new list that has all the elements less than 5
# from this list in it and print out this new list.
# Write this in one line of Python.
# Ask the user for a number and return a list that contains only elements from the original list
# a that are smaller than that number given by the user.

def run():

    len_list = int(input('Introduzca la cantidad de elementos que tendra su lista : '))
    num_user = int(input('Escriba un numero para delimitar la lista : '))
    user_list = []

    if len_list > 0:

        for i in range(len_list):

            list_item = int(input(f'Intozuca el {i + 1} elemento : '))
            user_list.append(list_item)

        print_list(user_list, num_user)

    else:
        print('Solo se aceptan numeros positivos')

        
def print_list(user_list, num_user):

    limited_list(user_list, 5)
    limited_list(user_list, num_user)


def limited_list(user_list, num_user):
    final_list = []

    for i in range(len(user_list)):
        if user_list[i] < num_user:
            final_list.append(user_list[i])

    print( f'Lista de numeros menores que {num_user} : {final_list}')


if __name__ == '__main__':
    run()
