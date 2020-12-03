# Exercise 9

# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number,
# then tell them whether they guessed too low, too high, or exactly right.
# (Hint: remember to use the user input lessons from the very first exercise)

# Extras:

# Keep the game going until the user types “exit”
# Keep track of how many guesses the user has taken, and when the game ends, print this out.

import random


def run():

    min_num = 1
    max_num = 9

    check_number(min_num, max_num)


def check_number(min_num, max_num):

    random_number = random.randint(min_num, max_num)
    count = 0
    run_code = True

    while run_code:

        input_user = input('\nAdivina el numero, escribe exit para salir : ')

        if input_user == 'exit':
            print(f'\nNo lo lograste, lo intentaste {count} veces')
            run_code = False

        else:

            int_number = int(input_user)

            if int_number < random_number:
                print('\nEl numero generado es mayor')
                count += 1

            elif int_number > random_number:
                print('\nEl numero generado es menor')
                count += 1

            else:
                print(f'\nAdivinaste, el numero es {random_number}, lo intentaste {count} veces hasta lograrlo')
                run_code = False


if __name__ == '__main__':
    run()
