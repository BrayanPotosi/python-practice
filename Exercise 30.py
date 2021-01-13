# Exercise 30

# In this exercise, the task is to write a function that picks a random word from a list of words from the SOWPODS dictionary.
#  Download this file and save it in the same directory as your Python code. This file is Peter Norvig’s compilation of 
# the dictionary of words used in professional Scrabble tournaments. Each line in the file contains a single word.

from random import choice

def run():

    print(get_word())


def get_word():
    
    with open('words.txt', 'r') as words_file:
        words_list = list(words_file)
        random_word = choice(words_list).strip()
        return random_word


if __name__ == "__main__":
    run()
