# Exercise 5

# Take two lists, say for example these two:
#  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are common between the lists
# (without duplicates). Make sure your program works on two lists of different sizes.

# Extras

# Randomly generate two lists to test this
# Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)

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
