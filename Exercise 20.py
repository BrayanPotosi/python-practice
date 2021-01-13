# Exercise 20

# Write a function that takes an ordered list of numbers (a list where the elements are in order from
# smallest to largest) and another number. The function decides whether or not the given number is inside
# the list and returns (then prints) an appropriate boolean.

# Extras:

# Use binary search.

def run():

    list_numbers = [1, 2, 3, 4, 5, 6]
    find_number = 12

    print(get_numbers(list_numbers, find_number))


def get_numbers(list_numbers, find_number):
    
    if find_number in list_numbers:
        return True
    else:
        return False


if __name__ == '__main__':
    run()
