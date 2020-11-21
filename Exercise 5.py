import random


def run():

    list_one = []
    list_two = []

    random_list(8, 10, list_one)
    random_list(8, 10, list_two)
    common_numbers(list_one, list_two)


def random_list(min_length, max_length, new_list):

    for i in range(random.randint(min_length, max_length)):
        new_list.append(random.randint(1, 101))


def common_numbers(list_one, list_two):

    final_list = []

    for i in list_one:
        if i in list_two:
            if i not in final_list:
                final_list.append(i)

    print(f'Lista numero 1 : {list_one}')
    print(f'Lista numero 2 : {list_two}')
    print(f'Elementos en comun : {final_list}')


if __name__ == '__main__':
    run()
