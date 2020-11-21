def run():

    len_list = int(input('Introduzca la cantidad de elementos que tendra su lista : '))
    num_user = int(input('Escriba un numero para delimitar la lista : '))
    user_list = []

    if len_list > 0:

        for i in range(len_list):

            list_item = int(input(f'Intozuca el {i + 1} elemento : '))
            user_list.append(list_item)

    else:
        print('Solo se aceptan numeros positivos')

    print_list(user_list, num_user)


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
