# Exercise 14

# Write a program (function!) that takes a list and returns a new list that contains all the elements
# of the first list minus all the duplicates.

# Extras:

# Write two different functions to do this - one using a loop and constructing a list, and another using sets.
# Go back and do Exercise 5 using sets, and write the solution for that in a different function.

import random


def run():

    current_set = set()
    current_list = []

    generate_random_elements(10, current_set)
    generate_random_elements(10, current_list)

    print(current_set)
    print(remove_duplicates_list(current_list))


def generate_random_elements(list_leng, structure):

    for i in range(list_leng):
        random_number = random.randint(1, 10)

        if type(structure) == list:
            structure.append(random_number)
        else:
            structure.add(random_number)


def remove_duplicates_list(current_list):

    new_list = []

    for element in current_list:
        if element not in new_list:
            new_list.append(element)

    return new_list


if __name__ == '__main__':
    run()
