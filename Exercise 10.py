# Exercise 10

# This week’s exercise is going to be revisiting an old exercise (see Exercise 5),
# except require the solution in a different way.
#
# Take two lists, say for example these two:
#
# 	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# 	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# and write a program that returns a list that contains only the elements that are common between the lists
# (without duplicates). Make sure your program works on two lists of different sizes.
# Write this in one line of Python using at least one list comprehension.
# (Hint: Remember list comprehensions from Exercise 7).

# The original formulation of this exercise said to write the solution using one line of Python,
# but a few readers pointed out that this was impossible to do without using sets
# that I had not yet discussed on the blog, so you can either choose to use the original directive and read
# about the set command in Python 3.3, or try to implement this on your own and use
# at least one list comprehension in the solution.

# Extra:
#
# Randomly generate two lists to test this

import random


def run():
    list_one = [1, 2, 3, 3, 4]
    list_two = [1, 2, 3, 4, 5]

    # random_list(8, 10, list_one)
    # random_list(8, 10, list_two)

    common_numbers(list_one, list_two)


def random_list(min_length, max_length, new_list):

    for i in range(random.randint(min_length, max_length)):
        new_list.append(random.randint(1, 101))


def common_numbers(list_one, list_two):

    final_list = [x for x in list_one for y in list_two if x == y]
    final_list = set(final_list)
    final_list = list(final_list)

    print(f'Lista numero 1 : {list_one}')
    print(f'Lista numero 2 : {list_two}')
    print(f'Elementos en comun : {final_list}')


if __name__ == '__main__':
    run()
