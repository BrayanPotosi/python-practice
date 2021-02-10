# Exercise 30

# In this exercise, the task is to write a function that picks a random word from a list of words from the SOWPODS dictionary.
#  Download this file and save it in the same directory as your Python code. This file is Peter Norvig’s compilation of
# the dictionary of words used in professional Scrabble tournaments. Each line in the file contains a single word.

from random import choice


def run():

    guess_letter()


def get_word():

    with open('words.txt', 'r') as words_file:
        words_list = list(words_file)
        random_word = choice(words_list).strip()
    return random_word


def print_hangmanpics(lives):
    HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

    print(HANGMANPICS[6-lives])


def guess_letter():

    word = str(get_word()).lower()

    LIVES = 6
    game = True

    print(word)

    blank_spaces = ['-'] * len(word)
    count_all_used_letters = 0
    used_letters = []

    while game:

        letter = str(input('\nIngresa una letra : ')).lower()
        print(count_all_used_letters, len(word))
        if count_all_used_letters == len(word)-1:
            print('Ganaste')
            break
        if letter in used_letters:
            print("Ya usaste esta letra")
            continue
        else:
            used_letters.append(letter)

        found = False
        count_repeated_letter = 0
        for index, letter2 in enumerate(word):
            if letter == letter2:
                found = True
                count_repeated_letter += 1
                count_all_used_letters += 1
                blank_spaces[index] = letter2

        if found:
            print(''.join(blank_spaces))

        else:
            print("Incorrecto")
            LIVES -= 1
            print_hangmanpics(LIVES)

        if LIVES == 0:
            print("Perdiste")
            break

    print("finished")


if __name__ == "__main__":
    run()