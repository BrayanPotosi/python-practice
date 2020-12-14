# Exercise 12

# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list
# of only the first and last elements of the given list. For practice, write this code inside a function.

def run():
    current_list = [5, 10, 15, 20, 25]
    get_first_last(current_list)


def get_first_last(current_list):
    return [current_list[0], current_list[-1]]


if __name__ == '__main__':
    run()
