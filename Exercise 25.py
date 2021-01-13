# Exercise 25 

# In a previous exercise, we’ve written a program that “knows” a number and asks a user to guess it.

# This time, we’re going to do exactly the opposite. You, the user, will have in your head a number between 0 and 100. 
# The program will guess a number, and you, the user, will say whether it is too high, too low, or your number.

# At the end of this exchange, your program should print out how many guesses it took to get your number.

# As the writer of this program, you will have to choose how your program will strategically guess. 
# A naive strategy can be to simply start the guessing at 1, and keep going (2, 3, 4, etc.) until you hit the number. 
# But that’s not an optimal guessing strategy. An alternate strategy might be to guess 50 (right in the middle of the range), 
# and then increase / decrease by 1 as needed. After you’ve written the program, try to find the optimal strategy! 
# (We’ll talk about what is the optimal one next week with the solution.)

def run():

    list_numbers = [*range(100)] 

    print('Adivinare tu numero, escribe "X" si el numero es correcto, "M" si es mayor o "L" si es menor \n')
    
    print_results(list_numbers)


def search_number(list_numbers):

    user_response = True
    count_attempts = 0
    low = 0
    hight = len(list_numbers)

    while user_response != 'x':
        
        mid = (low + hight) // 2

        count_attempts += 1
        user_response = str(input(f'Tu numero es {mid} ? : ')).lower()

        if user_response == 'm':
            low = mid + 1

        elif user_response == 'l':
            hight = mid - 1

    return count_attempts


def print_results(list_numbers):
    
    print (f'\nNumero de intentos : {search_number(list_numbers)}\n')


if __name__ == '__main__':
    run()

