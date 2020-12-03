# Exercise 7

# Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
# Write one line of Python that takes this list a and makes a new list that has only the even
# elements of this list in it.

def run():

    numbers_list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    even_list = [number for number in numbers_list if number % 2 == 0]
    print(f'Lista de numeros pares : {even_list}')


if __name__ == '__main__':
    run()
