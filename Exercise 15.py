# Exercise 15

# Write a program (using functions!) that asks the user for a long string containing multiple words.
# Print back to the user the same string, except with the words in backwards order.
# For example, say I type the string:

# My name is Michele
# Then I would see the string:

#   Michele is name My
# shown back to me.

def run():

    user_string = str(input('Ingresa una oracion : '))
    print(reverse_string(user_string))


def reverse_string(user_string):

    reverse_sentence = user_string.split(' ')

    return ' '.join(reverse_sentence[::-1])


if __name__ == '__main__':
    run()

