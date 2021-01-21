# Exercise 18

# Create a program that will play the “cows and bulls” game with the user. The game works like this:
# Randomly generate a 4-digit number. Ask the user to guess a 4-digit number.
# For every digit that the user guessed correctly in the correct place,
# they have a “cow”. For every digit the user guessed correctly in the wrong place is a “bull.”
# Every time the user makes a guess, tell them how many “cows” and “bulls” they have. Once the user guesses
# the correct number, the game is over. Keep track of the number of guesses the user makes throughout teh game
# and tell the user at the end.

from random import randint


def run():
    check_number()


def get_number():
    number_cb = str(input('Adivina el numero de 4 digitos : '))

    return number_cb


def check_number():

    random_number = str(randint(1000, 9999))
    var_run = True
    
    print(random_number)

    while var_run:

        cows = 0
        bulls = 0
        attemps = 0
        user_number = str(get_number())
        
        for i in range(len(random_number)):

            if user_number == random_number:
                print(f'Adivinaste, numero de intentos {attemps}')
                exit()
            elif user_number in random_number and user_number[i] == random_number[i]:
                cows += 1
            elif user_number in random_number:
                bulls += 1

        print(f'Tienes {cows} vacas y {bulls} Toros')

if __name__ == '__main__':
    run()
